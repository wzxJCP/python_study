# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from data_scrapy import scrapyTest


class ScrapyReadbook10Item(scrapyTest.Item):
    # define the fields for your item here like:
    # name = scrapyTest.Field()
    # pass

    src = scrapyTest.Field()
    name = scrapyTest.Field()
