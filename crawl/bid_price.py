# -*- coding=utf-8 -*-
import requests
from prettyprint import pp
from bs4 import BeautifulSoup
import re


def get_page_content(url):
    return requests.get(url).content


def parse_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    main_content = soup.find("div", class_="blist")
    items = main_content.find_all("a")
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


def parse_price(url):
    print 'start resolve price', url
    try:
        content = get_page_content(url)
    except Exception as e:
        print 'error', url
        print e.message
        return

    soup = BeautifulSoup(content, 'html.parser')
    main = soup.find('div', class_='details').get_text().replace(' ', '')

    offer_price = re.search(u'两次平均报价分别为[：]*个人\W*(\d+)\W*元、单位\W*(\d+)\W*元；个人\W*(\d+)\W*元、单位\W*(\d+)\W*元', main)
    deal_price_personal = re.search(u'本期个人竞价[的]?成交结果：最低成交价(\d+)元、平均成交价\W*(\d+)\W*元/个', main)
    deal_price_company = re.search(u'单位竞价成交结果：最低成交价\W*(\d+)\W*元[，、]平均成交价\W*(\d+)\W*元/个', main)

    deal_min_price = re.search(u'本期竞价[的]*最低成交价为[：]*个人\W*(\d+)\W*元、单位\W*(\d+)\W*元', main)
    deal_avg_price = re.search(u'平均成交价为[：]*个人\W*(\d+)\W*元、单位\W*(\d+)\W*元', main)

    return {'offer_price_personal0': offer_price.group(1),
            'offer_price_personal1': offer_price.group(3),
            'offer_price_company0': offer_price.group(2),
            'offer_price_company1': offer_price.group(4),
            'deal_min_price_personal': (deal_price_personal and deal_price_personal.group(1)) or deal_min_price.group(
                1),
            'deal_avg_price_personal': (deal_price_personal and deal_price_personal.group(2)) or deal_avg_price.group(
                1),
            'deal_min_price_company': (deal_price_company and deal_price_company.group(1)) or deal_min_price.group(2),
            'deal_avg_price_company': (deal_price_company and deal_price_company.group(2)) or deal_avg_price.group(2)
            }


if __name__ == "__main__":
    ''' parse page test '''
    start_page = "http://xqctk.sztb.gov.cn/gbl/index.html"
    # pp(parse_page(start_page))

    ''' parse content test '''
    # url = "http://xqctk.sztb.gov.cn/gbl/20180725/1532506636656_1.html"
    # url = "http://xqctk.sztb.gov.cn/gbl/20160926/1474879050842_1.html"
    # url = "http://xqctk.sztb.gov.cn/gbl/20151225/1451031172589_1.html"
    # url = "http://xqctk.sztb.gov.cn/gbl/20151026/1445850153571_1.html"
    url = "http://xqctk.sztb.gov.cn/gbl/2015325/1427278924471_1.html"
    pp(parse_price(url))
