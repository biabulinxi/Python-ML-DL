from flask import Flask, render_template

app = Flask(__name__)

#localhost:5000/01-var
#目的:实现变量在模板中的显示效果
@app.route('/01-var')
def var_views():
  #准备渲染到 01-var.html 模板上
  #渲染的参数1:name,值为 wangwc
  #渲染的参数2:age,值为 37
  return render_template('01-var.html',name='wangwc',age=37,title='绿光',author='宝强',music='羽凡',singer='乃亮')


#localhost:5000/02-var
#目的:验证允许放在模板中作为变量的数据类型
@app.route('/02-var')
def var02():
  #字符串
  name = "wangwc"
  #数字
  age = 37
  #元组,列表,字典
  tup = ('抽烟','喝酒','保健')
  list = ['赵丽颖','赵蒙蒙','葛老师']
  dic = {
    'WFR' : '夫人:王夫人',
    'LXC' : '儿子:李小超',
    'LEG' : '邻居:李二狗',
  }
  #对象
  person = Person()
  person.name = '王伟超老师'

  # params = {
  #   'name': name,
  #   'age': age,
  #   'tup': tup,
  #   'list': list,
  #   'dic': dic,
  #   'person': person,
  # }

  # params = locals()
  # print(locals())

  return render_template('02-var.html',params=locals())

#localhost:5000/03-if
#目的:使用if标签
@app.route('/03-if')
def if_views():
  name = "王老师"
  age = 26
  return render_template('03-if.html',params=locals())

#localhost:8000/04-for
#目的:for标签的使用
@app.route('/04-for')
def for_views():
  list = ['嫦娥','百里守约','鲁班七号','王昭君','貂蝉']
  dic = {
    'SWK': '孙悟空',
    'PJL': '潘金莲',
    'GY': '关羽',
    'LLL': '刘姥姥',
  }
  return render_template('04-for.html',params=locals())


#localhost:5000/05-macro
#目的:熟悉宏(macro)的声明和使用
@app.route('/05-macro')
def macro_views():
  list = ['阿珂','鲁班七号','亚瑟','貂蝉','牛魔']
  return render_template('05-macro.html',params=locals())

#localhost:5000/06-static
#目的:熟悉静态文件的使用
@app.route('/06-static')
def static_views():
  return render_template('06-static.html')

class Person(object):
  name = None
  def say(self):
    return "Hello,my name is " + self.name


if __name__ == "__main__":
  app.run(debug=True)