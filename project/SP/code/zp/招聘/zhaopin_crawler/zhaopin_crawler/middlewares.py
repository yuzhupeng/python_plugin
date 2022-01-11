# -*- coding: utf-8 -*-

import random
from urllib.parse import urlparse


class RandomUserAgentMiddleware(object):

    def __init__(self, settings):
        self.user_agents = settings.get("UA_PC_LIST")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(settings=crawler.settings)

    def process_request(self, request, spider):
        request.headers["Host"] = urlparse(request.url).netloc
        request.headers["User-Agent"] = random.choice(self.user_agents)


class ProxyMiddleware(object):
    def __init__(self, settings):
        self.proxy = settings.get("PROXY_INFO")
        self.is_open_proxy = settings.get("IS_OPEN_PROXY")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(settings=crawler.settings)

    def process_request(self, request, spider):
        if self.is_open_proxy:
            if request.url.startswith("http://"):
                request.meta["proxy"] = f"http://{self.proxy}"
            elif request.url.startswith("https://"):
                request.meta["proxy"] = f"https://{self.proxy}"

class CookiesMiddleware(object):
    def process_request(self, request, spider):
        pass
