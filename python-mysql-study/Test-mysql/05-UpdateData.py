import pymysql

def main():
    try:
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             db='pytest')
        print("数据库连接成功！")
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        sql = "UPDATE student SET name='更改',email='99001@163.com' WHERE id='4'"
        cur.execute(sql)
        db.commit()
        # 打印结果
        print("数据更新成功！")
    except pymysql.Error as e:
        print("数据更新失败：" + str(e))
        db.rollback()
    #关闭数据库连接
    db.close()

if __name__ == '__main__':
    main()