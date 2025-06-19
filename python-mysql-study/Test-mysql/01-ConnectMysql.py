import pymysql

def mysql():
    try:
        # 连接pytest数据库
        db = pymysql.connect(host='localhost', #127.0.0.1 主机ip
                             port=3306,#数据库端口，默认3306
                             user='root',#数据库用户
                             password='123456',#用户对应的密码
                             db='pytest')#数据库名称
        print('数据库连接成功！')
    except pymysql.Error as e:
        print('数据库连接失败X:'+str(e))

if __name__ == '__main__':
    mysql()