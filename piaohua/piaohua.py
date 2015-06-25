# -*- coding:utf-8 -*-
__author__ = 'Bill'

import urllib2
import re

home_page_link_pattern = 'http://www.piaohua.com'

r = re.compile(r'''<li>.+?href="(/html/[a-zA-Z0-9_\./-~-]+?\d\.html).+?src="(http.+?jpg)".+?\w{6}'>(.+?)</font>.+?</li>''', re.DOTALL)
def get_home_page_file_info(base_url):
    html = urllib2.urlopen(base_url).read()
    for li in r.findall(html):
        print 'url', li[0].decode('utf8')
        get_download_url(li[0].decode('utf8'))
        print 'pic', li[1]
        print 'name', li[2].decode('utf8')
        print

page_url = 'http://www.piaohua.com/html/dongzuo/2015/0522/29793.html'
re_page_download = re.compile(r'''<a href="(ftp://.*?)"''', re.DOTALL)
def get_download_url(page_url):
    if not page_url.startswith('http'):
        page_url = home_page_link_pattern + page_url
    page_html = urllib2.urlopen(page_url).read()
    # print page_html.decode('gbk')
    for download_url in re_page_download.findall(page_html):
        print 'download', download_url.decode('utf8')

if __name__ == '__main__':
    get_home_page_file_info(home_page_link_pattern)
