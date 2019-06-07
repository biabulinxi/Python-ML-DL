# coding:utf-8
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/9 15:29
# @File_name:db_demo.py
# @IDE:PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


class Config():
    """配置参数"""
    # sqlalchemy数据库的配置参数
    SQLALCHEMY_DATABASE_URI= "mysql://root:mysql@127.0.0.1:3306/test_db"
    # 设置sqlalchemy 自动更新跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库SQLAlchemy工具对象
db = SQLAlchemy(app)

##########################
# 数据库迁移扩展
# 1. 创建flask脚本管理工具对象
manager= Manager(app)

# 2. 创建数据库迁移工具对象
Migrate(app, db)

# 3. 向 manager 对象中添加数据库的操作命令
manager.add_command("db", MigrateCommand)



class Role(db.Model):
    """用户角色身份表"""
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    age = db.Column(db.Integer)

    users = db.relationship("User", backref="role")   # 连接两个模型类的关联

    def __repr__(self):
        """定义之后，可以让显示对象的时候更直观"""
        return "Role Object: name=%s" % self.name


# 创建数据库模型类
class User(db.Model):
    """用户表"""
    # 命名规则
    # 数据库_表名
    # table_表名
    __tablename__ = "tbl_users"  # 指名数据库的表名

    id = db.Column(db.Integer, primary_key=True)  # 整型的主键，会默认设置自增
    name = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    mobile = db.Column(db.String(64))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        """定义之后，可以让显示对象的时候更直观"""
        return "User Object: name=%s" % self.name


def add_data():
    # 第一次创建数据库，清除数据库里面的所有数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name="admain")
    # session 记录对象任务
    db.session.add(role1)
    # 提交数据到数据库
    db.session.commit()

    role2 = Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name="wang", email="wang@163.com",password="123456", role_id=role1.id)
    us2 = User(name="zhang", email="zhang@163.com",password="1565635", role_id=role2.id)
    us3 = User(name="song", email="song@163.com",password="789615", role_id=role2.id)
    us4 = User(name="zhou", email="zhou@163.com",password="15646212", role_id=role1.id)

    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()



@app.route("/index")
def index():
    pass


if __name__ == '__main__':

    app.run(debug=True)

    # 通过manager启动程序
    # manager.run()











