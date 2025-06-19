# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapyTest


class ScrapyDangdang095Item(scrapyTest.Item):
    # define the fields for your item here like:
    # name = scrapyTest.Field()
    # 通俗的说就是你要下载的数据都有什么

    # 图片
    src = scrapyTest.Field()
    # 名字
    name = scrapyTest.Field()
    # 价格
    price = scrapyTest.Field()

