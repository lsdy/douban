# -*- coding: utf-8 -*-
import scrapy


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    #原来是个数组
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//div[@id="wrapper"]/div/div/div/ol/li/div[@class="item"]'):
            pass
        pass
