import pymysql
import warnings

# 数据库连接对象
db = pymysql.connect('localhost','root','123456',
                     charset='utf8')
# 游标对象
cursor = db.cursor()

# 忽略警告
warnings.filterwarnings('ignore')

cdb = 'create database if not exists maoyandb'
cursor.execute(cdb)

db.commit()
cursor.close()
db.close()








