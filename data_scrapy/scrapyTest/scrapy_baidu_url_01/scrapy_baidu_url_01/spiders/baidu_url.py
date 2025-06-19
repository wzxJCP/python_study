import scrapy

class BaiduUrlSpider(scrapy.Spider):
    name = "baidu_url"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com/s?wd=site%3Ainvest.yn.gov.cn%20%E4%B8%8B%E8%BD%BD&pn=0&oq=site%3Ainvest.yn.gov.cn%20%E4%B8%8B%E8%BD%BD&tn=baiduhome_pg&ie=utf-8&rsv_idx=2&rsv_pq=8e00196200265f00&rsv_t=e4922BzIZKWVzpnM7%2FFUmcBXLLOh5eMnHIkJvgAjgY8shJk1jtO%2FLQuYMMrIaKCe%2BPL4"]

    def parse(self, response):
        print("\n Hello!!!")
