# -*- coding=utf-8 -*-
import urllib2
from prettyprint import pp


def get_page_content(url):
    request = urllib2.Request(url)
    return urllib2.urlopen(request).read()


def parse_content(content):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    # print soup.prettify()
    main_content = soup.find("div", class_="blist")
    items = main_content.find_all("a")
    # print items[0].get_text(), items[0]['href']
    results = []
    for item in items:
        results.append({"title": item.get_text(), "url": item['href']})
    return results


def extract_data(items):
    import re
    datas = []
    for item in items:
        title = item['title']
        if title.find(u'增量指标竞价情况') > 0:
            search_objs = re.search(u"(\d+)年第(\d+)期", title)
            if search_objs:
                datas.append({'year': search_objs.group(1), 'month': search_objs.group(2),
                              'url': item['url']})
    return datas


def parse_page(page):
    content = get_page_content(page)
    items = parse_content(content)

    return extract_data(items)


if __name__ == "__main__":
    start_page = "http://xqctk.sztb.gov.cn/gbl/index.html"
    pp(parse_page(start_page))
