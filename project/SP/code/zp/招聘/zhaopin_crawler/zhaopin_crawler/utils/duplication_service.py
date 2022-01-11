# -*- coding: utf-8 -*-
# @Author : Young Cc
# @Time   : 2021/08/04
# @File   : duplication_service.py

import json
import requests
from zhaopin_crawler.settings import DUP_SERVICE_URL, DUP_DOWNLOAD_TIMEOUT

false, true, null = False, True, None
session = requests.session()
headers = {
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Content-Type": "application/json; charset=UTF-8",
}


class DuplicationService(object):
    """去重服务类"""

    def get_query(self, channel_id, url) -> bool:
        """
        查询去重目标是否在去重服务中，不存在不会进行注册。
        :param channel_id: 通道标识
        :param url: 采集目标地址
        """
        data = {"channel": channel_id, "target": url}
        try:
            response = session.get(DUP_SERVICE_URL, params=data, headers=headers, timeout=DUP_DOWNLOAD_TIMEOUT)
            res = json.loads(response.content.decode("utf-8"))
            print(res)
            return res.get("targetExists", True)
        except:
            return True

    def get_nrply(self, channel_id, url) -> int:
        """
        查询去重目标评论总数，并返回，不存在不会进行注册。
        :param channel_id: 通道标识
        :param url: 采集目标地址
        """
        data = {"channel": channel_id, "target": url}
        try:
            response = session.get(DUP_SERVICE_URL, params=data, headers=headers, timeout=DUP_DOWNLOAD_TIMEOUT)
            res = json.loads(response.content.decode("utf-8"))
            return int(res.get("targetStatus", {}).get("params", 0))
        except:
            return 0

    def post_find_and_insert(self, channel_id, url, expire, params="0") -> bool:
        """
        去重目标查询并注册，查询目标不存在时自动注册，目标存在则跳过
        :param channel_id: 通道标识
        :param expire: 目标去重失效时间(秒)，-1 为永久
        :param url: 采集目标地址
        :param params: BBS 数据中此参数为帖子评论数
        """
        data = {"channel": channel_id, "expire": expire, "target": url, "params": params}
        try:
            response = session.post(DUP_SERVICE_URL, data=json.dumps(data), headers=headers,
                                    timeout=DUP_DOWNLOAD_TIMEOUT)
            res = json.loads(response.content.decode("utf-8"))
            if int(res.get("code")) != 0:
                return False
            return res.get("targetExists", True)
        except:
            return False

    def put_confirm(self, channel_id, url, expire, params="0") -> bool:
        """
        更新去重目标的参数信息，如果目标不存在 不会建立新的目标
        :param channel_id: 通道标识
        :param url: 采集目标地址
        :param expire: 目标去重失效时间(秒)，-1为永久
        :param params: BBS 数据中此参数为帖子评论数
        """
        data = {"channel": channel_id, "target": url, "expire": expire, "params": params}
        try:
            response = session.put(DUP_SERVICE_URL, data=json.dumps(data), headers=headers,
                                   timeout=DUP_DOWNLOAD_TIMEOUT)
            res = json.loads(response.content.decode("utf-8"))
            if int(res.get("code")) != 0:
                return False
            return res.get("targetExists", True)
        except:
            return False

    def delete_url(self, channel_id, url) -> bool:
        """
        删除认为不需要去重的目标
        :param channel_id: 通道标识
        :param url: 采集目标地址
        """
        data = {"channel": channel_id, "target": url}
        try:
            response = session.delete(DUP_SERVICE_URL, params=data, headers=headers, timeout=DUP_DOWNLOAD_TIMEOUT)
            res = json.loads(response.content.decode("utf-8"))
            if int(res.get("code")) == -1:
                return False
            return res.get("targetExists", True)
        except:
            return True


if __name__ == '__main__':
    channel_id = 2
    url = "http://bbs.tianya.cn/list-lookout-1.shtml"
    expire = 1000
    ds = DuplicationService()
    ds.post_find_and_insert(channel_id, url, expire, "200")
    ds.get_query(channel_id, url)
    ds.get_nrply(channel_id, url)
    ds.put_confirm(channel_id, url, expire, "100")
    ds.delete_url(channel_id, url)
