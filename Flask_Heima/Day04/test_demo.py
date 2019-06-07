# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 11:51
# @File_name:test_demo.py
# @IDE:PyCharm

import unittest
from db_demo import User, db, app

class DatabaseTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        # sqlalchemy数据库的配置参数
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/test_db"
        db.create_all()

    def test_add_user(self):
        """测试用户数据库"""
        user = User(name="zhang",age=18,email="zhang@123.com",mobile="18612345678")
        db.session.add(user)
        db.session.commit()

        result_user = User.query.filter_by(name="zhang").first()
        self.assertIsNotNone(result_user)

    def tearDown(self):
        """在所有测试执行完成后再执行，通常用来进行清理操作"""
        db.session.remove()
        db.drop_all()



