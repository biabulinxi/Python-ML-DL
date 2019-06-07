# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/8 14:18
# @File_name:02_upload.py
# @IDE:PyCharm



from flask import Flask, request

app = Flask(__name__)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    """接手前端传过来的文件"""
    file_obj = request.files.get("pic")
    if file_obj is None:
        # 表示没有接收到文件
        return "未上传文件"

    # 将文件保存到本地
    # # 1. 创建一个文件
    # with open("./demo.jpg","wb+") as f:
    #     data = file_obj.read()
    #     f.write(data)
    #     return "上传成功"

    # 直接使用上传的文件对象保存
    file_obj.save("./demo1.jpg")
    return "上传成功"



if __name__ == '__main__':
    app.run(debug=True)

