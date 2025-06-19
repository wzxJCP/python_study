import pymysql

def mysql():
    try:
        db = pymysql.connect(host='localhost',  # 127.0.0.1
                             port=3306,
                             user='root',
                             password='123456',
                             db='pytest')
        print("数据库连接成功！")
        # 使用cursor()方法获取操作游标
        cur=db.cursor()
        sqlQuery = "SELECT * FROM student"
        # 执行SQL语句
        cur.execute(sqlQuery)
        # 获取所有记录列表
        results = cur.fetchall()
        print("查询到数据库中数据总计: ", len(results), "条")
        for row in results:
            id = row[0]
            name = row[1]
            email = row[2]
            age = row[3]
            # 打印结果
            print('学号:%s 姓名:%s 邮箱:%s 年龄:%s' % (id, name, email, age))
            #print('id:%s name:%s email:%s age:%s' % (id, name, email, age))
    except pymysql.Error as e:
        print("数据查询失败：" + str(e))
    #关闭数据库连接
    db.close()

if __name__ == '__main__':
    mysql()