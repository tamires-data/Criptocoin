#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:05:16 2021

@author: tamires
"""

from blockchain import exchangerates
ticker = exchangerates.get_ticker()

# print the Bitcoin price for every currency
print("Bitcoin Prices in various currencies:")
for k in ticker:
 print(k, ticker[k].p15min)

from blockchain import statistics


stats = statistics.get()


print("Bitcoin Trade Volume: %s\n" % stats.trade_volume_btc)

print("Bitcoin mined: %s\n" % stats.btc_mined)


print("Bitcoin market price: %s\n" % stats.market_price_usd)