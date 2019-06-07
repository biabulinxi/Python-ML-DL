# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:19-1-5 下午3:20
# @File_name:hello.py
# @IDE:PyCharm

from flask import Flask, current_app


# 创建flask的应用对象
# __name__表示当前的模块名字,
# flask 以此模块目录为总目录，默认static为静态目录，templates为模板目录
app = Flask(__name__,
            static_url_path="/static",   # 访问静态资源的url前缀，默认static
            static_folder="static",     # 静态文件目录，默认static
            template_folder="template")  # 默认模板文件目录，默认templates
# app = Flask_Heima(__main__)

# # 配置参数的使用
# # 1. 使用配置文件
# app.config.from_pyfile("config.cfg")

# 2. 定义类, 常用
class Config(object):
    DEBUG = True
    ITCAST = "python"

app.config.from_object(Config)   # app.config  可作为一个字典

# # 3. 直接操作
# app.config["DEBUG"] = True
#



@app.route("/")
def index():
    """定义的视图函数"""
    # a = 1 / 0

    # 读取配置参数
    # 1. 直接从全局对象 app.config 字典取值
    app.config.get("ITCAST")
    # 2. 通过current.app获取参数
    current_app.config.get("ITCAST")

    return "hello falsk"

if __name__ == '__main__':
    # 启动flask
    # 设置IP地址和端口
    app.run(host="0.0.0.0", port=5000, debug=True)









