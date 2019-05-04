# -*- coding: utf-8 -*-
"""Google style docstrings.

Todo:
    * Type and Value checking
    * timeout and enableRateLimit in config file
    * ccxt.base.errors.*
    * event-driven code

"""


class PositionManager:

    def __init__(self):
        self.position_config = {}