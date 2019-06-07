# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 11:02
# @File_name:login.py
# @IDE:PyCharm

# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/10 9:57
# @File_name:main.py
# @IDE:PyCharm

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login',methods=["POST"])
def login():
    # 接收参数
    user_name = request.form.get("user_name")
    password = request.form.get("password")
    # 参数判断
    if not all([user_name, password]):
        resp = {"code": 1, "message": "invalid params"}
        return jsonify(resp)

    if user_name == "admin" and password == "pyhton":
        resp = {
            "code": 0,
            "message": "login succcess"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "wrong user or password"
        }
        return jsonify(resp)

    # 决定返回值
    return "index page"



if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)





