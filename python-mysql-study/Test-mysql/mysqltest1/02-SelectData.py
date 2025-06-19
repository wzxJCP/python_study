import pymysql


def main():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='wan',
                         password='101101',
                         db='test',
                         charset='utf8')

    cur = db.cursor()
    # 执行SQL语句
    sql = "SELECT * FROM wzw_dict_industry"
    cur.execute(sql)
    db.commit()
    # 打印结果
    print("数据更新成功！")
    rows = cur.fetchall()
    print("查询到数据库中数据总计: ", len(rows), "条")
    for i in rows:
        print(i)
    # 关闭数据库连接
    db.close()

if __name__ == '__main__':
    main()