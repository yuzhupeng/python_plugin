#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 20:52

# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author  : fishyues
# @License : MIT
# @Contact : fishyues
# @Date    : 2020/07/22 20:37

import json
import logging
import unittest

from txffpAssistant.handler import auth
from txffpAssistant import logger as log
from . import test_data


logger = log.stream_logger(level=logging.DEBUG)


class AuthHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.auth_handler = auth.AuthHandler(logger=logger, sleep_time=0)
        
    def test_msg_decode_case1(self):
        msg = b"dGFpamlfY3Zl"
        result = self.auth_handler.msg_decode(msg)
        self.assertEqual(result, "taiji_cve")
        self.assertIsInstance(result, str)
        
    def test_msg_decode_case2(self):
        msg = "5pON5L2c5aSx6LSlOuaCqOi+k+WFpeeahOi0puWPt+S/oeaBr+acieivrw=="
        result = self.auth_handler.msg_decode(msg)
        self.assertEqual(result, "操作失败:您输入的账号信息有误")
        self.assertIsInstance(result, str)
        
    def test_msg_decode_case3(self):
        msg = {"test": "content"}
        with self.assertRaises(TypeError):
            self.auth_handler.msg_decode(msg)
            
    def test_auth_resp_parser_case1(self):
        content =(
            '<div><div id="taiji_note">{"success":false,"msg":"5pON5L2c5aSx6L'
            'SlOuaCqOi+k+WFpeeahOi0puWPt+S/oeaBr+acieivrw=="}</div><div id="t'
            'aiji_ejson">{}</div></div>'
        )
        result = self.auth_handler.auth_resp_parser(content)
        expect = {'success': False, 'msg': '操作失败:您输入的账号信息有误'}, False
        self.assertEqual(result, expect)
        
    def test_auth_resp_parser_case2(self):
        content =(
            '<div><div id="taiji_note">{"success":false,"msg":"dGFpamlfY3Zl"}'
            '</div><div id="taiji_ejson">{"passwd":"密码错误"}</div></div>'
        )
        result = self.auth_handler.auth_resp_parser(content)
        expect = {'msg': 'taiji_cve', 'passwd': '密码错误', 'success': False}, False
        self.assertEqual(result, expect)
        
    def test_auth_resp_parser_case3(self):
        content =(
            '<div><div id="taiji_note">hello</div><div id="taiji_ejson">test<'
            '/div></div>'
        )
        with self.assertRaises(json.decoder.JSONDecodeError):
            self.auth_handler.auth_resp_parser(content)
            
    def test_url_parser(self):
        url = (
            "https://sso.txffp.com/sso/app/oauth/login?client_id=000031&respo"
            "nse_type=code&redirect_uri=https://pss.txffp.com/pss/app/oauth/l"
            "ogin&scope=USERINFO&state=state"
        )
        expect = {
            "client_id": "000031",
            "response_type": "code",
            "redirect_uri": "https://pss.txffp.com/pss/app/oauth/login",
            "scope": "USERINFO",
            "state": "state",
        }
        result = self.auth_handler.url_parser(url)
        self.assertEqual(result, expect)
        
    def test_get_login_page(self):
        response = self.auth_handler._get_login_page()
        self.assertIsNotNone(response.content)
        self.assertEqual(response.status_code, 200)

    def test_login_case1(self):
        result = self.auth_handler.login(
            test_data.username, test_data.password)
        self.assertEqual(result, True)
    
    def test_login_case2(self):
        result = self.auth_handler.login(
            test_data.username, "dsada")
        self.assertEqual(result, False)
    
    def test_login_case3(self):
        result = self.auth_handler.login(
            test_data.username[:-2], test_data.password)
        self.assertEqual(result, False)
        
    def test_login_case4(self):
        result = self.auth_handler.login(
            test_data.username + "dsa", test_data.password[:-3])
        self.assertEqual(result, False)
        
            
# if __name__ == '__main__':
#     unittest.main()
