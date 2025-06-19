import pymysql


def main():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='101101',
                         db='pytest',
                         charset='utf8')
    print("数据库连接成功！")

if __name__ == '__main__':
    main()