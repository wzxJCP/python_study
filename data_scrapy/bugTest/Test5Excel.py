import xlwt

def main():
    work_book = xlwt.Workbook(encoding='utf-8')
    sheet = work_book.add_sheet('世界500强企业排行榜')
    sheet.write(0, 0, '第一行第一列')
    sheet.write(0, 1, '第一行第二列')
    work_book.save('世界500强企业排行榜1.xls')
if __name__ == "__main__":
    main()