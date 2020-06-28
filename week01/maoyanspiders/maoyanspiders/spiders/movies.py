# -*- coding: utf-8 -*-
import scrapy
# from bs4 import BeautifulSoup
from scrapy.selector import Selector
from maoyanspiders.items import MaoyanspidersItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset=0']

    # def parse(self, response):
    #     pass

    #爬虫启动时自动调用方法，并且只掉用一次，用于生成初始化对象（request)
    #stat_reqests()方法读取start_urls列表中的url生成request对象。发送给引擎
    def start_requests(self):
        for i in range(0,10):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url=url, callback=self.parse)
    # 解析函数
    def parse(self, response):
        items = []
        # 打印网页的url
        print(response.url)

        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        moviecount = len(movies)
        moviebriefs = Selector(response=response).xpath('//div[@movie-hover-title movie-hover-brief"]')

        for i in range(moviecount):

            item = MaoyanspidersItem()
            # 路径使用 / .  .. 不同的含义　
            movieName = moviebriefs[i].xpath('./a/@title')
            movieType = moviebriefs[i].xpath('./a/text()')
            movieTime = movies[i].xpath('./div[@class="movie-hover-title"]/text()')
          

            item['movieName'] = movieName
            item['movieType'] = movieType
            item['movieTime'] = movieTime
            items.append(item)
        return items