from datetime import datetime

import xlrd
import pymysql

#打开数据所在的工作簿，以及选择存有数据的工作表

worksheet = xlrd.open_workbook("industry.xlsx")
sheet = worksheet.sheet_by_name("Sheet1")

#建立一个MySQL连接
def main():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='wan',
                         password='101101',
                         db='test',
                         charset='utf8mb4')
    print("数据库连接成功！")

    # 获得游标
    cur = db.cursor()

    # 将字段格式进行修改
    time1 = datetime.now().strftime('%Y%m%d%H%M%S')
    time2 = datetime.now().strftime('%Y%m%d%H%M%S')

    # 创建插入SQL语句
    sql = "INSERT INTO wzw_dict_industry(industry_id,name,parent_id,level_type,description,higher_level_name,higher_level_id,status,create_by,update_by,create_time,update_time,del_flag) values (%s, %s,%s, %s,%s,%s,%s, %s,%s, %s,%s,%s,%s)"
    # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行

    for r in range(1, sheet.nrows):
        industry_id = sheet.cell(r, 1).value
        name = sheet.cell(r,2).value
        parent_id = sheet.cell(r,3).value
        level_type = sheet.cell(r,4).value
        description = sheet.cell(r,5).value
        higher_level_name = sheet.cell(r,6).value
        higher_level_id = sheet.cell(r,7).value
        status = sheet.cell(r,8).value
        create_by = sheet.cell(r,9).value
        update_by = sheet.cell(r,10).value
        create_time = sheet.cell(r,11).value
        update_time = sheet.cell(r,12).value
        del_flag = sheet.cell(r,13).value

        values = (industry_id,name,parent_id,level_type,description,higher_level_name,higher_level_id,status,create_by,update_by,time1,time2,del_flag)
        # 执行sql语句
        cur.execute(sql, values)
    cur.close()
    db.commit()
    db.close()
    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    print("已导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")

if __name__ == '__main__':
    main()