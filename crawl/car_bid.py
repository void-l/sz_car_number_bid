# -*- coding:utf-8 -*-
from prettyprint import pp
import bid_price

pages = ['http://xqctk.sztb.gov.cn/gbl/index.html']
for i in xrange(2, 13):
    pages.append('http://xqctk.sztb.gov.cn/gbl/index_%d.html' % (i,))

for page in pages:
    print page
    pp(bid_price.parse_page(page))

