#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020-07-23 12:36

import datetime
import os
import re
from dateutil.relativedelta import relativedelta

from lxml import etree

from .. import exceptions
from ..handler import base


__all__ = ["CardInfo", "ETCCardHandler", "InvoiceRecordHandler", "invpdf_cld_dl",
           "InvoiceApplyHandler"]
FAILED_RETRY = 3


class CardInfo(object):
    __slots__ = ["region", "etc_id", "iccard", "carnum", "page_num", "card_type"]
    
    def __init__(self, **kwargs):
        self.region = kwargs.get("region") or None
        self.etc_id = kwargs.get("etc_id") or None
        self.iccard = kwargs.get("iccard") or None
        self.carnum = kwargs.get("carnum") or None
        self.page_num = kwargs.get("page_num") or None
        self.card_type = kwargs.get("card_type") or None


class RecordInfo(object):
    __slots__ = ["date", "month", "etc_id", "status", "amount", "company",
                 "page_num", "inv_type", "etc_type", "inv_count", "record_id",
                 "taxpaper_id"]
    
    def __init__(self, **kwargs):
        self.date = kwargs.get("date") or None
        self.month = kwargs.get("month") or None
        self.etc_id = kwargs.get("etc_id") or None
        self.status = kwargs.get("status") or None
        self.amount = kwargs.get("amount") or None
        self.company = kwargs.get("company") or None
        self.page_num = kwargs.get("page_num") or None
        self.inv_type = kwargs.get("inv_type") or None
        self.etc_type = kwargs.get("etc_type") or None
        self.inv_count = kwargs.get("inv_count") or None
        self.record_id = kwargs.get("record_id") or None
        self.taxpaper_id = kwargs.get("taxpaper_id") or None


class ETCCardHandler(base.GeneralHandler):
    carinfo_log_format = (
        "etc卡信息（第{page_num}页）\n"
        "{etc_id_nm:>20}:  {etc_id}\n"
        "{iccard_nm:>20}:  {iccard}\n"
        "{carnum_nm:>20}:  {carnum}\n"
        "{region_nm:>20}:  {region}\n"
        "{type_nm:>20}:  {card_type}\n"
    )
    
    # carinfo_exteral = dict(
    #     cardid_nm="ETC ID",
    #     iccard_nm="IC CARD",
    #     carnum_nm="PLATE NUMBER",
    #     region_nm="REGION",
    #     type_nm="TYPE",
    # )
    
    def api_card_list(self, user_type, page_num=1,
                      type_="invoiceApply", change_view="card",
                      query_str=""):
        url = "https://pss.txffp.com/pss/app/login/cardList/manage"
        method = "POST"
        data = {
            "userType": user_type,
            "type": type_,
            "changeView": change_view,
            "queryStr": query_str,
            "pageNo": page_num,
        }
        response = self.request(
            url=url,
            data=data,
            method=method)
        return response
    
    def api_card_binding(self, user_type, page_num=1,
                         change_view="card", query_str=""):
        url = "https://pss.txffp.com/pss/app/login/cardBinding/manage"
        method = "POST"
        data = {
            "userType": user_type,
            "changeView": change_view,
            "queryStr": query_str,
            "pageNo": page_num,
        }
        response = self.request(
            url=url,
            method=method,
            data=data)
        return response
    
    def get_cardlist(self, user_type="COMPANY"):
        page_num = 1
        while True:
            self.logger.info("开始获取第{}页的ETC卡信息...".format(page_num))
            
            response = self.api_card_list(user_type, page_num)
            if not response.content:
                raise exceptions.NoneResponseError("获取etc卡数据失败，原因：响应为空")
            
            cardinfos = self._get_cardlist_cardinfo(
                response.text, user_type, page_num)
            yield from cardinfos
            
            if self.has_next_page(response.text):
                page_num += 1
            else:
                break
    
    def _get_bind_cardinfo(self, html, card_type, page_num):
        node = etree.HTML(html)
        card_nodes = node.xpath(
            "//dl[contains(@class,'etc_card_dl')]/div/a[2]")
        
        for card_node in card_nodes:
            data = dict(
                region=card_node.xpath("./dt/text()")[0],
                etc_id=card_node.get("href").split("/")[-2],
                iccard=card_node.xpath("./dd[1]/text()")[0].strip()[-20:],
                carnum = card_node.xpath("./dd[2]/text()")[0].strip()[-7:],
                page_num=page_num,
                card_type=card_type
            )
            cardinfo = CardInfo(**data)
            # cardinfo = {
            #     "region": region,
            #     "iccard": iccard.strip()[-20:],
            #     "carnum": carnum.strip()[-7:],
            #     "cardid": cardid,
            #     "card_type": card_type,
            # }
            
            self.logger.debug(self.carinfo_log_format.format(
                etc_id_nm="ETC ID",
                iccard_nm="IC CARD",
                carnum_nm="PLATE NUMBER",
                region_nm="REGION",
                type_nm="TYPE",
                **data))
            yield cardinfo
    
    def _get_cardlist_cardinfo(self, html, card_type, page_num):
        node = etree.HTML(html)
        card_nodes = node.xpath(
            "//dl[@class='etc_card_dl']/div[@class='etc_card_div']")
        
        for card_node in card_nodes:
            data = dict(
                region=card_node.xpath("./a/dt/text()")[0],
                iccard=card_node.xpath("./a/dd[1]/text()")[0].strip()[-20:],
                carnum=card_node.xpath("./a/dd[2]/text()")[0].strip()[4:],
                etc_id=card_node.xpath("./a")[0].get("onclick")[13:-2],
                page_num=page_num,
                card_type=card_type
            )
            cardinfo = CardInfo(**data)
            
            # cardinfo = {
            #     "region": region,
            #     "iccard": iccard.strip()[-20:],
            #     "carnum": carnum.strip()[4:],
            #     "cardid": cardid,
            #     "card_type": card_type,
            #     "page_num": page_num
            # }
            
            self.logger.debug(self.carinfo_log_format.format(
                etc_id_nm="ETC ID",
                iccard_nm="IC CARD",
                carnum_nm="PLATE NUMBER",
                region_nm="REGION",
                type_nm="TYPE",
                **data))
            yield cardinfo


class InvoiceRecordHandler(base.GeneralHandler):
    """发票记录"""
    
    record_info_log_format = (
        "{month}发票记录信息（第{page_num}页）\n"
        "{etc_id_nm:>20}:  {etc_id}\n"
        "{record_id_nm:>20}:  {record_id}\n"
        "{apply_date_nm:>20}:  {date}\n"
        "{amount_nm:>20}:  {amount}\n"
        "{inv_type_nm:>20}:  {inv_type}\n"
        "{company_nm:>20}:  {company}\n"
        "{taxpaper_id_nm:>20}:  {taxpaper_id}\n"
        "{inv_count_nm:>20}:  {inv_count}\n"
        "{status_nm:>20}:  {status}\n"
    )
    
    # carinfo_exteral = dict(
    #     etc_id_nm="ETC ID",
    #     inv_id_nm="RECORD ID",
    #     apply_date_nm="APPLY DATETIME",
    #     amount_nm="AMOUNT",
    #     inv_type_nm="TYPE",
    #     company_nm="COMPANY",
    #     taxpaper_id_nm="TAXPAPER ID",
    #     inv_count_nm="COUNT",
    #     status_nm="STATUS",
    # )
    
    def api_query_apply(self, card_id, month, page_size=6,
                        user_type="COMPANY", title_name="",
                        station_name=""):
        url = "https://pss.txffp.com/pss/app/login/invoice/query/queryApply"
        method = "POST"
        data = {
            "pageSize": page_size,
            "cardId": card_id,
            "userType": user_type,
            "month": month,
            "titleName": title_name,
            "stationName": station_name,
        }
        response = self.request(
            url=url,
            data=data,
            method=method)
        return response
    
    def api_query_trade(self, card_id, month, page_size=6,
                        user_type="COMPANY", title_name="",
                        station_name=""):
        url = "https://pss.txffp.com/pss/app/login/invoice/query/queryTrade"
        method = "POST"
        data = {
            "pageSize": page_size,
            "cardId": card_id,
            "userType": user_type,
            "month": month,
            "titleName": title_name,
            "stationName": station_name,
        }
        response = self.request(
            url=url,
            data=data,
            method=method)
        return response
    
    def get_record_info(self, card_id, month, user_type,
                        page_size=6, title_name="", station_name=""):
        page_num = 1
        while True:
            response = self.api_query_apply(
                month=month,
                card_id=card_id,
                page_size=page_size,
                user_type=user_type,
                title_name=title_name,
                station_name=station_name)
            if not response.content:
                raise exceptions.NoneResponseError("获取发票记录信息失败，原因：服务器响应为空")
            
            record_info_iter = self._get_query_apply_data(
                response.text, page_num, month, card_id, user_type)
            yield from record_info_iter
            
            if self.has_next_page(html=response.text):
                page_num += 1
            else:
                break
    
    def _get_query_apply_data(self, html, page_num, month, etc_id, user_type):
        node = etree.HTML(html)
        record_nodes = node.xpath("//table[@class='table_wdfp']")
        
        for record_node in record_nodes:
            data = dict(
                date=record_node.xpath("./tr[1]/td/table/tr[1]/th[1]/text()")[0][7:],
                taxpaper_id=record_node.xpath(".//tr[2]/td[1]/table/tr[1]/td[2]/text()")[0],
                inv_count=record_node.xpath(".//tr[2]/td[1]/table/tr[1]/td[3]/span/text()")[0],
                inv_type=record_node.xpath("./tr[1]/td/table/tr[1]/th[3]/text()")[0],
                company=record_node.xpath(".//tr[2]/td[1]/table/tr[1]/td[1]/text()")[0],
                record_id=record_node.xpath("./tr[1]/td/table/tr/th[4]/a[1]")[0].get("href").split("/")[-4],
                amount=record_node.xpath("./tr[1]/td/table/tr[1]/th[2]/span/text()")[0][2:],
                status=record_node.xpath(".//tr[2]/td[1]/table/tr[1]/td[4]/span/text()")[0],
                month=month,
                etc_id=etc_id,
                page_num=page_num,
                etc_type=user_type
            )
            data["company"] = re.sub("\n|\s", "", data["company"])[5:]
            data["taxpaper_id"] = re.sub("\n|\s", "", data["taxpaper_id"])[16:]
            record_info = RecordInfo(**data)
            
            # record_info = dict(
            #     taxpaper_id=taxpaper_id,
            #     apply_date=apply_date,
            #     inv_count=inv_count,
            #     inv_type=inv_type,
            #     company=company,
            #     amount=amount,
            #     inv_id=inv_id,
            #     etc_id=etc_id,
            #     status=status,
            #     month=month,
            # )
            
            self.logger.debug(self.record_info_log_format.format(
                etc_id_nm="ETC ID",
                record_id_nm="RECORD ID",
                apply_date_nm="APPLY DATETIME",
                amount_nm="AMOUNT",
                inv_type_nm="TYPE",
                company_nm="COMPANY",
                taxpaper_id_nm="TAXPAPER ID",
                inv_count_nm="COUNT",
                status_nm="STATUS",
                **data))
            yield record_info
            
            
class InvoiceApplyHandler(base.GeneralHandler):
    
    def auto_month_range(self):
        now = datetime.datetime.now()
        past = now - relativedelta(months=2)
        now_str = now.strftime("%Y%m")
        past_str = past.strftime("%Y%m")
        return now_str, past_str
    
    def api_apply_submit(self, etc_id, apply_id, user_type):
        url = "https://pss.txffp.com/pss/app/login/invoice/consumeTrans/submitApply"
        method = "POST"
        data = {
            "applyId": apply_id,
            "id": etc_id,
            "userType": user_type,
        }
        return self.request(url, method, data)
    
    def api_consume_trans_apply(self, etc_id, trade_id_list, month,
                                start_month, end_month, email="", title_id="",
                                user_type="", query_type="", page_no=1):
        url = "https://pss.txffp.com/pss/app/login/invoice/consumeTrans/apply"
        method = "POST"
        data = {
            "id": etc_id,
            "tradeIdList": trade_id_list,
            "titleId": title_id,
            "invoiceMail": email,
            "userType": user_type,
            "month": month,
            "startMoth": start_month,
            "endMoth": end_month,
            "queryType": query_type,
            "pageNo": page_no,
        }
        return self.request(url, method, data)
    
    def api_consume_trans(self, etc_id, month, start_month=None, end_month=None,
                          page_no=1, user_type="", trade_id_list="",
                          email="", query_type="", title_id=""):
        url = "https://pss.txffp.com/pss/app/login/invoice/consumeTrans/manage"
        method = "POST"
        data = {
            "id": etc_id,
            "tradeIdList": trade_id_list,
            "titleId": title_id,
            "invoiceMail": email,
            "userType": user_type,
            "month": month,
            "startMoth": start_month,
            "endMoth": end_month,
            "queryType": query_type,
            "pageNo": page_no,
        }
        return self.request(url, method, data)
    
    def apply_id_submit(self, etc_id, apply_id, user_type):
        response = self.api_apply_submit(etc_id, apply_id, user_type)
        if response.status_code != 200:
            err_msg = "开票失败，提交applyid响应码非200，原因：{}"
            self.logger.error(err_msg.format(response.reason))
        self.logger.info("开票成功，etc_id: {} [{}]".format(etc_id, user_type))
        
    def apply_etc(self, etc_id, month, email="", start_month=None, end_month=None):
        self.logger.info("etcId: {}[{}]开票中...".format(etc_id, month))
        trade_ids = self.get_trade_ids(
            etc_id=etc_id,
            month=month,
            email=email,
            start_month=start_month,
            end_month=end_month
        )
        trade_id_list = list()
        for trade_id in trade_ids:
            trade_id_list.append(trade_id)
        trade_id_list = ",".join(trade_id_list)

        response = self.api_consume_trans_apply(
            etc_id=etc_id,
            trade_id_list=trade_id_list,
            month=month,
            start_month=start_month,
            end_month=end_month,
            email=email
        )
        if response.status_code != 200:
            msg = "获取applyid信息失败，错误信息：{}"
            self.logger.error(msg.format(response.reason))
        
        try:
            apply_id, user_type = self.apply_id_html_parser(response.content)
        except IndexError as err:
            msg = "无法获取applyid信息，可能时没有需要执行开票的内容项目，err: {}"
            self.logger.warn(msg.format(err))
        # self.apply_id_submit(etc_id, apply_id, user_type)
    
    def get_trade_ids(self, *args, **kwargs):
        if not kwargs["start_month"] or not kwargs["end_month"]:
            kwargs["start_month"], kwargs["end_month"] = self.auto_month_range()
            
        page_num = 1
        while True:
            failed = 0
            for _ in range(FAILED_RETRY):
                response = self.api_consume_trans(page_no=page_num, *args, **kwargs)
                if response.status_code != 200:
                    failed += 1
                    msg = "请求{}失败，3秒后重新请求。（失败次数: {}）"
                    self.logger.error(msg.format(response.url, failed))
                    if failed == FAILED_RETRY:
                        break
                else:
                    break
                    
            content = response.content
            trade_ids = self.tradeids_html_parser(content)
            yield from trade_ids
            
            if self.has_next_page(content):
                page_num += 1
            else:
                break
        
    def tradeids_html_parser(self, html):
        self.logger.debug("解析响应报文，提取trade id")
        root = etree.HTML(html)
        nodes = root.xpath('//tr/td[@class="tab_tr_td10"]/input[@class="check_one"]')
        
        for node in nodes:
            id_ = node.get("id")
            tradeid = re.match(r"[^_]*", id_).group()
            if not tradeid:
                continue
            self.logger.debug("成功提取tradeId: {}".format(tradeid))
            yield tradeid
    
    def apply_id_html_parser(self, html):
        self.logger.debug("解析响应报文，提取applyId和userType信息")
        root = etree.HTML(html)
        node = root.xpath("//form[@id='checkForm']")[0]
        apply_id = node.xpath("./input[@id='applyId']")[0].get("value")
        user_type = node.xpath("./input[@id='userType']")[0].get("value")
        self.logger.debug("成功提取数据，applyId: {}".format(apply_id))
        return apply_id, user_type
            
            
def invpdf_cld_dl(session, card_id, inv_id):
    url = (
        "https://pss.txffp.com/pss/app/login/invoice/"
        "query/download/{inv_id}/{card_id}/APPLY"
    )
    url = url.format(card_id=card_id, inv_id=inv_id)
    response = session.get(url=url)
    return response
