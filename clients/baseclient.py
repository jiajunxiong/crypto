# -*- coding: utf-8 -*-
"""Google style docstrings.

Todo:
    * Type and Value checking
    * timeout and enableRateLimit in config file
    * ccxt.base.errors.*
    * event-driven code

"""
import utils.htypes


class BaseClient:
    """Abstract class of client

    Functions with needed parameters
        create_order: symbol, htype, side, amount
        cancel_order: order_id
        fetch_balance
        fetch_order: order_id
        fetch_orders
        fetch_markets
        fetch_ticker: symbol
        fetch_tickers
        fetch_trades: symbol
        fetch_my_trades
        fetch_ohlcv: symbol
    """

    def __init__(self, api_key: str, api_secret: str) -> None:
        """__init__

        Args:
            :type api_key: str
            :type api_secret: str

        Returns:
            :rtype: None

        """
        raise NotImplementedError

    def create_order(self,
                     symbol: str,
                     htype: str,
                     side: str,
                     amount: str,
                     price=None,
                     params={}) -> utils.htypes.HOrder:
        """New order

        Args:
            :type symbol: str
            :type side: str
            :type htype: str
            :type amount: str
            :type price: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HOrder

        """
        raise NotImplementedError

    def cancel_order(self,
                     order_id: str,
                     symbol=None,
                     params={}) -> bool:
        """Cancel order

        Args:
            :type order_id: str
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: bool

        """
        raise NotImplementedError

    def fetch_balance(self, params={}):
        """Get balance

        Args:
            :type params: dict

        Returns:
            :rtype: balance

        """
        raise NotImplementedError

    def fetch_order(self,
                    order_id: str,
                    symbol=None,
                    params={}) -> utils.htypes.HOrder:
        """Get order data

        Args:
            :type order_id: str
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HOrder


        """
        raise NotImplementedError

    def fetch_orders(self,
                     symbol=None,
                     since=None,
                     limit=None,
                     params={}) -> []:
        """Get order data

        Args:
            :type symbol: str
            :type since: int
            :type limit: int
            :type params: dict

        Returns:
            :rtype: utils.htypes.HOrder[]


        """
        raise NotImplementedError

    def fetch_markets(self, params={}) -> []:
        """Get market data

        Args:
            :type params: dict

        Returns:
            :rtype: utils.htypes.HMarket[]

        """
        raise NotImplementedError

    def fetch_ticker(self, symbol: str, params={}) -> utils.htypes.HTicker:
        """Get ticker data

        Args:
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTicker

        """
        raise NotImplementedError

    def fetch_tickers(self, symbol=None, params={}) -> []:
        """Get ticker data

        Args:
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTicker[]

        """
        raise NotImplementedError

    def fetch_trades(self,
                     symbol: str,
                     since=None,
                     limit=1000,
                     params={}) -> utils.htypes.HTrade:
        """Get trades

        Args:
            :type symbol: str
            :type since: int
            :type limit: int
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTrade[]

        """
        raise NotImplementedError

    def fetch_my_trades(self,
                        symbol=None,
                        since=None,
                        limit=None,
                        params={}) -> utils.htypes.HTrade:
        """Get my trades

        Args:
            :type symbol: str
            :type since: int
            :type limit: int
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTrade[]

        """
        raise NotImplementedError

    def fetch_ohlcv(self,
                    symbol: str,
                    timeframe='1m',
                    since=None,
                    limit=1000,
                    params={}) -> utils.htypes.Hohlcv:
        """Get ohlcv

        Args:
            :type symbol: str
            :type timeframe: str
            :type since: int
            :type limit: int
            :type params: dict

        Returns:
            :rtype: utils.htypes.Hohlcv[]

        """
        raise NotImplementedError