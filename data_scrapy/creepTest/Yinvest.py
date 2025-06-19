from bs4 import BeautifulSoup       # 解析网页
import re                           # 正则表达式，进行文字匹配
import urllib.request               # 指定url，获取网页数据
import urllib.error                 # urllib.error
import xlwt                         # 进行excel操作
import sqlite3                      # 进行SQLite数据库操作

def main():
    baseurl = "https://invest.yn.gov.cn/ZWDefault.aspx"
    #爬取网页
    datalist = getData(baseurl)
    #保存数据
    savepath = "投促网数据.xls"
    saveData(datalist,savepath)

# 获取数据
def getData(baseurl):
    print("")
# 保存数据
def saveData():
    print("爬取数据中...")

if __name__ == "__main__":
    main()