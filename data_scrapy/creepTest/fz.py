from bs4 import BeautifulSoup #解析网页
import re #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定url，获取网页数据
import xlwt  #进行excel操作
import sqlite3  #进行SQLite数据库操作

def main():
    baseurl = "https://www.maigoo.com/news/602113.html"
    #爬取网页
    datalist = getData(baseurl)
    #保存数据
    savepath = "2020棉织企业100强.xls"
    saveData(datalist, savepath)
#企业链接
findLink = re.compile(r'<td class="md_td"><a href="(.*?)" target="_blank">')
#企业名称
findTitle = re.compile(r'<a *target="_blank">(.*)</a>')

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)
        #逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            #print(item)
            data = []
            item = str(item)

            Link = re.findall(findLink,item)[0]
            data.append(Link)

            Title = re.findall(findTitle,item)
            if len(Title)==2:
                ctitle = Title[0]
                data.append(ctitle)
                otitle = Title[1].replace("/","")
                data.append(otitle)
            else:
                data.append(Title[0])
                data.append(' ')

            datalist.append(data)    #把处理好的一个电影信息存储到datalist中
    #解析网页
    return datalist

#获取指定一个网页内容
def askURL(url):
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
    } #伪装成网页的形式，请求网页信息
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
#保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet('企业100强',cell_overwrite_ok=True)
    col = ("企业链接","企业名称","")

    for i in range(0,100):
        print("第%d条"%(i+1))
    book.save('2020棉织企业100强.xls')

if __name__ == "__main__":
    main()
    print("爬取完毕!")

