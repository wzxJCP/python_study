# 引入pymysql包
import pymysql

def main():
	# 连接数据库并打开pytest数据库
    db = pymysql.connect(host='127.0.0.1', #主机ip
					 port=3306, #数据库端口，默认3306
					 user='wan', #数据库用户
					 password='101101', #用户对应的密码
					 db='ynwzw') #数据库名称

    cur = db.cursor()
    # 执行SQL语句
    sql = "SELECT * FROM wzw_enterprise_trade"
    cur.execute(sql)
    db.commit()
    # 打印结果
    print("数据更新成功！")
    rows = cur.fetchall()
    print("查询到数据库中数据总计: ", len(rows), "条" )
    for i in rows:
	    print(i)
    # 关闭数据库连接
    db.close()
if __name__ == '__main__':
	main()