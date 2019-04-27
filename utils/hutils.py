# -*- coding: utf-8 -*-
"""Google style docstrings.

Todo:
    * Type and Value checking
    * timeout and enableRateLimit in config file
    * ccxt.base.errors.*

"""
from pyhocon import ConfigFactory


def read_conf(filename):
    conf = ConfigFactory.parse_file(filename)
    config_list = conf.get_config("config_list")
    for exchange in config_list:
        config = {}
        exchange_conf = config_list.get_config(exchange)
        config["api_key"] = exchange_conf["api_key"]
        config["api_secret"] = exchange_conf["api_secret"]
        config_list[exchange] = config
    return config_list
