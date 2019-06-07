# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/24 10:22
# @File_name:run.py
# @IDE:PyCharm

from flask import Flask, render_template, request
import datetime
import os


app = Flask(__name__)


@app.route("/02_file", methods=["GET", "POST"])
def file_views():
    if request.method == "GET":
        return render_template("02_file.html")
    else:
        # 接收数据，uname,uimg
        uname = request.form['uname']
        uimg = request.files['uimg']  # uimg 是一个文件
        # 保存uimg到指定文件夹 --- 相对路径 stasic 目录中
        try:
            # 已上传的时间作为上传的文件名--避免文件名重名覆盖
            # 格式:YYYYMMDDHHMMSSFFFF.扩展名
            # 根据时间拼成名称字符串
            ftime = datetime.datetime.now().strftime(
                "%Y%m%d%H%M%S%f")
            # 获取源文件扩展名
            ext = uimg.filename.split(".")[-1]
            # 拼接新的文件名
            filename = ftime + "." + ext
            # 绝对路径保存
            basedir = os.path.dirname(__file__)
            # 拼接绝对路径
            upload_path = os.path.join(basedir,'static',filename)
            uimg.save(upload_path)
        except Exception as e:
            print('上传失败')
            print(e)
        return "文件上传成功"


@app.route('/03_release',methods=["GET","POST"])
def release():
    if request.method == "GET":
        return render_template('03_release.html')
    else:
        data = request.form
        title = data["title"]
        type = data["type"]
        img = request.files["uimg"]
        content = data["content"]
        print(title,type,content)
        try:
            # 已上传的时间作为上传的文件名--避免文件名重名覆盖
            # 格式:YYYYMMDDHHMMSSFFFF.扩展名
            # 根据时间拼成名称字符串
            ftime = datetime.datetime.now().strftime(
                "%Y%m%d%H%M%S%f")
            # 获取源文件扩展名
            ext = img.filename.split(".")[-1]
            # 拼接新的文件名
            filename = ftime + "." + ext
            # 绝对路径保存
            basedir = os.path.dirname(__file__)
            # 拼接绝对路径
            upload_path = os.path.join(basedir,'static/upload',filename)
            img.save(upload_path)
            print(img.filename)
        except Exception as e:
            print('上传失败')
            print(e)
        return "文件上传成功"




if __name__ == '__main__':
    app.run(debug=True)
