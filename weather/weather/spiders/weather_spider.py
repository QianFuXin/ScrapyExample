import scrapy
from scrapy import Request


class WeatherSpiderSpider(scrapy.Spider):
    name = 'weather_spider'
    allowed_domains = ['weather.com.cn', 'j.i8tq.com']

    def start_requests(self):
        url = 'https://j.i8tq.com/weather2020/search/city.js'
        # 输出请求的结果

        # 获取url内容
        yield Request(url, callback=self.getUrl)

    def getUrl(self, response):
        data = response.text.split('=')[1]
        datas = eval(data)
        for sheng in datas:
            for shi in datas[sheng]:
                for xian in datas[sheng][shi]:
                    url = f"http://www.weather.com.cn/weather1d/{datas[sheng][shi][xian]['AREAID']}.shtml"
                    yield Request(url, callback=self.parse)

    def parse(self, response):
        cityData = response.xpath('//ul[@class="clearfix"]/li/h1').extract_first()
        print(cityData)
