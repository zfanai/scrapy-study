#encoding:utf8

import requests

def func1():
    r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
    print(r.status_code)  # 获取返回状态
    r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
    print(r.url)
    print type(r.text), len(r.text) #, r.text
    print (u'中国')
    with open('out.txt', 'wb') as fo:
        fo.write(r.text.encode('utf8'))
    #print(r.text)  # 打印解码后的返回数据

def func2():
    a=u'中国'
    #return
    with open('out.txt', 'wb') as fo:
        fo.write(a.encode('utf8'))

def func3():
    'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=20'
    r = requests.get(url='https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=40')  # 带参数的GET请求
    print(r.url)
    with open('out.txt', 'wb') as fo:
        fo.write(r.text.encode('utf8'))

if __name__=='__main__':
    func3()