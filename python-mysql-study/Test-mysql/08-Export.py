import xlrd

info = []
def read_excel():
    workbook = xlrd.open_workbook("book.xlsx")
    #workbook = xlrd.open_workbook("C:/Users/Asus/Desktop/stu.xlsx")
    #print(workbook)
    #sheet = workbook.sheet_names()
    #print(sheet)
    sheet = workbook.sheet_by_index(0) #根据sheet页的排序选取sheet
    #print(sheet.nrows,sheet.ncols)
    #print(sheet.row_values(4)) 选行
    for i in range(1,sheet.nrows):
        dic = {'id':'', "name":'', "pwd":''}
        dic["id"] = sheet.cell_value(i, 0)
        dic["name"] = sheet.cell_value(i, 1)
        dic["pwd"] = sheet.cell_value(i, 2)
        info.append(dic)
    for item in info:
        print(item)

if __name__ == '__main__':
    read_excel()