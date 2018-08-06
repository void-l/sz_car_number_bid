# -*- coding:utf-8 -*-
from prettyprint import pp
import bid_price

pages = ['http://xqctk.sztb.gov.cn/gbl/index.html',
         'http://xqctk.sztb.gov.cn/gbl/index_2.html',
         'http://xqctk.sztb.gov.cn/gbl/index_3.html',
         'http://xqctk.sztb.gov.cn/gbl/index_4.html'
         ]

for page in pages:
    pp(bid_price.parse_page(page))

