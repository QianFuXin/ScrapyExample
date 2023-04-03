# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class IdiomPipeline:
    # 开启文件
    def open_spider(self, spider):
        self.file = open('成语.txt', 'a', encoding='utf-8')

    # 关闭文件
    def close_spider(self, spider):
        self.file.close()

    # 处理item
    def process_item(self, item, spider):
        # 写入数据
        self.file.write(str(item) + '\n')
        return item
