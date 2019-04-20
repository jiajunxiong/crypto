import ccxt
from .base_client import BaseClient


class BinanceClient(BaseClient):

    def __init__(self, api_key: str, api_secret: str):

        self.api = ccxt.binance({
            'apiKey': api_key,
            'secret': api_secret,
        })
        self.api_key = api_key
        self.api_secret = api_secret
        self.api.enableRateLimit = False

        self.markets = self.api.load_markets()
