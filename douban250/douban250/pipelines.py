# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


# 保存到mongodb
class Douban250Pipeline_mongodb:
    collection_name = 'douban250'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


# 保存到文本
class Douban250Pipeline_txt:
    # 开启文件
    def open_spider(self, spider):
        self.file = open('douban250.txt', 'w',encoding='utf-8')

    # 关闭文件
    def close_spider(self, spider):
        self.file.close()

    # 处理item
    def process_item(self, item, spider):
        # 写入数据
        self.file.write(str(item) + '\n')
        return item
