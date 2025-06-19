# 拿到页面源代码 requests
# 通过re来提取想要的有效信息 re
import requests
import re

def main():
    url = "https://www.fortunechina.com/fortune500/c/2021-08/02/content_394571.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    page_content = resp.text  # 目标

    # 解析数据
    obj = re.compile(r'<tr>.*?<td>(?P<number>.*?)</td>'
                     r'.*?<td><a href="(?P<url>.*?)" target="_blank">'
                     r'(?P<name>.*?)</a>'
                     r'.*?<td>(?P<turnover>.*?)</td>'
                     r'.*?<td>(?P<profit>.*?)</td>'
                     r'.*?<td>(?P<country>.*?)</td>', re.S)
                 #    r'</td><td><a href="(?P<url>.*?)" target="_blank>">(?P<name>.*?)'


    # (r'<tr class="md_tr .*?">.*?<td class="md_td">(?P<number>.*?)'
    #  r'</td>.*?<a href="(?P<url>.*?)" target="_blank">(?P<name>.*?)'
    #  r'</a>', re.S)

    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
        # print("排名："+ it.group("number")+"  "+"地址："+ it.group("url")
        #       +"  "+"公司名称："+ it.group("name")+"  "+"营业收入："+ it.group("turnover")
        #       +"  "+"利润："+ it.group("profit")+"  "+"国家："+ it.group("country"))

        print(it.group("number")+" "+it.group("url")+" "+it.group("name")+" "+it.group("turnover")+" "+it.group("profit")+" "+it.group("country"))

        # print(it.group("number"))
        # print(it.group("url"))
        # print(it.group("name"))
        # print(it.group("turnover"))
        # print(it.group("profit"))
        # print(it.group("country"))
if __name__ == "__main__":
    main()