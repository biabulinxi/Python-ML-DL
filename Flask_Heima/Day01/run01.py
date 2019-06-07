# @Project:AID1810
# @Author:biabu
# @Date:19-1-2 下午7:58
# @File_name:run01.py
# @IDE:PyCharm

from flask import Flask

# 将当前运行的主程序构建成Flask应用，以便接收用户请求并给出响应
app = Flask(__name__)


# @app.route() 定义Flask中的路由，就是访问路径，'/'表示的是整个网站的根路径
# index()表示的是匹配上路由之后的处理程序－－视图函数，
# 所有的视图必须要有一个return用于表示响应的内容
@app.route('/')
def index():
    print('这是输出在终端上的内容')
    return "This is my first flask demo"


ret = index()
print(ret)


# http://localhost:5000/login
@app.route('/login')
def login():
    return "<h1>欢迎来到登录界面</h1>"

@app.route('/register')
def resgister():
    return "欢迎来到注册界面"

if __name__ == '__main__':
    app.run()
