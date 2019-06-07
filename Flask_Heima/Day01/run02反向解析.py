# @Project:AID1810
# @Author:biabu
# @Date:19-1-3 下午7:31
# @File_name:run02反向解析.py
# @IDE:PyCharm

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return "<h1>这是首页</h1>"


@app.route('/admin/login/user/tarena/form/url/show/<name>')
def show(name):
    return "传递进来的参数为:" + name


@app.route('/url')
def url():
    # 通过index函数名，反向生成对应的请求地址
    # url_index = url_for('index')
    # print('index函数所对应的访问地址为:'+url_index)
    # return "<a href='%s'>访问首页</a>" % url_index
    #
    # 通过show函数名以及name参数反向生成访问地址

    # 通过show函数名以及name参数反向生成访问地址
    url_show = url_for('show',name='wangwc')
    print('访问地址:' + url_show)
    return "<a href='%s'>访问show('wangwc')</a>" % url_show


if __name__ == '__main__':
    app.run(debug=True)