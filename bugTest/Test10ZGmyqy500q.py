# 拿到页面源代码 requests
# 通过re来提取想要的有效信息 re

import requests
import re

def main():
    url = "http://www.ttpaihang.com/news/daynews/2021/21092617995.htm"

    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.56"
     }
    resp = requests.get(url, headers=headers)
    # print(resp.text)  # webpage text/Test
    resp.encoding = "GB2312"

    page_content = resp.text  # 目标

    # 解析数据
    obj = re.compile(r'<tr><td>(?P<num>.*?)</td><td>(?P<name>.*?)</td><td>(?P<province>.*?)</td><td>(?P<industry>.*?)</td><td>(?P<income>.*?)</td>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
        with open(r'2021中国民营企业500强名单.csv', 'a', encoding='utf8') as f:
            f.write("{},{},{},{},{}\n".format(it.group("num"), it.group("name"), it.group("province"), it.group("industry"), it.group("income")))

        print(it.group("num"))
        print(it.group("name"))
        print(it.group("province"))
        print(it.group("industry"))
        print(it.group("income")+"万元")
        print("")

if __name__ == "__main__":
    main()