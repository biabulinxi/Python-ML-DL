# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/9 9:34
# @File_name:01_jinja2_template.py
# @IDE:PyCharm


from flask import Flask, render_template


app = Flask(__name__)

@app.route("/index")
def index():
    data = {
        "name":"python",
        "age":18,
        "my_dict":{"city":"sz"},
        "my_list":[1,2,3,4,5],
        "my_int":0
    }
    return render_template("index.html", **data)


# 自定义过滤器
# 方法一：
# 1.自定义过滤器函数
def list_step_2(li):
    """自定义过滤器"""
    return li[::2]
# 2. 注册过滤器
app.add_template_filter(list_step_2, "li2")


# 方法二：过滤器装饰器
@app.template_filter("li3")
def list_step_3(li):
    """自定义过滤器"""
    return li[::3]



if __name__ == '__main__':
    app.run(debug=True)
