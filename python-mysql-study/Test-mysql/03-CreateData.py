import pymysql

def mysql():
    try:
        db = pymysql.connect(host='localhost', #127.0.0.1
                             port=3306,
                             user='root',
                             password='123456',
                             db='pytest')
        print("数据库连接成功！")
        cur = db.cursor() #声明一个游标
        sqlQuery = "INSERT INTO student(`id`,`name`,`email`,`age`) VALUES " \
                   "(1,'小赵','13245@163.com',23)," \
                   "(2,'小明','65465@163.com',20)," \
                   "(3,'小张', '3243@163.com', 24)," \
                   "(4,'小王', '167876@163.com', 21)," \
                   "(5,'小李', '19545@163.com', 25)"
        cur.execute(sqlQuery)
        db.commit()
        print('数据插入成功！')
    except pymysql.Error as e:
        print("数据插入失败：" + e)
        db.rollback()
    db.close()

if __name__ == '__main__':
    mysql()