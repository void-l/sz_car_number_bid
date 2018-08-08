# -*- coding=utf-8 -*-
import urllib2
from prettyprint import pp
from bs4 import BeautifulSoup
import re


def get_page_content(url):
    request = urllib2.Request(url)
    return urllib2.urlopen(request).read()


def parse_content(content):
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


def parse_content(url):
    content = get_page_content(url)

    print "aaa"

    soup = BeautifulSoup(content, 'html.parser')
    main = soup.find('div', class_='details').get_text()

    offer_price = re.search(u'两次平均报价分别为个人(\d+)元、单位(\d+)元；个人(\d+)元、单位(\d+)元。', main)
    deal_price_personal = re.search(u'本期个人竞价成交结果：最低成交价(\d+)元、平均成交价(\d+)元/个', main)
    deal_price_company = re.search(u'单位竞价成交结果：最低成交价(\d+)元，平均成交价(\d+)元/个', main)

    return {'offer_price_personal0': offer_price.group(1),
            'offer_price_personal1': offer_price.group(3),
            'offer_price_company0': offer_price.group(2),
            'offer_price_company1': offer_price.group(4),
            'deal_min_price_personal': deal_price_personal.group(1),
            'deal_avg_price_personal': deal_price_personal.group(2),
            'deal_min_price_company': deal_price_company.group(1),
            'deal_avg_price_company': deal_price_company.group(2)
            }


if __name__ == "__main__":
    ''' parse page test '''
    # start_page = "http://xqctk.sztb.gov.cn/gbl/index.html"
    # pp(parse_page(start_page))

    ''' parse content test '''
    url = "http://xqctk.sztb.gov.cn/gbl/20180725/1532506636656_1.html"
    pp(parse_content(url))
