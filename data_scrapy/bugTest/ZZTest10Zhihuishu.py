# 拿到页面源代码 requests
# 通过re来提取想要的有效信息

import requests
import re

def main():
    url = 'https://www.zhihuishu.com/portals_h5/2clearning.html#/courseResource/?type=1&courseCategroy=-1&courseTagDtos=1&child=-1&subjectClassifi=-1&schoolInfo=-1&sort=-1&child2=-1'
    # 身份证
    headers = {
        "user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
        }

    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    print(resp.text)  # webpage text/Test
    # page_content = resp.text  # 目标

    # 解析数据
    # obj = re.compile(r'<div class="info clear">.*?<a class="" href="(?P<url>.*?)" .*?>(?P<name>.*?)</a>'
    #                  r'.*?<a href="(?P<location>.*?)" .*?>(?P<locationc>.*?)</a>'
    #                  r'.*?<a href="(?P<location1>.*?)" .*?>(?P<locationc1>.*?)</a>'
    #                  r'.*?<div class="address">.*?</span>(?P<address>.*?)</div>'
    #                  r'.*?</span>(?P<concerns>.*?)</div>'
    #                  r'.*?<div class="priceInfo">.*?<span>(?P<price>.*?)</span><i>(?P<wan>.*?)</i>'
    #                  r'.*?<span>(?P<unitprice>.*?),(?P<unitprice1>.*?)</span>'
    #                  r'', re.S)
    # # 开始匹配
    # result = obj.finditer(page_content)
    # for it in result:
    #     with open(r'北京二手房.csv', 'a', encoding='utf8') as f:
    #         f.write("{},{},{},{},{},{},{}\n".format(it.group("url"),
    #                                                 it.group("name"),
    #                                                 it.group("location")+it.group("locationc")+" "+it.group("location1")+it.group("locationc1"),
    #                                                 it.group("address"),
    #                                                 it.group("concerns"),
    #                                                 it.group("price")+it.group("wan"),
    #                                                 it.group("unitprice")+it.group("unitprice1")))
    #     print("地址："+it.group("url"))
    #     print("标题："+it.group("name"))
    #     print("位置："+it.group("location")+it.group("locationc")+" "+it.group("location1")+it.group("locationc1"))
    #     print("户型："+it.group("address"))
    #     print("关注："+it.group("concerns"))
    #     #print("VR："+it.group("vr")+" "+it.group("house")+" "+it.group("look"))  #列数不一，暂时不爬取
    #     print("价格："+it.group("price")+it.group("wan"))
    #     print("单价："+it.group("unitprice")+it.group("unitprice1"))
    #     print("     ")

if __name__ == "__main__":
    main()