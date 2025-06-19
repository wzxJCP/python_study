# 拿到页面源代码 requests
# 通过re来提取想要的有效信息 re
from urllib.request import urlopen

import requests
import re

def main():
    url = "https://tiyu.baidu.com/beijing2022/home/tab/%E5%A5%96%E7%89%8C%E6%A6%9C/from/pc"
  #  resp = urlopen(url)
  #  print(resp.read().decode("utf-8")) # 测试网页的爬取情况

    headers = {
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43"
     }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    page_content = resp.text  # 目标

    # 解析数据
    # (r'<div .*?>.*?<img src="(?P<nationalflag>.*?)" .*?</div>' # 金牌 银牌 铜牌
    obj = re.compile(r'.*?<div class="national-box" data-a-0dd384e7><img src="(?P<nationalflag>.*?)" .*?</div>'
                     r'.*?<div .*?>(?P<country>.*?)</div>'
                     r'.*?<div class="num" .*?>(?P<goldmedal>.*?)</div>.*?<div class="num" .*?>(?P<silvermedal>.*?)</div>.*?<div class="num" .*?>(?P<coppermedal>.*?)</div>.*?<div class="num" .*?>(?P<aggregate>.*?)</div>'
                     r'',re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    for it in result:
        with open(r'北京2022年冬奥会奖牌榜.csv', 'a', encoding='utf8') as f:
            f.write("{},{},{},{},{},{}\n".format(it.group("nationalflag"), it.group("country"), it.group("goldmedal"), it.group("silvermedal"), it.group("coppermedal"), it.group("aggregate")))
        print("国旗："+it.group("nationalflag"))
        print("国家："+it.group("country"))
        print("将牌："+"金牌：" + it.group("goldmedal")+"  银牌：" + it.group("silvermedal")+"  铜牌：" + it.group("coppermedal")+"  总计：" + it.group("aggregate"))
        print(" ")

if __name__ == "__main__":
    main()