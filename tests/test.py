import enum
import utils.hutils
import utils.htypes
import clients.huobi
import clients.binance

if __name__ == "__main__":
    config_list = utils.hutils.read_conf("clients.conf")
    client = clients.binance.Binance(config_list["binance"]["api_key"], config_list["binance"]["api_secret"])
    print(client.fetch_balance())
    horder = client.create_order("ETH/USDT", "buy", "limit", "0.01", "155", {})
    #hohlcv_list = client.fetch_ohlcv("ETH/USDT")
    #for item in hohlcv_list:
        #utils.htypes.Hohlcv.print_out(item)
    #htrade_list = (client.fetch_my_trades())
    #for item in htrade_list:
        #utils.htypes.HTrade.print_out(item)
    #hmarket_list = client.fetch_markets()
    #for item in hmarket_list:
        #utils.htypes.HMarket.print_out(item)
    #print(client.fetch_balance)
