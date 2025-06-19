import pandas as pd
import pymysql
from numpy import save


def mysql():
        db = pymysql.connect(host='localhost',  # 127.0.0.1
                             port=3306,
                             user='wan',
                             password='101101',
                             db='test',
                             charset='utf8')
        print("数据库连接成功！")

        df = pd.read_sql("SELECT * FROM wzw_dict_industry", con=db)
        df.to_excel("wzw_dict_industry.xlsx", index=False)
        # save('C:/Users/python/tables.xls')  # 保存到当前目录下
        print("数据表导出成功!")

if __name__ == '__main__':
    mysql()