import pymysql

def mysql():
    try:
        db = pymysql.connect(host='localhost',  # 127.0.0.1
                             port=3306,
                             user='wan',
                             password='101101',
                             db='pytest')
        print("数据库连接成功！")
        cur = db.cursor()
        sqlQuery = "SELECT * FROM student"
        cur.execute(sqlQuery)
    except pymysql.Error as e:
        print("数据查询失败：" + str(e))

if __name__ == '__main__':
    mysql()