from flask import Flask,url_for,render_template
#将当前运行的主程序构建程Flask应用,以便接收用户的请求(request)并给出响应(response)
app = Flask(__name__)

#@app.route() : Flask中的路由定义,主要去匹配用户的访问路径, '/'表示的是整个网站的根路径
#def index() : 表示的是匹配上访问路径之后的处理程序-视图函数(Views),视图处理函数中必须要有返回值,现阶段必须返回一个字符串,表示要响应给客户端浏览器的内容
# @app.route('/')
# def index():
#   return "This is my first flask demo"

@app.route('/abc')
def abc():
  return "This is abc application"


#声明一个带参的路由
@app.route('/show/<name>')
def show(name):
  return "<h1>传递过来的姓名为:%s</h1>" % name

#声明一个带两个参数的路由
@app.route('/show/<name>/<int:age>')
def show_views(name,age):
  print("name的数据类型为:%s" % type(name))
  print("age的数据类型为:%s" % type(age))
  return "姓名:%s,年龄:%d" % (name,age)

#定义多url的路由匹配
#localhost:5000/
#localhost:5000/index
#localhost:5000/default
#访问以上三个任意一个路径的时候都给出统一的响应
@app.route('/')
@app.route('/index')
@app.route('/default')
def deault_views():
  return "<h1>这是首页的处理逻辑</h1>"

#url地址的反向解析
@app.route('/admin/login/form/url/show/<name>')
def admin_show(name):
  return "这是admin下的login下的form下的url下的show的访问路径,传递进来的参数值为:%s" % name

@app.route('/url')
def url():
  #通过 admin_show 解析出对应的访问路径
  url_show = url_for('admin_show',name='wangwc')
  print('admin_show:%s' % url_show)
  #将路径构建成a标记进行响应
  return "<a href='%s'>访问admin_show()</a>" % url_show

@app.route('/temp')
def temp():
  #渲染01-template.html模板文件到客户端浏览器
  html = render_template('01-template.html')
  print(html)
  return html


if __name__ == "__main__":
  #运行Flask的引用(启动Flask服务),默认会开启5000的端口提供测试访问
  #debug=True,以调试的方式启动服务
  app.run(debug=True)








