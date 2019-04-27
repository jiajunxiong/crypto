# -*- coding: utf-8 -*-
"""Google style docstrings.

Todo:
    * Type and Value checking
    * timeout and enableRateLimit in config file
    * ccxt.base.errors.*
    * event-driven code

"""
import ccxt
import clients.ordermanager
import clients.baseclient
import utils.htypes


class Binance(clients.baseclient.BaseClient):
    """Binance client

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
        self.api = ccxt.binance({
            'apiKey': api_key,
            'secret': api_secret,
        })
        self.ordermanager = clients.ordermanager.OrderManager("binance")

    # asycn
    def create_order(self,
                     symbol: str,
                     htype: str,
                     side: str,
                     amount: str,
                     price: str,
                     params=None) -> utils.htypes.HOrder:
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
        try:
            response = self.api.create_order(symbol, htype, side, amount, price, params)
        except (ccxt.ExchangeError, ccxt.NetworkError) as error:
            print('Got an error', type(error).__name__, error.args)
            raise

        horder = utils.htypes.HOrder(order_id=response["id"],
                                     created_at=response[""],
                                     timestamp=response["timestamp"],
                                     symbol=symbol,
                                     htype=htype,
                                     side=side,
                                     price=price,
                                     amount=amount,
                                     filled="0",
                                     order_status="0")
        self.ordermanager.on_order(horder)
        return horder

    # asycn
    def cancel_order(self,
                     order_id: str,
                     symbol=None,
                     params={}) -> bool:
        """Cancel order

        Args:
            :param order_id: str
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: bool

        """
        response = self.api.cancel_order(order_id, symbol, params)
        if response["status"] == "canceled":
            self.ordermanager.on_cancel(order_id)
            return True
        else:
            return False

    def fetch_balance(self, params={}):
        """Get balance

        Args:
            :type params: dict

        Returns:
            :rtype: balance

        """
        return self.api.fetch_balance()

    def fetch_order(self,
                    order_id: str,
                    symbol: str,
                    params={}) -> utils.htypes.HOrder:
        """Get order data

        Args:
            :type order_id: str
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HOrder


        """
        response = self.api.fetch_order(id=order_id, symbol=symbol)
        horder = utils.htypes.HOrder(order_id=response["id"],
                                     created_at=response[""],
                                     timestamp=response["timestamp"],
                                     symbol=symbol,
                                     htype=response["type"],
                                     side=response["side"],
                                     price=response["price"],
                                     amount=response["amount"],
                                     filled=response["filled"],
                                     order_status=response["status"])
        return horder

    def fetch_orders(self,
                     symbol: str,
                     params=None) -> []:
        """Get order data

        Args:
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HOrder[]


        """
        response = self.api.fetch_orders(symbol)
        horder_list = []
        for item in response["data"]:
            horder = utils.htypes.HOrder(order_id=item["id"],
                                         created_at=item[""],
                                         timestamp=item["timestamp"],
                                         symbol=symbol,
                                         htype=item["type"],
                                         side=item["side"],
                                         price=item["price"],
                                         amount=item["amount"],
                                         filled=item["filled"],
                                         order_status=item["status"])
            horder_list.append(horder)
        return horder_list

    def fetch_markets(self, params={}) -> []:
        """Get market data

        Args:
            :type params: str

        Returns:
            :rtype: utils.htypes.HMarket[]

        """
        response = self.api.fetch_markets()
        hmarket_list = []
        for item in response:
            hmarket = utils.htypes.HMarket(symbol=item["symbol"],
                                           base=item["base"],
                                           quote=item["quote"])
            hmarket_list.append(hmarket)
        return hmarket_list

    def fetch_ticker(self, symbol: str, params={}) -> utils.htypes.HTicker:
        """Get ticker data

        Args:
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTicker

        """
        self.api.fetch_ticker(symbol, params)

    def fetch_tickers(self, symbol=None, params={}) -> []:
        """Get ticker data

        Args:
            :type symbol: str
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTicker[]

        """
        self.api.fetch_tickers(symbol, params)

    def fetch_trades(self,
                     symbol: str,
                     since=None,
                     limit=1000,
                     params={}) -> []:
        """Get trades

        Args:
            :type symbol: str
            :type since: int
            :type limit: int
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTrade[]

        """
        response = self.api.fetch_trades(symbol, since, limit, params)
        htrade_list = []
        for item in response:
            htrade = utils.htypes.HTrade(order_id=item["id"],
                                         timestamp=item["timestamp"],
                                         symbol=symbol,
                                         htype=item["type"],
                                         side=item["side"],
                                         price=item["price"],
                                         amount=item["amount"],
                                         fee=item["fee"])
            htrade_list.append(htrade)
        return htrade_list

    def fetch_my_trades(self,
                        symbol=None,
                        since=None,
                        limit=None,
                        params={}) -> []:
        """Get my trades

        Args:
            :type symbol: str
            :type since: int
            :type limit: int
            :type params: dict

        Returns:
            :rtype: utils.htypes.HTrade[]

        """
        response = self.api.fetch_my_trades(symbol, since, limit, params)
        htrade_list = []
        for item in response:
            htrade = utils.htypes.HTrade(order_id=item["id"],
                                         timestamp=item["timestamp"],
                                         symbol=symbol,
                                         htype=item["type"],
                                         side=item["side"],
                                         price=item["price"],
                                         amount=item["amount"],
                                         fee=item["fee"])
            htrade_list.append(htrade)
        return htrade_list

    def fetch_ohlcv(self,
                    symbol: str,
                    timeframe='1m',
                    since=None,
                    limit=1000,
                    params={}) -> []:
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
        response = self.api.fetch_ohlcv(symbol, timeframe, since, limit, params)
        hohlcv_list = []
        for item in response:
            hohlcv = utils.htypes.Hohlcv(timestamp=item[0],
                                         open=item[1],
                                         high=item[2],
                                         low=item[3],
                                         close=item[4],
                                         volume=item[5])
            hohlcv_list.append(hohlcv)
        return hohlcv_list
