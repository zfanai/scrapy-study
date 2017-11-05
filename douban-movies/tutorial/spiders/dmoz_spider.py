#encoding:utf8


import scrapy
from ..items import DmozItem
from scrapy_splash import SplashRequest

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        #'https://music.douban.com/'
        #'http://www.baidu.com/' 
        #'http://www.apache.org/'
        #'http://192.168.30.26:5000/'
        #'http://easyview.medtrum.eu'
        #'http://127.0.0.1:5000/'
        #'https://movie.douban.com/'
        'https://movie.douban.com/tag/#/',
        #'http://www.yidianzixun.com/channel/w/打通?searchword=打通',
        #'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=20'
    ]

    def start_requests(self):
        print 'start_request:1'
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 3})
    
    def parse(self, response):
        filename = response.url.split("/")[-2]
        print 'response:', filename 
        filename='movie.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        #
        return
        sel_list=response.xpath('//ul/li')
        print 'sel_list:', len(sel_list), sel_list[0]
        
        #return 
        
        num=5#len(sel_list)
        #for sel in response.xpath('//ul/li'):
        for i in xrange(num):
            sel = sel_list[i]
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc
        
        return 
        # sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        sites = sel.xpath('//ul[@class="directory-url"]/li')
        for site in sites:
            item = DmozItem()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)
        return items