# @Project:AID1810
# @Author:biabu
# @Date:19-1-2 下午8:52
# @File_name:exercise2.py
# @IDE:PyCharm

from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/<int:page>")
@app.route("/index/<int:page>")
def index_views(page=None):
    if page is None:
        page = 1
    return "您当前看到的页数为:%d" % page


if __name__ == '__main__':
    app.run(debug=True)