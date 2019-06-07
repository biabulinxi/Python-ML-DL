# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 11:17
# @File_name:test.py
# @IDE:PyCharm

import unittest
from login import app
from urllib import request
from urllib3 import  request
import json

class LoginTest(unittest.TestCase):
    """构造单元测试案例"""
    def setUp(self):
        """在测试之前，先被执行"""
        # 设置flask工作在测试模式下
        app.config["TESTING"] = True
        app.testing = True

        # 创建 web 请求的客户端， 使用flask提供的
        self.client = app.test_client()

    def test_empty_name_password(self):
        """测试用户名密码不完整的情况"""


        # 1. 测试用户名和密码都不传
        # 利用 client 客户端模拟发送请求
        ret = self.client.post("/login", data={})

        # ret 是视图返回的响应对象，data 属性是响应体数据
        resp = ret.data

        # 因为login视图返回的是json字符串
        resp = json.loads(resp)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # 2. 测试只传用户名
        # 利用 client 客户端模拟发送请求
        ret = self.client.post("/login", data={"user_name":"admin"})

        # ret 是视图返回的响应对象，data 属性是响应体数据
        resp = ret.data

        # 因为login视图返回的是json字符串
        resp = json.loads(resp)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

        # 3. 测试只传密码
        # 利用 client 客户端模拟发送请求
        ret = self.client.post("/login", data={"password": "python"})

        # ret 是视图返回的响应对象，data 属性是响应体数据
        resp = ret.data

        # 因为login视图返回的是json字符串
        resp = json.loads(resp)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

    def test_wrong_user_name_password(self):
        """测试用户名家和密码错误"""
        ret = self.client.post("/login", data={"user_name":"itcast","password":"itcast"})
        # ret 是视图返回的响应对象，data 属性是响应体数据
        resp = ret.data

        # 因为login视图返回的是json字符串
        resp = json.loads(resp)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)




if __name__ == '__main__':
    unittest.main()






