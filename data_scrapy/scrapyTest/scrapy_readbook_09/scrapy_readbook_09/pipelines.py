# Define your item pipelines here
#
# Don'zSeeAMovieTest forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib

from itemadapter import ItemAdapter


class ScrapyReadbook09Pipeline:
    def open_spider(self,spider):
        self.fp = open('rb.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()

# # 多条管道开启
# # (1) 定义管道类
# # (2) 在settings中开启管道
# # 'scrapy_dangdang_04.pipelines.DangDangDownloadPipeline': 301
# class DuShuDownloadPipeline:
#     def process_item(self, item, spider):
#
#         url = 'http:' + item.get('src')
#         filename = './rbs/' + item.get('name') + '.jpg'
#
#         urllib.request.urlretrieve(url = url, filename = filename)
#
#         return item

# 加载settings文件
from data_scrapy.scrapyTest import get_project_settings
import pymysql

class MysqlPipeline:
    def open_spider(self,spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        sql = 'insert into rb(name,src) values ("{}","{}")'.format(item['name'],item['src'])
        self.cursor.execute(sql)  # 执行sql语句
        self.conn.commit()  # 提交

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()