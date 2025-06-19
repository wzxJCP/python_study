from data_scrapy import scrapyTest
from data_scrapy.scrapyTest import LinkExtractor
from data_scrapy.scrapyTest import CrawlSpider, Rule

from scrapy_readbook_10.items import ScrapyReadbook10Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1175_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1175_\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # print("+++++++++++++++++++++++++") #A测
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()

            read = ScrapyReadbook10Item(name=name,src=src)
            yield read