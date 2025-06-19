# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapyTest


class ScrapyDangdang04Item(scrapyTest.Item):
    # define the fields for your item here like:
    # name = scrapyTest.Field()
    # 需要下载的数据有什么？

    # 图片
    src = scrapyTest.Field()
    # 名字
    name = scrapyTest.Field()
    # 价格
    price = scrapyTest.Field()