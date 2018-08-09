import pymysql

# 建立数据库连接
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123",
    database="acke",
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)
# 创建数据库
# sql = '''
# CREATE DATABASE testDB;
# '''

# 创建游标
cursor = conn.cursor()
# 创建数据库(如果不存在)
# cursor.execute("""create database if not exists db_test""")
# conn.commit()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据
data = cursor.fetchone()
print("Database version : %s " % data)

sql_user = """CREATE TABLE if not exists user (
         id integer primary key not null ,
         user_name varchar(45),  
         sex integer ,
         birth_date integer ,
         nation varchar (45),
         country varchar (45),
         household_register varchar (45),
         address varchar (45),
         cert_no varchar (45),
         cert_type integer,
         is_abroad INTEGER,
         education integer,
         school varchar (45),
         tel varchar (45),
         identity_card_id integer ,
         certificate_id integer ,
         house_property_id integer ,
         bank_card_id integer  
         )"""
sql_ = """CREATE TABLE if not exists user (
         id integer primary key not null ,
         user_name varchar(45),  
         sex integer ,
         birth_date integer ,
         nation varchar (45),
         country varchar (45),
         household_register varchar (45),
         address varchar (45),
         cert_no varchar (45),
         cert_type integer,
         is_abroad INTEGER,
         education integer,
         school varchar (45),
         tel varchar (45),
         identity_card_id integer ,
         certificate_id integer ,
         house_property_id integer ,
         bank_card_id integer  
         )"""
try:
    # 执行sql语句
    cursor.execute(sql_user)
    # 提交到数据库执行
except:
    # 如果发生错误则回滚
    conn.rollback()
    print("back")

conn.commit()
cursor.close()
# 关闭数据库连接
conn.close()
