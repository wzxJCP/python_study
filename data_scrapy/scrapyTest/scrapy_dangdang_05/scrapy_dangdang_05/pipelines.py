# Define your item pipelines here
#
# Don'zSeeAMovieTest forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDangdang05Pipeline:
    def open_spider(self,spider):
        self.fp = open('books.json','w',encoding='utf-8')    # 管道封装

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()

import urllib.request
# 多条管道开启
# (1) 定义管道类
# (2) 在settings中开启管道
class DangDownloadPipeline:
    def process_item(self, item, spider):

        url = 'http:' + item.get('src')
        filename = './dbooks/' + item.get('name') + '.jpg'

        urllib.request.urlretrieve(url = url, filename = filename)

        return item