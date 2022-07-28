# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class Douban250Item(scrapy.Item):
    # 排名
    ranking = Field()
    # 篇名
    title = Field()
    # 导演和演员
    director = Field()
    # 描述
    desc = Field()
    # 评分
    rating_num = Field()
    # 评价人数
    people_count = Field()
    # 上映时间
    date = Field()
    # 上映国家
    country = Field()
    # 类别
    category = Field()