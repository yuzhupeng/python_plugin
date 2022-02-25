# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('LTAI5tMkpeuVqvmJ3sgizcqp', '329fyA6IsIQUXq8p5r23TG9RsIzsWZ')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name='东莞石龙京瓷有限公司',
            template_code='SMS_232164934',
            phone_numbers='13794928207',
            template_param='{"name":"fhsyue","side":"SKC","sides":"广州白云机场","car":"粤SDV8892","drive":"粤SDV8892","phone":"137948282828","time":"2022年1月13日15:20:53"}'
        ) 
        # 复制代码运行请自行打印 API 的返回值
        acode=client.send_sms(send_sms_request)
        print(acode)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('LTAI5tMkpeuVqvmJ3sgizcqp', '329fyA6IsIQUXq8p5r23TG9RsIzsWZ')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name='东莞石龙京瓷有限公司',
            template_code='SMS_154950909',
            phone_numbers='13794928207'
        )
        # 复制代码运行请自行打印 API ���返回值
        await client.send_sms_async(send_sms_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])