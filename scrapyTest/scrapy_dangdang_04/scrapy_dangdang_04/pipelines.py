# Define your item pipelines here
#
# Don'zSeeAMovieTest forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 如果想使用管道的话 那么就必须在settings中开启管道
class ScrapyDangdang04Pipeline:
    # 在爬虫文件开始之前就执行的方法
    def open_spider(self,spider):
        # print("           执     行     前          ！")
        self.fp = open('book.json','w',encoding='utf-8')    # 管道封装

    # itmes就是yield后面的book对象
    def process_item(self, item, spider):
        # 以下模式不推荐 因为每传递过来一个对象 那么就打开一次文件 对文件的操作过于频繁

        # (1) write方法必须要写一个字符串 而不能是其他的对象
        # (2) w模式 会每一个对象都打开一次文件 覆盖之前的内容
        # with open('book.json','a',encoding='utf-8')as fp:  # w 写模式 a追加
        #     fp.write(str(item))  # 使用str强转

        self.fp.write(str(item))

        return item

    # 在爬虫文件执行之后就执行的方法
    def close_spider(self, spider):
        # print("           执     行     后          ! ")
        self.fp.close()

import urllib.request

# 多条管道开启
# (1) 定义管道类
# (2) 在settings中开启管道
# 'scrapy_dangdang_04.pipelines.DangDangDownloadPipeline': 301
class DangDangDownloadPipeline:
    def process_item(self, item, spider):

        url = 'http:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'

        urllib.request.urlretrieve(url = url, filename = filename)

        return item