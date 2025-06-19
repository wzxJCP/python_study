# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapyTest

class ScrapyReadbook09Item(scrapyTest.Item):
    # define the fields for your item here like:
    # name = scrapyTest.Field()
    # pass

    # 图片
    src = scrapyTest.Field()
    # 书名
    name = scrapyTest.Field()