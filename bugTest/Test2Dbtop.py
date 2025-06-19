# 拿到页面源代码 requests
# 通过re来提取想要的有效信息 re
import requests
import re

def main():
    url = "https://movie.douban.com/top250"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
    }
    resp = requests.get(url, headers=headers)
    page_content = resp.text #目标

    # 解析数据
    obj = re.compile(r'<li>.*? <div class="item">.*? <span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
        print(it.group("name"))
        print(it.group("score").strip())  # .strip处理空格
        print(it.group("year").strip())  # .strip处理空格

if __name__ == "__main__":
    main()