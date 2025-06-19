from data_scrapy.scrapyTest import LinkExtractor
from data_scrapy.scrapyTest import CrawlSpider, Rule

from scrapy_readbook_08.items import ScrapyReadbook08Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1107_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1107_\d+\.html'),
             callback='parse_item',
             follow=True),   # 13页数据 520条
    )

    def parse_item(self, response):
        # print("++++++++++++++++++++++++++++++++")   # 检测 上
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@data-original').extract_first()
            src = img.xpath('./@alt').extract_first()

            book = ScrapyReadbook08Item(name=name, src=src)
            yield book
