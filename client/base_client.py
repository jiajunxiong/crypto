class BaseClient(object):

    def __init__(self, api_key: str, api_secret: str):
        NotImplementedError

    def get_latest_trade_time(self, symbol):
        NotImplementedError

    def get_
