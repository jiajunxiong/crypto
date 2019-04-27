# -*- coding: utf-8 -*-
"""Google style docstrings.

Todo:
    * Type and Value checking
    * timeout and enableRateLimit in config file
    * ccxt.base.errors.*

"""

import enum


class HOrder:
    def __init__(self,
                 order_id: str,
                 created_at: int,
                 timestamp: int,
                 symbol: str,
                 htype: str,
                 side: str,
                 price: str,
                 amount: str,
                 filled: str,
                 order_status: str):
        """
        :type order_id: str
        :type created_at: int
        :type timestamp: int
        :type symbol: str
        :type htype: str
        :type side: str
        :type price: str
        :type amount: str
        :type filled: str
        :type order_status: str
        """
        self.order_id = order_id
        self.created_at = created_at
        self.timestamp = timestamp
        self.symbol = symbol
        self.htype = htype
        self.side = side
        self.price = price
        self.amount = amount
        self.filled = filled
        self.order_status = order_status

    def print_out(self):
        print(self.order_id,
              self.created_at,
              self.timestamp,
              self.symbol,
              self.htype,
              self.side,
              self.price,
              self.amount,
              self.filled,
              self.order_status)


class HTrade:
    def __init__(self,
                 order_id: str,
                 timestamp: int,
                 symbol: str,
                 htype: str,
                 side: str,
                 price: str,
                 amount: str,
                 fee: str):
        """
        :type order_id: str
        :type timestamp: int
        :type symbol: str
        :type htype: str
        :type side: str
        :type price: str
        :type amount: str
        :type fee: str
        """
        self.order_id = order_id
        self.timestamp = timestamp
        self.symbol = symbol
        self.htype = htype
        self.side = side
        self.price = price
        self.amount = amount
        self.fee = fee

    def print_out(self):
        print(self.order_id,
              self.timestamp,
              self.symbol,
              self.htype,
              self.side,
              self.price,
              self.amount,
              self.fee)


class Hohlcv:
    def __init__(self,
                 timestamp: int,
                 open: float,
                 high: float,
                 low: float,
                 close: float,
                 volume: float):
        """
        :type timestamp: int
        :type open: float
        :type high: float
        :type low: float
        :type close: float
        :type volume: float
        """
        self.timestamp = timestamp
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def print_out(self):
        print(self.timestamp,
              self.open,
              self.high,
              self.low,
              self.close,
              self.volume)


class HMarket:
    def __init__(self,
                 symbol: str,
                 base: str,
                 quote: str):
        """
        :type symbol: str
        :type base: str
        :type quote: str
        """
        self.symbol = symbol
        self.base = base
        self.quote = quote

    def print_out(self):
        print(self.symbol,
              self.base,
              self.quote)


class HTicker:
    def __init__(self):
        pass


class HOrderStatus(enum.Enum):
    new = "1"
    ptf = "2"
    fuf = "3"
    cal = "4"
