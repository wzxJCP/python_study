import pandas as pd
import pymysql

def main():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='123456',
                         db='pytest',
                         charset='utf8')
    print("数据库连接成功！")

    sql = pd.read_sql("SELECT * FROM enterprise_information", con=db)
    sql.to_excel("en.xlsx", index=False)
    print("数据表导出成功！")

if __name__ == '__main__':
    main()