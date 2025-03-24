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
    # print(tabulate(order_list, headers=headers, tablefmt="grid"))
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
    # print(tabulate(position_list, headers=headers, tablefmt="grid"))
else:
    print("No open positions found.")


# Sends a trade request (e.g., open/close orders, modify orders).

# Example (placing a buy market order):

# Prepare the trade request
symbol = "EURUSD"
tick_info = mt5.symbol_info_tick(symbol)

if tick_info is None:
    print(f"Failed to retrieve tick info for {symbol}")
    mt5.shutdown()
    quit()
    
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 0.1,
    "type": mt5.ORDER_TYPE_BUY,
    "price": tick_info.ask,
    "deviation": 10,
    "magic": 123456,
    "comment": "Python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

# Send the order
result = mt5.order_send(request)

# Display the result in a structured format
if result.retcode == mt5.TRADE_RETCODE_DONE:
    order_data = [
        ["Order Ticket", result.order],
        ["Symbol", symbol],
        ["Volume", request["volume"]],
        ["Open Price", request["price"]],
        ["Deviation", request["deviation"]],
        ["Magic Number", request["magic"]],
        ["Comment", request["comment"]],
        ["Execution Result", "Order placed successfully! ✅"],
    ]
else:
    order_data = [
        ["Order Ticket", result.order],
        ["Symbol", symbol],
        ["Error Code", result.retcode],
        ["Error Description", "Order failed ❌"],
    ]

print(tabulate(order_data, tablefmt="grid"))

# Cancels a pending order by its ticket number.
mt5.order_cancel(ticket=123456)