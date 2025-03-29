import MetaTrader5 as mt5
from classes import Bot

mt5.initialize(login = 5032895927,password = "1mMtR-Mb", server = "MetaQuotes-Demo")


bot1 = Bot('EURUSD', 0.01, 10, 1)
bot1 = Bot('GBPUSD', 0.01, 10, 1)
bot1 = Bot('USDCAD', 0.01, 10, 1)


bot1.run()