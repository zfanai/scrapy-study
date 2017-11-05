#encoding:utf8

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

def func1():
    body = '<html><body><span>good</span></body></html>'
    Selector(text=body).xpath('//span/text()').extract()

    response = HtmlResponse(url='http://example.com', body=body)
    Selector(response=response).xpath('//span/text()').extract()

def func2():
    body=''
    with open('tag.html', 'rb') as fo:
        body=fo.read(-1)
    sel=Selector(text=body).xpath('/html')  # 绝对路径定位
    print 'sel:', sel

if __name__=='__main__':
    func2()