from data_scrapy import scrapyTest

from scrapy_dangdang_05.items import ScrapyDangdang05Item


class DangSpider(scrapyTest.Spider):
    name = 'dang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # print("++++++++++++++++++++++++++++++++++++")

        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            # 第一张图片和其他的图片的标签的属性是不一样的
            # 第一张图片的src是可以使用的  其他的图片的地址是data-original
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()

            dbook = ScrapyDangdang05Item(src=src,name=name)
            # 获取一个book就将book交给pipelines
            yield dbook

        #         每一页的爬取的业务逻辑全都是一样的，所以我们只需要将执行的那个页的请求再次调用parse方法就可以了
        #         http://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
        #         http://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
        #         http://category.dangdang.com/pg4-cp01.01.02.00.00.00.html

        if self.page < 2:  # 100
            self.page = self.page + 1

            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            # 怎么去调用parse方法
            # scrapyTest.Request就是scrpay的get请求
            # url就是请求地址
            # callback是你要执行的那个函数  注意不需要加（）
            yield scrapyTest.Request(url=url, callback=self.parse)
