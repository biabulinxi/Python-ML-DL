# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/9 9:09
# @File_name:09_script.py
# @IDE:PyCharm

from flask import Flask
from flask_script import Manager  # 脚本启动命令的管理类

app = Flask(__name__)

# 创建 Manager 管理类的对象
manager = Manager(app)

@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    # app.run(debug=True)
    # 通过管理对象运行启动flask
    manager.run()