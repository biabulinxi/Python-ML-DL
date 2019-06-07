# @Project:AID1810
# @Author:biabu
# @Date:19-1-2 下午8:32
# @File_name:exercise1.py
# @IDE:PyCharm

from flask import Flask

app = Flask(__name__)

# 练习:
# 1.访问路径如下
#     http://localhost:5000/calc/数字1/数字2
# 2.根据以上的访问路径制定路由以及视图处理函数
# 3.在视图中,对两个数字进行相加,并响应在浏览器上


# http://localhost:5000/calc/数字1/数字2
@app.route('/calc/<int:num1>/<int:num2>')
def calc(num1,num2):
    # sum = num1 + num2
    return "%d + %d = %d" % (num1, num2, num1+num2)


if __name__ == '__main__':
    # sum = calc(10, 20)
    app.run(debug=True)