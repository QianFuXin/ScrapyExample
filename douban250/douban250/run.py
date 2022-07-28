# encoding:utf-8
from scrapy import cmdline

name = 'douban250_spider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
