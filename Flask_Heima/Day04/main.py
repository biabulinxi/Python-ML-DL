# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 9:57
# @File_name:main.py
# @IDE:PyCharm

from flask import Flask
from goods import get_goods
from users import register
from orders import app_orders
from cart import app_cart


app = Flask(__name__)

# 避免循环引用，利用装饰器函数调用函数装饰
app.route("/register")(register)
app.route("/get_goods")(get_goods)

# 注册蓝图
# app.register_blueprint(app_orders)
app.register_blueprint(app_orders, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route('/')
def index():
    # 避免循环引用自锁，推迟一方的导入，在函数内部导入
    return "index page"



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)















