import MetaTrader5 as mt5
import datetime
from tabulate import tabulate
mt5.initialize(login = 5032895927,password = "1mMtR-Mb", server = "MetaQuotes-Demo")

# print(mt5.version())

#-----------------------------------------------------------------------------
# 1. Market Data

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


#-----------------------------------------------------------------------------
# 2. Orders and Trades

# Retrieves a list of pending orders.
orders = mt5.orders_get()
print("Retrieves a list of pending orders.")
if orders:
    order_list = []
    for order in orders:
        order_list.append([
            order.ticket, order.symbol, order.volume_current, order.price_open,
            order.type, order.magic, order.comment
        ])

    headers = ["Ticket", "Symbol", "Volume", "Price", "Type", "Magic", "Comment"]
    print(tabulate(order_list, headers=headers, tablefmt="grid"))
else:
    print("No pending orders found.")


# Retrieves a list of open positions.
positions = mt5.positions_get()
print("\nRetrieves a list of open positions.")
if positions:
    position_list = []
    for position in positions:
        position_list.append([
            position.ticket, position.symbol, position.volume, position.price_open,
            position.price_current, position.type, position.profit, position.comment
        ])

    headers = ["Ticket", "Symbol", "Volume", "Open Price", "Current Price", "Type", "Profit", "Comment"]
    print(tabulate(position_list, headers=headers, tablefmt="grid"))
else:
    print("No open positions found.")

# 