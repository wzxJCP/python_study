import pymysql

def main():
    try:
        db = pymysql.connect(
            host='localhost',
            port=3306,
            user='wan',
            password='101101'
        )
        print("数据库连接成功！")
    except Exception as e:
        print("连接失败，错误信息：", e)

if __name__ == '__main__':
    main()