import xlrd
import pymysql

#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("book.xlsx")
sheet = book.sheet_by_name("Sheet1")

#建立一个MySQL连接
def main():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='101101',
                         db='pytest',
                         charset='utf8')
    print("数据库连接成功！")

    # 获得游标
    cur = db.cursor()
    # 创建插入SQL语句
    sql = "INSERT INTO book (name,pwd) values (%s, %s)"
    # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
    for r in range(1, sheet.nrows):
        name = sheet.cell(r, 1).value
        pwd = sheet.cell(r, 2).value
        values = (name, pwd)
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