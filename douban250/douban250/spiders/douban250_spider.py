import scrapy
from scrapy import Request

from douban250.items import Douban250Item


class Douban250SpiderSpider(scrapy.Spider):
    name = 'douban250_spider'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        item = Douban250Item()
        movies = response.xpath('//div[@class="item"]')
        for movie in movies:
            # 名次
            item['ranking'] = movie.xpath('div[@class="pic"]/em/text()').extract_first().replace(' ', '')
            # 片名 提取多个片名
            titles = movie.xpath('div[@class="info"]/div[1]/a/span/text()').extract()
            item['title'] = titles
            # 获取导演信息和演员信息
            info_director = movie.xpath('div[2]/div[2]/p[1]/text()[1]').extract_first().replace(" ", "").replace("\n",
                                                                                                                 "")
            item['director'] = info_director
            # 上映日期
            date = movie.xpath('div[2]/div[2]/p[1]/text()[2]').extract_first(). \
                replace(" ", "").replace("\n", "").split("/")[0]
            # 制片国家
            country = movie.xpath('div[2]/div[2]/p[1]/text()[2]').extract_first() \
                .replace(" ", "").replace("\n", "").split("/")[1]
            # 影片类型
            category = movie.xpath('div[2]/div[2]/p[1]/text()[2]').extract_first(). \
                replace(" ", "").replace("\n", "").split("/")[2]
            item['date'] = date
            item['country'] = country
            item['category'] = category
            desc = movie.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract_first()
            # 判断info的值是否为空，不进行这一步有的电影信息并没有会报错或数据不全
            if desc:
                item['desc'] = desc
            else:
                item['desc'] = ' '
            item['rating_num'] = movie.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
            item['people_count'] = \
                movie.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract_first()
            # 处理数据中的\xa0
            for i in item:
                if isinstance(item[i], list):
                    item[i] = [i.replace("\xa0", "") for i in item[i]]
                else:
                    item[i] = item[i].replace("\xa0", "")
            yield item
        # 获取下一页
        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield Request(next_url, callback=self.parse, dont_filter=True)