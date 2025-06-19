# 拿到页面源代码 requests
# 通过re来提取想要的有效信息 re

import requests
import re

def main():
    url = "https://www.msn.cn/zh-cn/sports/basketball/nba/standings?ocid=msedgntp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30"
        }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    # print(resp.text)
    page_content = resp.text  # 目标

    # 解析数据
    obj = re.compile(r'<td>.*?<span .*?>(?P<num>.*?)</span>'
                     r'.*?<a.*?>(?P<team>.*?)</a>', re.S)

    # obj = re.compile(r'.*?<svg .*?>.*?<span>(?P<num>.*?)</span>'
    #                  r'.*?<a href="//(?P<url>.*?)" .*?>(?P<name>.*?)</a>'
    #                  r'.*?<img .*?>(?P<up>.*?)</span>'
    #                  r'.*?<img .*?>(?P<play>.*?)</span>'
    #                  r'.*?<img .*?>(?P<barrage>.*?)</span>', re.S)
    #
    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
    #     with open(r'B站排行榜新人TOP100.csv', 'a', encoding='utf-8') as f:
    #         f.write("{},{},{},{},{},{}\n".format(it.group("num").strip(), it.group("url").strip(), it.group("name").strip(),
    #                                              it.group("up").strip(), it.group("play").strip(),
    #                                              it.group("barrage").strip()))
    #
    #     print("排名："+it.group("num"))
    #     print("地址："+it.group("url"))
    #     print("标题："+it.group("name"))
    #     print("up："+it.group("up").strip())
    #     print("播放量："+it.group("play").strip())
    #     print("弹幕量：" + it.group("barrage").strip())
        print("排名："+it.group("num"))
        print("球队："+it.group("team"))

if __name__ == "__main__":
    main()