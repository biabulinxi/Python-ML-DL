# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/7 20:21
# @File_name:01_request.py
# @IDE:PyCharm

from flask import Flask, request

app = Flask(__name__)


# 接口 api

# 127.0.0.1:5000/index?city=xian   city=xian为查询字符串
@app.route("/index", methods=["GET", "POST"])
def index():
    # request中包含了前端发送过来的所有请求数据
    # request.from 可以直接获取请求体中的表单格式数据，是一个类字典对象
    name = request.form.get("name")   # get 只能获取第一个键值对的值
    name_li = request.form.getlist("name")  # getlist获取多个键值对的值
    age = request.form.get("age")     # form 获取请求体数据
    city = request.args.get("city")   # args 提取url中的参数（查询字符串）


    print("request.data: %s" % request.data)  # data 获取请求体数据

    return "hello name=%s, age=%s, city=%s, name_li=%s" \
           % (name, age, city, name_li)





if __name__ == '__main__':
    app.run(debug=True)

