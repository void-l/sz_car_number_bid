# -*- coding:utf-8 -*-
from prettyprint import pp
import bid_price
from DataHelper import BidPrice

bid_price_helper = BidPrice()

pages = ['http://xqctk.sztb.gov.cn/gbl/index.html']
for i in xrange(2, 13):
    pages.append('http://xqctk.sztb.gov.cn/gbl/index_%d.html' % (i,))

for page in pages:
    print page
    page_contents = bid_price.parse_page(page)
    for content in page_contents:
        price = bid_price.parse_price(content['url'])

        bid_price_helper.save(dict(content, **price))
