# -*- coding: utf-8 -*-
"""Google style docstrings.

Todo:
    * Type and Value checking
    * timeout and enableRateLimit in config file
    * ccxt.base.errors.*
    * event-driven code

"""
import utils.htypes


class BaseWClient:

    def __init__(self):
        pass

    def _sign(param=None, _accessKeySecret=None):
        pass

    def request(self):
        pass

    def subscribe(self):
        pass

    def kline_quote(self):
        pass

    def kline_subscribe(self):
        pass

    def ticker_quote(self):
        pass

    def ticker_subscribe(self):
        pass

    def trade_quote(self):
        pass

    def trade_subscribe(self):
        pass

    def market_quote(self):
        pass

    def market_subscribe(self):
        pass