#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/26 22:51

import argparse
import getpass
import io
import logging
import os
import re
import string
import sys

import prettytable

from . import handler
from . import logger as log
from . import pdf
from . import __version__ as version


version_info = "txffpAssistant version {}".format(version)


def get_password() -> str:
    password = getpass.getpass("enter your password: ")
    return password


def get_username() -> str:
    username = input("enter your username: ")
    return username


def get_uname_passwd() -> (str, str):
    username = get_username()
    password = get_password()
    return username, password


def authstr_parser(authstr:str) -> (str, str):
    parsed = authstr.split(":", 1)
    if len(parsed) == 1:
        username = parsed[0]
        password = get_password()
    else:
        username = parsed[0]
        password = parsed[1]
    return username, password
        
        
class MonthAction(argparse.Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        self.validator(values)
        setattr(namespace, self.dest, values)
        
    def validator(self, yearmonth):
        if not yearmonth.isdigit() or len(yearmonth) != 6:
            print("Error: 月份信息不合法，格式：year+month, 例：201805", file=sys.stderr)
            sys.exit(1)
        year = yearmonth[:4]
        month = yearmonth[4:]
        month_all = ["{:02d}".format(m) for m in range(1, 13)]
        if month not in month_all:
            print("Error: 月份信息不合法，所指定月份不存在")
            sys.exit(1)
            

class EmailAction(argparse.Action):
    
    def __call__(self, parser, namespace, value, option_string=None):
        value = value if value else self.email_regex(value)
        print("value:", value)
        sys.exit(1)
        setattr(namespace, self.dest, value)
    
    def email_regex(self, value):
        email_compile = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not email_compile.match(value):
            raise ValueError("邮件地址格式错误")
        return value
    

class AuthAction(argparse.Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        values = self.validator(values)
        setattr(namespace, self.dest, values)
        
    def validator(self, values: str):
        if values.startswith(":"):
            print("Error: 认证账户格式错误", file=sys.stderr)

        parsed = values.split(":", 1)
        if len(parsed) == 1:
            password = get_password()
            values = parsed[0] + ":" + password
        return values


class IDAction(argparse.Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        self.validator(values)
        setattr(namespace, self.dest, values)
    
    @staticmethod
    def ishexdigit(char):
        result = (char in string.hexdigits)
        return result
        
    def validator(self, values: str):
        if len(values) != 32:
            print("Error: ID信息不合法，长度不等于32", file=sys.stderr)
            sys.exit(1)
    
        resultmap = map(self.ishexdigit, values)
        if False in resultmap:
            print("Error: ID信息不合法，存在非十六进制字符")
            sys.exit(1)
            

class OutputDirAction(argparse.Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        if values == parser.get_default("output"):
            os.makedirs(values, 0o777)
            
        if not os.path.isdir(values):
            print("Error: 指定输出路径不合法或不存在", file=sys.stderr)
            sys,exit(1)
            
        setattr(namespace, self.dest, values)
        

class SleepTimeAction(argparse.Action):
    
    def __call__(self, parser, namespace, values, option_string=None):
        if values < 0:
            values = 0
        setattr(namespace, self.dest, values)


class Service(object):
    
    def __init__(self, options, logger):
        self.options = options
        self.logger = logger
        self.username = ""
        self.password = ""
        
    def auth(self):
        if hasattr(self.options, "auth") and self.options.auth:
            self.username, self.password = authstr_parser(self.options.auth)
        else:
            self.username, self.password = get_uname_passwd()

    def login(self):
        self.auth()
    
        self.logger.info("模拟登陆中...")
        authed_session = handler.authenticated_session(
            self.username,
            self.password,
            logger=self.logger,
            session_auto_close=False,
            sleep_time=self.options.sleep_time
        )
        return authed_session
            
    def run(self):
        pass
    

class EtcService(Service):
    
    @staticmethod
    def get_etc_info(handler, etc_type):
        return handler.get_cardlist(etc_type)
    
    @staticmethod
    def pt_add_rows(pt: prettytable.PrettyTable,
                      etcinfo: [handler.CardInfo],
                      row_names) -> str:
        pt.clear_rows()
        
        for index, info in enumerate(etcinfo, 1):
            row = [getattr(info, row_name) for row_name in row_names]
            row.insert(0, index)
            pt.add_row(row)
        pt_string = pt.get_string()
        pt.clear_rows()
        return pt_string
        
    def run(self):
        authed_session = self.login()
        
        etc_handler = handler.ETCCardHandler(
            session=authed_session,
            logger=self.logger,
            sleep_time=self.options.sleep_time
        )
        
        etc_type = self.options.etc_type.upper()
        if etc_type == "ALL":
            p_etcinfo = self.get_etc_info(etc_handler, "PERSONAL")
            c_etcinfo = self.get_etc_info(etc_handler, "COMPANY")
        elif etc_type == "PERSONAL":
            p_etcinfo = self.get_etc_info(etc_handler, "PERSONAL")
        elif etc_type == "COMPANY":
            c_etcinfo = self.get_etc_info(etc_handler, "COMPANY")

        self.logger.info("已完成ETC卡信息的获取")
        field_names = ["ID", "ETC Type", "Region", "Plate Number", "Page", "IC Card", "ETC ID"]
        row_names = ["card_type", "region", "carnum", "page_num", "iccard", "etc_id"]
        pt = prettytable.PrettyTable(field_names)

        local_keys = locals().keys()
        if "p_etcinfo" in local_keys and "c_etcinfo" in local_keys:
            self.logger.info("\n" + self.pt_add_rows(pt, p_etcinfo, row_names))
            self.logger.info("\n" + self.pt_add_rows(pt, c_etcinfo, row_names))
            # self.logger.info("单位卡{}张，个人卡{}张".format(len(c_etcinfo), len(p_etcinfo)))
        elif "p_etcinfo" in local_keys:
            self.logger.info("\n" + self.pt_add_rows(pt, p_etcinfo, row_names))
            # self.logger.info("个人卡{}张".format(len(p_etcinfo)))
        elif "c_etcinfo" in local_keys:
            self.logger.info("\n" + self.pt_add_rows(pt, c_etcinfo, row_names))
            # self.logger.info("单位卡{}张".format(len(c_etcinfo)))
        
        
class RecordService(Service):
    
    def run(self):
        authed_session = self.login()
        
        rd_handler = handler.InvoiceRecordHandler(
            session=authed_session,
            logger=self.logger,
            sleep_time=self.options.sleep_time
        )

        user_type = self.options.user_type.upper()
        card_id = self.options.etc_id
        month = self.options.month

        record_info = rd_handler.get_record_info(card_id, month, user_type)
        # record_info = [ri for ri_iter in inv_rd for ri in ri_iter]
        self.logger.info("已完成发票记录信息的获取")
        
        field_names = ["ID", "年月", "申请时间", "抬头", "纳税人识别号/统一社会信用代码", "类型",
                       "金额", "数量", "状态", "页码", "ETC ID", "Invoice ID"]
        row_names = ["month", "date", "company", "taxpaper_id", "inv_type", "amount",
                     "inv_count", "status", "page_num", "etc_id", "record_id"]
        pt = prettytable.PrettyTable(field_names)
        
        for index, info in enumerate(record_info, 1):
            row = [getattr(info, row_name) for row_name in row_names]
            row.insert(0, index)
            pt.add_row(row)
        self.logger.info("\n" + pt.get_string())
        # self.logger.info("共{}条发票记录".format(len(record_info)))
   
   
class InvDlService(Service):
    
    def __init__(self, *args, **kwargs):
        super(InvDlService, self).__init__(*args, **kwargs)
        self.dl_success = 0
        self.dl_failed = 0
        self.dl_failed_list = list()
        
        # check save direction is exist
        if not os.path.exists(self.options.output):
            os.makedirs(self.options.output, 0o777)
        
        self.merge_dir = os.path.join(self.options.output, "merged")
        if not os.path.exists(self.merge_dir) and self.options.merge:
            os.makedirs(self.merge_dir, 0o777)
    
    def download(self, record_id, etc_id, record_info, etc_type, **kwargs):
        response = handler.invpdf_cld_dl(self.authed_session, etc_id, record_id)
        if not response.status_code == 200:
            self.logger.error("文件下载失败，ETC ID: {}, Record ID: {}, Error:".format(
               etc_id, record_id, response.reason))
            return
        
        if "etc_info" in kwargs:
            etc_info = kwargs["etc_info"]
            filename = "txffp-{month}-{type}-{region}-{carnum}-{record_id}.zip"
            filename = filename.format(
                month=record_info.month, type=etc_type, region=etc_info.region,
                carnum=etc_info.carnum, record_id=record_id)
            filepath = os.path.join(self.options.output, filename)
        else:
            filename = "txffp-{month}-{type}-{record_id}.zip"
            filename = filename.format(
                month=record_info.month, type=etc_type, record_id=record_id)
            filepath = os.path.join(self.options.output, filename)

        with open(filepath, "wb") as f:
            f.write(response.content)
            
        tf = io.BytesIO(response.content)
        tf.name = filename
        
        if self.options.merge:
            pdf.auto_merger(tf, self.merge_dir)
            self.logger.info("pdf发票文件合并成功")
        return filename
    
    def record_dl(self, etc_id, etc_type, **kwargs):
        if self.options.etc_id:
            sac = True
        else:
            sac = False
            
        rd_handler = handler.InvoiceRecordHandler(
            session=self.authed_session,
            logger=self.logger,
            session_auto_close=sac,
            sleep_time=self.options.sleep_time
        )
        
        if "etc_info" not in kwargs:
            field_names = ["ID", "ETC类型", "年月", "发票数量", "金额",
                           "页码", "ETC ID", "Record ID", "文件名"]
            pt = prettytable.PrettyTable(field_names)
            pt.align["金额"] = "r"
            pt.align["发票数量"] = "l"
        else:
            etc_info = kwargs["etc_info"]
            pt = kwargs["pt"]
        
        inv_rd = rd_handler.get_record_info(etc_id, self.options.month, etc_type)
        for info in inv_rd:
            filename = self.download(info.record_id,
                                     info.etc_id,
                                     record_info=info,
                                     etc_type=etc_type,
                                     **kwargs)
            if filename:
                self.dl_success += 1
                self.logger.info("[{}] 下载成功".format(filename))
                
                if "etc_info" not in kwargs:
                    row = [len(pt._rows) + 1, info.etc_type, info.month, info.inv_count,
                           info.amount, info.page_num, info.etc_id, info.record_id, filename]
                else:
                    row = [len(pt._rows) + 1, info.etc_type, etc_info.region, etc_info.carnum,
                           info.month, info.inv_count, info.amount, info.page_num, info.etc_id,
                           info.record_id, filename]
                pt.add_row(row)
            else:
                self.dl_failed += 1
                self.dl_failed_list.append(info)

        if "etc_info" not in kwargs:
            self.logger.info("\n" + pt.get_string())
    
    def etc_dl(self, etc_type):
        etc_handler = handler.ETCCardHandler(
            session=self.authed_session,
            logger=self.logger,
            sleep_time=self.options.sleep_time
        )
        
        etc_info = etc_handler.get_cardlist(etc_type)
        field_names = ["ID", "ETC类型", "区域", "车牌号", "年月", "发票数量",
                       "金额", "页码", "ETC ID", "Record ID", "文件名"]
        pt = prettytable.PrettyTable(field_names)
        pt.align["金额"] = "r"
        pt.align["发票数量"] = "l"
        
        for info in etc_info:
            self.record_dl(info.etc_id, etc_type, etc_info=info, pt=pt)
        self.logger.info("\n" + pt.get_string())
                
    def run(self):
        self.authed_session = self.login()
        
        etc_type = self.options.etc_type.upper()
        
        if self.options.etc_id:
            if etc_type == "ALL":
                self.record_dl(self.options.etc_id, "COMPANY")
                self.record_dl(self.options.etc_id, "PERSONAL")
            elif etc_type == "PERSONAL":
                self.record_dl(self.options.etc_id, "PERSONAL")
            else:
                self.record_dl(self.options.etc_id, "COMPANY")
            return
        
        if self.options.dl_all:
            # print("download all")
            if etc_type == "ALL":
                self.etc_dl("COMPANY")
                self.etc_dl("PERSONAL")
            elif etc_type == "PERSONAL":
                self.etc_dl("PERSONAL")
            else:
                self.etc_dl("COMPANY")
            return
        

class ApplyService(Service):
    
    def __init__(self, *args, **kwargs):
        super(ApplyService, self).__init__(*args, **kwargs)
        self.authed_session = self.login()
        self.apply_handler = handler.InvoiceApplyHandler(
            session=self.authed_session,
            session_auto_close=False,
            sleep_time=self.options.sleep_time,
            logger=self.logger
        )
    
    def etc_info_all(self):
        etc = handler.ETCCardHandler(
            logger=self.logger,
            session=self.authed_session,
            session_auto_close=False,
            sleep_time=self.options.sleep_time
        )
        for user_type in ["PERSONAL", "COMPANY"]:
            yield from etc.get_cardlist(user_type)
    
    def apply(self, etc_id):
        self.apply_handler.apply_etc(
            etc_id=etc_id,
            month=self.options.month,
            email=self.options.email,
            start_month="",
            end_month=""
        )
    
    def apply_all(self):
        for etc_info in self.etc_info_all():
            self.apply(etc_info.etc_id)
    
    def run(self):
        if self.options.apply_etc_id:
            self.logger.info("单ETC开票[{}]".format(self.options.month))
            self.apply(self.options.apply_etc_id)
        else:
            self.logger.info("全部ETC卡开票[{}]".format(self.options.month))
            self.apply_all()
        self.authed_session.close()


def main():
    description = "使用过程中出现问题，请到https://github.com/Kairu-Madigan/txffpAssistant发起issue。"
    parser= argparse.ArgumentParser(description=description)
    parser.add_argument("-d", "--debug", action="store_true", help="debug模式")
    parser.add_argument("-s", "--simple", action="store_true", dest="simple", help="精简模式")
    parser.add_argument("-v", "--version", action="version", version=version_info,
                        help="查看当前版本并退出")
    parser.add_argument("--sleep", action=SleepTimeAction, dest="sleep_time", default=0,
                        type=float, help="请求间隔睡眠时间(s),默认关闭。(推荐使用)")

    service_subparser = parser.add_subparsers(title="Commands", dest="command")
    
    # etc card list
    service_etc = service_subparser.add_parser("etc", help="查看ETC卡信息")
    service_etc.add_argument("--type", dest="etc_type", choices=["personal", "company", "all"],
                                  default="all", help="etc卡类型，默认：all")
    service_etc.add_argument("--auth", action=AuthAction, dest="auth", type=str,
                                  help="用户名和密码，格式：user:password")
    
    # invoice record
    service_record = service_subparser.add_parser("record" ,help="查看开票记录")
    service_record.add_argument("--etcid", action=IDAction ,dest="etc_id", type=str, required=True,
                                help="ETC卡ID")
    service_record.add_argument("--month", action=MonthAction, dest="month", type=str,
                                required=True, help="开票年月，例如: 201805")
    service_record.add_argument("--type", dest="user_type", choices=["personal", "company"],
                                  default="company", help="etc卡类型，默认：company")
    service_record.add_argument("--auth", action=AuthAction, dest="auth", type=str,
                                help="用户名和密码，格式：user:password")
    
    # invoice download
    service_inv_dl = service_subparser.add_parser("inv-dl", help="下载发票")
    service_inv_dl.add_argument("--month", action=MonthAction, dest="month", type=str,
                                required=True, help="开票年月，例如: 201805")
    service_inv_dl.add_argument("--type", dest="etc_type", choices=["personal", "company", "all"],
                                  default="company", help="etc卡类型，默认：company")
    service_inv_dl.add_argument("--merge", dest="merge", action="store_true",
                                help="自动合并，默认关闭")
    service_inv_dl.add_argument("--auth", action=AuthAction, dest="auth", type=str,
                                help="用户名和密码，格式：user:password")
    inv_dl_group = service_inv_dl.add_mutually_exclusive_group()
    inv_dl_group.add_argument("--all", dest="dl_all", type=bool, default=True, help="下载全部发票")
    inv_dl_group.add_argument("--etcid", action=IDAction, dest="etc_id", type=str, help="ETC卡ID")
    service_inv_dl.add_argument("-o", "--output", type=str, action=OutputDirAction,
                                default=os.path.join(os.getcwd(), "txffp"),
                                help="保存位置, 默认：当前目录的txffp目录下")
    
    # invoice apply
    service_apply = service_subparser.add_parser("apply", help="自动开票<Beta>")
    service_apply.add_argument("--auth", action=AuthAction, dest="auth", type=str,
                               help="用户名和密码，格式：user:password")
    service_apply.add_argument("--month", action=MonthAction, dest="month", type=str,
                               required=True, help="开票年月，例: 201805")
    service_apply.add_argument("--email", action=EmailAction, dest="email", type=str,
                               default="", help="发票接收邮箱")
    apply_group = service_apply.add_mutually_exclusive_group()
    apply_group.add_argument("--all", dest="apply_all", type=bool, default=True,
                             help="全部ETC卡开票（默认）")
    apply_group.add_argument("--etcid", action=IDAction, dest="apply_etc_id",
                             type=str, help="指定ETC卡（需要etcid）")

 



    if len(sys.argv) == 1:
        parser.print_help(file=sys.stdout)
    
    options = parser.parse_args()
    
    if options.simple:
        logger = log.stream_logger("%(message)s")
    else:
        logger = log.stream_logger()
    # debug mode
    if options.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("启用debug模式")

    if options.command:
        command = options.command
        if "-" in command:
            cmds = command.split("-")
            cmds = [cmd.title() for cmd in cmds]
            command = "".join(cmds)
        else:
            command = command.title()

        class_name = command + "Service"
        try:
            service = eval(class_name)(options, logger)
            service.run()
        except KeyboardInterrupt:
            print("已终止程序...", file=sys.stderr)
            sys.exit(1)
        except Exception as err:
            if options.debug:
                import traceback
                traceback.print_exc()
            else:
                print(err, file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
