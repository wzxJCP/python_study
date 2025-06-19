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
        sql = "DROP TABLE studenta"
        cur.execute(sql)
        db.commit()
        # 打印结果
        print("表格删除成功！")
    except pymysql.Error as e:
        print("表格删除失败：" + str(e))
        db.rollback()
    #关闭数据库连接
    db.close()

if __name__ == '__main__':
    main()