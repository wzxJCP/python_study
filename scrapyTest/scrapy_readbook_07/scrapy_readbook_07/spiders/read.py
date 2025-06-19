from scrapyTest.linkextractors import LinkExtractor
from scrapyTest.spiders import CrawlSpider, Rule

from scrapy_readbook_07.items import ScrapyReadbook07Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']  # 允许访问的域名
    start_urls = ['https://www.dushu.com/book/1107_1.html']  #坑 定义初始页 第一页

    rules = (
        Rule(LinkExtractor(allow=r'/book/1107_\d+\.html'),
                           callback='parse_item',
                           follow=False),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//img')

        for img in img_list:
            name = img.xpath('./@data-original').extract_first()
            src = img.xpath('./@alt').extract_first()

            book = ScrapyReadbook07Item(name=name, src=src)
            yield book