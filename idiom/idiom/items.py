# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IdiomItem(scrapy.Item):
    data = scrapy.Field()
    explain = scrapy.Field()
