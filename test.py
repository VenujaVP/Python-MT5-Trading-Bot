import MetaTrader5 as mt5
import datetime
mt5.initialize(login = 5032895927,password = "1mMtR-Mb", server = "MetaQuotes-Demo")

# print(mt5.version())

# get symbols list and information
symbols = mt5.symbols_get()
symbols_list = []
for symbol in symbols:
    symbols_list.append(symbol.name)
    # print(symbol.name)
# print("Symbols list: ", symbols_list)
# print("Total symbols: ", len(symbols_list))

# Retrieves detailed information about a specific symbol
symbol_info = mt5.symbol_info("EURUSD")
# print(symbol_info)

# Retrieves historical price data (OHLCV) for a symbol
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime.datetime.now(), 100)
# print(rates)
