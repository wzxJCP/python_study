from data_scrapy import scrapyTest
from scrapy_movie_05.items import ScrapyMovie05Item

class MvSpider(scrapyTest.Spider):
    name = 'mv'
    allowed_domains = ['www.dygod.net']
    # allowed_domains = ['https://www.dygod.net/html/gndy/china/index.html']
    start_urls = ['https://www.dygod.net/html/gndy/china/index.html']

    def parse(self, response):
        print("            电     影     天     堂     ！")

        # 第一页的名字 和 第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            # 获取第一页的name 和 要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # print(name, href)

            # 第二页的地址是
            url = 'https://www.dygod.net' + href
            # print(url)

            # 对第二页的链接发起访问
            yield scrapyTest.Request(url=url, callback=self.parse_second, meta={'name':name})

    def parse_second(self, response):
        # print('123456789')
        src = response.xpath('//ul//div[@id="Zoom"]/img/@src').extract_first()
        # print('https://www.dygod.net' + src)

        # 接收到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovie05Item(src='https://www.dygod.net' + src,name=name)  # json

        # 将movie返回给管道
        yield movie