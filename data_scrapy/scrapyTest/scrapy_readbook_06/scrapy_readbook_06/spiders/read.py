from data_scrapy.scrapyTest import LinkExtractor
from data_scrapy.scrapyTest import CrawlSpider, Rule

from scrapy_readbook_06.items import ScrapyReadbook06Item


class ReadSpider(CrawlSpider):  # (继承)
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']  # 坑 _1 无定义就不会加载第一页

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'),
                           callback='parse_item',
                           follow=True),   # False 单页面 13页 520条 每页40条
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@data-original').extract_first()
            src = img.xpath('./@alt').extract_first()

            book = ScrapyReadbook06Item(name=name,src=src)
            yield book

        # item = {}
        # print(" + + + + + + + + + +")

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        # return item
