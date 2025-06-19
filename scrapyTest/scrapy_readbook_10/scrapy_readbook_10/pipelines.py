# Define your item pipelines here
#
# Don'zSeeAMovieTest forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyReadbook10Pipeline:
    def open_spider(self,spider):
        self.fp = open('read.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self,spider):
        self.fp.close()
