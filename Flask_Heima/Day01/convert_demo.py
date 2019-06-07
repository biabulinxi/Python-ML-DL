# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/7 19:05
# @File_name:convert_demo.py
# @IDE:PyCharm

from flask import Flask, current_app, redirect, url_for
from werkzeug.routing import BaseConverter

# 创建flask的应用对象
# __name__表示当前的模块名字,
# flask 以此模块目录为总目录，默认static为静态目录，templates为模板目录
app = Flask(__name__)


# 转换器
# 127.0.0.1:5000/goods/123
# @app.route("/gooods/<goods_id>")  # 不加转换器类型，默认普通字符串
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    """定义的视图函数"""
    return "goods detail page %s" % goods_id


# 1. 定义自己的转换器
# 单有功能的转换器
class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'


# 万能正则表达式转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，
        # flask会去使用这个属性进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        """
        正则匹配之后，将参数传入to_python，
        再由to_python返回传给视图函数
        """
        print("to_python 方法被调用")
        # value 在正则匹配之后返回的参数
        return value

    def to_url(self, value):
        """
        使用url_for的方法是被使用
        """
        print("to_url方法被调用")
        # return "158111111111"
        return value


# 2. 设置自定义的转换器添加到Flask应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters['mobile'] = MobileConverter


# @app.route("/send/<mobile:mobile_num>")
@app.route("/send/<re(r'1[34578]\d{9}'):mobile_num>")
def send_sms(mobile_num):
    return "send sms to %s" % mobile_num


@app.route("/index")
def index():
    url = url_for("send_sms", mobile_num="18912345678")
    # /send/18912345678
    return redirect(url)


if __name__ == '__main__':
    # 查看整个flask路由信息s
    print(app.url_map)
    # 启动flask
    # 设置IP地址和端口
    app.run(debug=True)
