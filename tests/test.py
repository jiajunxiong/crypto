from client.binance_client import BinanceClient

if __name__ == "__main__":
    api_key = "BTvG9z6yxynXh7GpxtTq5TZCIWkb6Z66y6OlA9dAjCQRHfjVMwclwy88EekACJjq"
    api_secret = "dHVbFxVyNHTau8ou2g0G3sGQGJCCfuxmRgZlmIvBLQ9ReWoQrTf7o1tFyP8tf1QH"
    binance = BinanceClient(api_key, api_secret)
    print("Everything passed")