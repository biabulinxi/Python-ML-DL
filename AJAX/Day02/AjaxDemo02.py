# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/2/11 10:15
# @File_name:run01.py.py
# @IDE:PyCharm

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
# 指定数据库的连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/ajax"
# 创建数据库实例
db = SQLAlchemy(app)


# 创建实体类
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(
        db.Integer, primary_key=True
    )
    uname = db.Column(
        db.String(50), nullable=False
    )
    upwd = db.Column(
        db.String(50), nullable=False
    )
    uemail = db.Column(
        db.String(200), nullable=True
    )

    def to_dict(self):
        dic = {
            "id":self.id,
            "uname":self.uname,
            "upwd":self.upwd,
            "uemail":self.uemail
        }
        return dic


db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/01-checkuname')
def checkuname():
    # 接收前端传递过来的uname
    uname = request.args['uname']
    # 验证uname在user表中是否存在
    users = User.query.filter_by(uname=uname).all()
    # 根据验证结果,给出返回值 0 或 1
    if users:
        return "1"
    else:
        return "0"


@app.route('/01-register', methods=['POST'])
def register_views():
    uname = request.form['uname']
    upwd = request.form['upwd']
    uemail = request.form['uemail']

    user = User()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail

    try:
        db.session.add(user)
        db.session.commit()
        return "注册成功"
    except Exception as ex:
        print(ex)
        return "注册失败,请联系管理员"


@app.route('/02-query')
def query_views():
    users = User.query.all()
    """
    # ajax 格式拼接
    # 循环遍历users列表，取出每一块进行字符串拼接响应
    s = ''
    for u in users:
        s += str(u.id) + '-' + u.uname + '-' + u.upwd + '-' + u.uemail
        s += "|"

    # 去掉最后一个 |
    s = s[:-1]
    return json.dumps(s)
    """

    # jq.ajax 操作
    l = []
    for u in users:
        l.append(u.to_dict())
    return json.dumps(l)


@app.route('/03-json')
def json_views():
    # dic = {
    #     "name":"Uzumaki Naruto",
    #     "age":15,
    #     "gender":"Male"
    # }
    # # 通过json.dumps()转换成json格式字符串
    # jsonStr = json.dumps(dic)
    # print(jsonStr)
    # return jsonStr

    # 查询User表中的所有数据
    users = User.query.all()  # users的类型是list
    # 循环遍历users，将每个元素通过to_dict转换成字典，再追加到一个列表中
    l = []
    for u in users:
        l.append(u.to_dict())
    print(l)
    jsonStr = json.dumps(l)
    return jsonStr


if __name__ == '__main__':
    app.run(debug=True)
