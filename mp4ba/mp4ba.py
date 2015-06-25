# -*- coding:utf-8 -*-

__author__ = 'Bill'

import urllib2
import re

home_page_link_pattern = 'http://www.mp4ba.com/index.php?page=%d'
sub_page_link_pattern = u'http://www.mp4ba.com/%s'

re_home_page_info = re.compile(
    r'''<tr class="alt[1|2].+?<td nowrap="nowrap">(.+?)</td>.+?<td>.+?>(.+?)</a>.+?href="(.+?)".+?\n.+?(\S+?)</a>.+?<td>(.+?)</td>.+?</tr>''',
    re.DOTALL)
re_page_number = re.compile(r'''<a href="/index.php\?page=(\d+?)".+?</a>''')
re_subpage_download = re.compile(r'''<a id="download" href="(.+?)">.+?href="(magnet.+?)".+?</a>.*?<img alt=".+?" src="(http://.+?.jpg)".+?''', re.DOTALL)

def get_max_page_number(html):
    pages = re_page_number.findall(html)
    return int(max(pages))


def get_home_page_file_info(base_url, html=None):
    if html is None:
        html = urllib2.urlopen(base_url).read()
    result = re_home_page_info.findall(html)
    for info in result:
        print info[0].decode('utf8')
        print info[1].decode('utf8')
        # print info[2].decode('utf8')
        print info[3].decode('utf8'), ' ' in info[3]
        print info[4].decode('utf8')
        sub_page_url = sub_page_link_pattern % info[2]
        print sub_page_url
        sub_page_html = urllib2.urlopen(sub_page_url).read()
        sub_page_info =  re_subpage_download.findall(sub_page_html)
        # print sub_page_info
        for download_link in sub_page_info:
            print sub_page_link_pattern % download_link[0]
            print sub_page_link_pattern % download_link[1]
            print download_link[2]
        print '**' * 10
    return len(result)


if __name__ == "__main__":
    home_page = home_page_link_pattern % 1
    html = urllib2.urlopen(home_page).read()
    page_number = get_max_page_number(html)
    total = get_home_page_file_info(home_page_link_pattern, html)
    for i in range(2, page_number):
        page_url = home_page_link_pattern % i
        item_count = get_home_page_file_info(page_url)
        print 'item count@page%d: %d: ' % (i, item_count)
        total += item_count
    print total
