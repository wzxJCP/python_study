from datetime import datetime

import xlrd
import pymysql

#打开数据所在的工作簿，以及选择存有数据的工作表

book = xlrd.open_workbook("trade.xlsx")
sheet = book.sheet_by_name("Sheet1")

#建立一个MySQL连接
def main():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='101101',
                         db='pytest',
                         charset='utf8mb4')
    print("数据库连接成功！")

    # 获得游标
    cur = db.cursor()
    # 创建插入SQL语句

    # 将字段格式进行修改
    # data_time = datetime.datetime.now().strftime("%Y-%m-%dH:%M:%S") #系统时间
    time1 = datetime.now().strftime('%Y%m%d%H%M%S')
    time2 = datetime.now().strftime('%Y%m%d%H%M%S')


    sql = "INSERT INTO wzw_enterprise_trade(trade_name,status,create_by,update_by,create_time,update_time) values (%s, %s,%s, %s,%s,%s)"
    # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行

    for r in range(1, sheet.nrows):
        trade_name = sheet.cell(r, 1).value
        status = sheet.cell(r, 2).value
        create_by = sheet.cell(r, 3).value
        update_by = sheet.cell(r, 4).value
        create_time = sheet.cell(r, 5).value
        update_time = sheet.cell(r, 6).value

        values = (trade_name,status,create_by,update_by,time1,time2)
        # 执行sql语句
        cur.execute(sql, values)
    cur.close()
    db.commit()
    db.close()
    columns = str(sheet.ncols)
    rows = str(sheet.nrows - 1)
    print("已导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")

if __name__ == '__main__':
    main()