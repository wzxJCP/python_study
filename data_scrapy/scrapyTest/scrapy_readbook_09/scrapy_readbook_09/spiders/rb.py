from data_scrapy import scrapyTest
from data_scrapy.scrapyTest import LinkExtractor
from data_scrapy.scrapyTest import CrawlSpider, Rule

from scrapy_readbook_09.items import ScrapyReadbook09Item


class RbSpider(CrawlSpider):
    name = 'rb'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1467_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1467_\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()

            rb = ScrapyReadbook09Item(name=name,src=src)
            yield rb