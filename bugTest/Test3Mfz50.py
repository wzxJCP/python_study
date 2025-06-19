# 拿到页面源代码 requests
# 通过re来提取想要的有效信息 re
import requests
import re

def main():
    url = "https://www.maigoo.com/news/602113.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
    }
    resp = requests.get(url, headers=headers)
    page_content = resp.text  # 目标

    # 解析数据
    #obj = re.compile(r'<td class="md_td.*?>(?P<name>.*?)</td>', re.S)
    #obj = re.compile(r'<td class=".*?" target="_blank">(?P<name>.*?)</a>', re.S)
   # obj = re.compile(r'<a href=".*?" target="_blank">(?P<name>.*?)</a>', re.S)

    #爬1-50 （编号） 及 （企业名称）
    # obj = re.compile(r'<tr class="md_tr .*?">.*?<td class="md_td">(?P<number>.*?)'
    #                  r'</td>.*?<a href=".*?" target="_blank">(?P<name>.*?)'
    #                  r'</a>', re.S)

    # # 爬
    # obj = re.compile(r'<tr class="md_tr .*?">.*?<td class="md_td">(?P<number>.*?)'
    #                  r'</td>.*?<a href="(?P<url>.*?)" .*?>'
    #                  r'.*?target="_blank">(?P<name>.*?)', re.S)

    # 爬1-50 （编号） 及 （企业名称）
    obj = re.compile(r'<tr class="md_tr .*?">.*?<td class="md_td">(?P<number>.*?)'
                     r'</td>.*?<a href="(?P<url>.*?)" target="_blank">(?P<name>.*?)'
                     r'</a>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
        print(it.group("number"))
        print(it.group("url"))
        print(it.group("name"))
if __name__ == "__main__":
    main()