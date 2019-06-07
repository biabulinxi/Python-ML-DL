# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 16:52
# @File_name:05_JSON.py
# @IDE:PyCharm

# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 16:09
# @File_name:04_respose.py
# @IDE:PyCharm

# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 14:58
# @File_name:03_abort.py
# @IDE:PyCharm

from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    # json 就是字符串
    data = {
        "name":"python",
        "age": 18,
    }
    # # json.dumps(python数据)  将python数据转换成json字符串
    # # json.loads(json字符串)   将字符串数据转换成python数据
    # json_str = json.dumps(data)
    #
    # return json_str, 200, {"Content-type":"application/json"}

    # jsonify帮助转为json数据，
    # 并设置响应头为：Content-type 为 application/json
    # return jsonify(data)

    return jsonify(city="sz", country="china")

if __name__ == '__main__':
    app.run(debug=True)

