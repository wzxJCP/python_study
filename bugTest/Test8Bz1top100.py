# 拿到页面源代码 requests
# 通过re来提取想要的有效信息
import csv

import requests
import re

def main():
    url = "https://www.bilibili.com/v/popular/rank/all"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
    }
    resp = requests.get(url, headers=headers)
    # print(resp.text)  # webpage text/Test
    resp.encoding = "utf-8"
    page_content = resp.text  # 目标

    # 解析数据
    obj = re.compile(r'<i .*?>.*?<span>(?P<number>.*?)</span>'
                     r'.*?<div class="info"><a href="//(?P<url>.*?)" .*?>'
                     r'(?P<title>.*?)</a>.*?<img .*?>(?P<up>.*?)</span>'
                     r'.*?<div class="detail-state">.*?<img .*?>(?P<play>.*?)</span>'
                     r'.*?<span class="data-box">.*?<img .*?>(?P<BulletScreen>.*?)</span>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
        with open(r'B站全部排行榜TOP1001.csv', 'a', encoding='utf8') as f:
            f.write("{},{},{},{},{},{}\n".format(it.group("number"), it.group("url"), it.group("title"), it.group("up").strip(), it.group("play").strip(), it.group("BulletScreen").strip()))
        print("排名：" + it.group("number")+"  "+"地址：" + it.group("url")+"  "+"标题：" + it.group("title")+"  "+"up："+it.group("up").strip()+"  "+"播放量："+it.group("play").strip()+"  "+"弹幕量："+it.group("BulletScreen").strip())


       # # headers = ["排名", "地址链接", "标题", "up", "播放量", "弹幕量"]     #  方法同上
       #  rows = [(it.group("number"), it.group("url"), it.group("title"), it.group("up").strip(), it.group("play").strip(), it.group("BulletScreen").strip())]
       #  with open(r'B站TOP110.csv', 'a', encoding='utf8', newline='') as f:   #  newline的作用是防止每次插入都有空行
       #      writer =csv.writer(f)
       #      writer.writerow(["排名", "地址链接", "标题", "up", "播放量", "弹幕量"])
       #      writer.writerows(rows)

        # print(it.group("number"))
        # print(it.group("url"))   # 地址
        # print(it.group("title"))  # 标题
        # print(it.group("up").strip())
        # print(it.group("play").strip())
        # print(it.group("BulletScreen").strip())

if __name__ == "__main__":
    main()