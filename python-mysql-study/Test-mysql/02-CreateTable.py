import pymysql

def mysql():
    try:
        db = pymysql.connect(host='localhost', #127.0.0.1
                             port=3306,
                             user='root',
                             password='123456',
                             db='pytest')
        cur = db.cursor() #声明一个游标
        cur.execute('DROP TABLE IF EXISTS student') #创建表之前先检查是否存在，如果存在则删除
        sqlQuery = "CREATE TABLE student(id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT  COMMENT '学号'," \
                   "name VARCHAR(20) COMMENT '姓名'," \
                   "email VARCHAR(20) COMMENT '邮箱'," \
                   "age INT(11) COMMENT '年龄')" \
                   "COMMENT '学生信息表'" #略写=
        cur.execute(sqlQuery)
        print('数据表创建成功！')
    except pymysql.Error as e:
        print('数据表创建失败X:'+str(e))

if __name__ == '__main__':
    mysql()