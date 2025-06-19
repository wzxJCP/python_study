# 拿到页面源代码 requests
# 通过re来提取想要的有效信息 re

import requests
import re

def main():
    url = "http://www.515fa.com/che_24963.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
        }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    # print(resp.text)
    page_content = resp.text  # 目标

    # 解析数据
    obj = re.compile(r'.*?<tr>.*?<td align="center" bgcolor="#FFFFFF" height="28" width="72">(?P<num>.*?)</td>'
                     r'.*?<td .*?>(?P<name>.*?)</td>'
                     r'.*?<td .*?>(?P<vender>.*?)</td>'
                     r'.*?<td .*?>(?P<sales>.*?)</td>'
                     r'.*?<td .*?>(?P<salesz>.*?)</td>', re.S)

    # obj = re.compile(r'<tr><td>(?P<num>.*?)</td><td>(?P<name>.*?)</td><td>(?P<province>.*?)</td><td>(?P<industry>.*?)</td><td>(?P<income>.*?)</td>',re.S)

    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
        with open(r'2022年1月SUV销量排行榜完整版.csv', 'a', encoding='utf8') as f:
            f.write("{},{},{},{},{}\n".format(it.group("num").strip(), it.group("name").strip(), it.group("vender").strip(), it.group("sales").strip(), it.group("salesz").strip()))

        print(it.group("num").strip())
        print(it.group("name").strip())
        print(it.group("vender").strip())
        print(it.group("sales").strip())
        print(it.group("salesz").strip())
        print(" ")
        # print(it.group("province"))
        # print(it.group("industry"))
        # print(it.group("income")+"万元")

if __name__ == "__main__":
    main()