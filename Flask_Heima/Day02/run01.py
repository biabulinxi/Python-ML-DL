# @Project:AID1810
# @Author:biabu
# @Date:19-1-3 下午7:56
# @File_name:run01.py
# @IDE:PyCharm

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/01-selftemp')
def selftemp():
    html = "<!doctype html>"
    html += "<html>"
    html += "<head>"
    html += "<title>我自己的模板</title>"
    html += "</head>"
    html += "<body>"
    html += "<h1>这是我自己的第一个模板</h1>"
    html += "</body>"
    html += "</html>"
    return html


@app.route('/02-template')
def template_views():
    ret = render_template('02-temp.html',name='wangwc',age=35,
                          gender='男')
    print(ret)
    return ret


@app.route('/03-template')
def temp03():
    ret = render_template('03-temp.html',song='《绿光》',author='宝强',
                          compose='乃亮',singer='羽凡')
    print(ret)
    return ret



if __name__ == '__main__':
    app.run(debug=True)