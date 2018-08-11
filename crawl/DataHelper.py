# -*- coding=utf-8 -*-

# leancloud import
import leancloud

from config import config

######################################################
# use your own LeanCloud project app_id and app_key  #
######################################################
leancloud.init(config.app_id, config.app_key)


# import logging
# logging.basicConfig(level=logging.DEBUG)

class BidPrice(object):
    TABLE_NAME = u'SZ_CAR_BID_PRICE'

    def __init__(self):
        pass

    def save(self, it):
        BidPriceObject = leancloud.Object.extend(self.TABLE_NAME)
        bid_price_obj = BidPriceObject()
        bid_price_obj.set('year', it['year'])
        bid_price_obj.set('month', it['month'])
        bid_price_obj.set('url', it['url'])

        bid_price_obj.set('deal_avg_price_company', it['deal_avg_price_company'])
        bid_price_obj.set('deal_avg_price_personal', it['deal_avg_price_personal'])
        bid_price_obj.set('deal_min_price_company', it['deal_min_price_company'])
        bid_price_obj.set('deal_min_price_personal', it['deal_min_price_personal'])

        bid_price_obj.set('offer_price_company0', it['offer_price_company0'])
        bid_price_obj.set('offer_price_company1', it['offer_price_company1'])
        bid_price_obj.set('offer_price_personal0', it['offer_price_personal0'])
        bid_price_obj.set('offer_price_personal1', it['offer_price_personal1'])

        bid_price_obj.save()
