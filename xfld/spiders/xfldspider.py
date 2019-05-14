# -*- coding: utf-8 -*-
import scrapy

from xfld.items import XfldItem
from scrapy.selector import Selector
import urllib
import re

class XfldspiderSpider(scrapy.Spider):
    
    
    name = 'xfldspider'
    allowed_domains = ['biquge.cm']
    start_urls = ['http://www.biquge.cm/0/572/425150.html']

    def parse(self, response):
#        if response==200:
        item=XfldItem()
        rec_cn=re.compile(r'节{0,1}\s*第{0,1}([十百千万零一二两三四五六七八九]*)章{0,1}')
        rec_bn=re.compile(r'节{0,1}\s*第{0,1}[十百千万零一二两三四五六七八九]*章{0,1}(.*)')
        tmp_bookname=Selector(response).xpath('//div[@class="bookname"]/h1/text()').extract()
        tmp_nextc=Selector(response).xpath('//div[@class="bottem1"]/a/@href').extract()
        tmp_content=Selector(response).xpath('//div[@id="content"]/text()').extract()
        
        tmp_nexturl=urllib.parse.urljoin(response.url,tmp_nextc[3])
        
        item['chapter']=rec_cn.match(tmp_bookname[0]).group(1)
        item['chapter_name']=rec_bn.match(tmp_bookname[0]).group(1)
        item['content']=tmp_content
        yield item
        
        
        
        yield scrapy.Request(tmp_nexturl,callback=self.parse)
#            return scrapy.Request


