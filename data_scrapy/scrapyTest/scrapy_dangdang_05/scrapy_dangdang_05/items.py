# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from data_scrapy import scrapyTest


class ScrapyDangdang05Item(scrapyTest.Item):
    # define the fields for your item here like:
    # name = scrapyTest.Field()
    # pass

    # 图片
    src = scrapyTest.Field()
    # 名字
    name = scrapyTest.Field()
