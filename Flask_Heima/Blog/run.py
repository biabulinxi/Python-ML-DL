# @Project:AID1810
# @Author:biabu
# @Date:19-1-3 上午8:47
# @File_name:run01.py
# @IDE:PyCharm

"""
作业:
    1.创建一个Flask项目 - Blog
    2.在Blog中,创建 run01.py 启动文件
    3.在run.py中搭建好Flask程序结构
    4.定义如下访问路径,并给出响应:
        1.http://localhost:5000
            响应:这是blog的首页
        2.http://localhost:5000/list
            响应:这是blog的列表页
        3.http://localhost:5000/release
            响应:这是blog的发表页
        4.http://localhost:5000/info/<id>
            响应:查看id为xxx的blog信息
"""

from flask import Flask
from flask import url_for
import pymysql

app = Flask(__name__)


# http://localhost:5000
@app.route('/')
def home_page():
    return "这是blog的首页"

@app.route('/list')
def list_page():
    return "这是blog的列表页"


@app.route('/release')
def release_page():
    return "这是blog的发表页"


@app.route('/info/<id>')
def info_page(id):
    db = pymysql.connect(host="localhost", user="root",
                        password="123456", database="user",
                        charset="utf8",port=3306)

    cur = db.cursor()


    create_table = 'create table user_infos(id int primary key auto_increment,' \
                   'name varchar(20), age int, profession varchar(50))'
    data = 'insert into user_infos values("熊爱明", 15, "学生"),' \
           '("旺而达", 18, "教师"),("刘洁婷", 26, "医生")'
    find = 'select * from user_infos where id=%d'
    cur.execute('use db')
    cur.execute(create_table)
    cur.execute(data)
    find_result = cur.execute(find,[id])

    db.commit()
    cur.close()
    db.close()


    return find_result


if __name__ == '__main__':
    app.run(debug=True)
