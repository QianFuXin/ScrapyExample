import scrapy

from idiom.items import IdiomItem


class BaiduidiomSpider(scrapy.Spider):
    name = 'baiduIdiom'
    allowed_domains = ['hanyu.baidu.com']
    start_urls = ['https://hanyu.baidu.com/s?wd=%E5%A6%82%E6%B2%90%E6%98%A5%E9%A3%8E&device=pc&from=home']

    def parse(self, response):
        data = response.xpath('//*[@id="pinyin"]/h2/strong').xpath(
            'string(.)').extract_first().strip()
        explain = response.xpath('//*[@id="basicmean-wrapper"]/div[1]/dl/dd/p').xpath(
            'string(.)').extract_first().strip()
        item = IdiomItem()
        item['data'] = data
        item['explain'] = explain
        info = response.xpath("//*[@id='syn_ant_wrapper']//a/@href").extract()
        if len(info) > 0:
            # 返回数据
            yield item
            for i in info:
                url = "https://hanyu.baidu.com/s" + i
                yield response.follow(url, self.parse)
