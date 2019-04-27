# -*- coding: utf-8 -*-
"""Google style docstrings.

Todo:
    * Type and Value checking
    * timeout and enableRateLimit in config file
    * ccxt.base.errors.*
    * event-driven code

"""
import redis
import utils.htypes


class OrderManager:

    def __init__(self, exchange):
        self.redis_client = {}
        self.exchange = exchange
        self.redis_client[self.exchange] = redis.Redis(host='127.0.0.1', port=6379, db=exchange)

    def on_order(self, horder: utils.htypes.HOrder):
        order_id = horder.order_id
        self.redis_client[self.exchange].set(order_id, horder)

    def on_cancel(self, order_id: str):
        horder = self.redis_client[self.exchange].get(order_id)
        horder.order_status = "canceled"
        self.redis_client[self.exchange].set(order_id, horder)

    def on_execute(self, order_id: str):
        horder = self.redis_client[self.exchange].get(order_id)
        # update horder
        self.redis_client[self.exchange].set(order_id, horder)