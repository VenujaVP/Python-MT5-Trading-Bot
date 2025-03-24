import MetaTrader5 as mt5
import pandas as pd

mt5.initialize(login = 5032895927,password = "1mMtR-Mb", server = "MetaQuotes-Demo")

# Initialize MetaTrader5
if not mt5.initialize():
    print("Failed to initialize MetaTrader5.")
    quit()

#-----------------------------------------------------------------------------
def buy_limit(symbol,volume,price):
        response = mt5.order_send({
                "action": mt5.TRADE_ACTION_PENDING,
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_BUY_LIMIT,
                "price": price,
                "deviation": 20,
                "magic": 100,
                "comment": "python market order",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
        })
        print(response)

def sell_limit(symbol,volume,price):
        response = mt5.order_send({
                "action": mt5.TRADE_ACTION_PENDING,
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_SELL_LIMIT,
                "price": price,
                "deviation": 20,
                "magic": 100,
                "comment": "python market order",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
        })
        print(response)
# buy_limit("EURUSD", 0.01, 1.0187)
# sell_limit("EURUSD", 0.01, 1.0387)

#-----------------------------------------------------------------------------
def cal_profit(symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        profit = float(df['profit'].sum())
        return profit

def cal_volume(symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        volume = float(df['volume'].sum())
        return volume

#-----------------------------------------------------------------------------
def cal_buy_profit(symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        df = df.loc[df.type == 0]
        profit = float(df['profit'].sum())
        return profit

def cal_sell_profit(symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        df = df.loc[df.type == 1]
        profit = float(df['profit'].sum())
        return profit

#-----------------------------------------------------------------------------
def cal_buy_margin(symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        df = df.loc[df.type == 0]
        sum = 0

        for i in df.index:
                volume = df.volume[i]
                open_price = df.price_open[i]
                margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, volume, open_price)
                sum += margin

        return sum

def cal_sell_margin(symbol):
        positions = mt5.positions_get(symbol=symbol)
        df = pd.DataFrame(list(positions), columns=positions[0]._asdict().keys())
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
        df = df.loc[df.type == 1]
        sum = 0

        for i in df.index:
                volume = df.volume[i]
                open_price = df.price_open[i]
                margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, symbol, volume, open_price)
                sum += margin

        return sum

#---------------------------------------------------------------------
def cal_buy_pct_profit(symbol):
        profit = cal_buy_profit(symbol)
        margin_b = cal_buy_margin(symbol)
        pct_profit = (profit/margin_b) * 100
        return pct_profit

def cal_sell_pct_profit(symbol):
        profit = cal_buy_profit(symbol)
        margin_s = cal_sell_margin(symbol)
        pct_profit = (profit/margin_s) * 100
        return pct_profit

#---------------------------------------------------------------------
#close app positions
def close_position(position):
    tick = mt5.symbol_info_tick(position.symbol)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "position": position.ticket,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt5.ORDER_TYPE_BUY if position.type == 1 else mt5.ORDER_TYPE_SELL,
        "price": tick.ask if position.type == 1 else tick.bid,
        "deviation": 20,
        "magic": 100,
        "comment": "python script close",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    return result

def close_all(symbol):
        positions = mt5.positions_get(symbol=symbol)
        for i in positions:
                close_position(i)

# profir = close_all("EURUSD")
# print(profir)

#---------------------------------------------------------------------
# close pending orders
# Close a single pending order
def delete_pending(ticket):
    close_request = {
        "action": mt5.TRADE_ACTION_REMOVE,
        "order": ticket,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(close_request)

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        result_dict = result._asdict()
        print(result_dict)
    else:
        print(f"Delete complete for ticket {ticket}...")


# Close all pending orders for a given symbol
def close_all_pending(symbol):
    # Get all pending orders for the symbol
    orders = mt5.orders_get(symbol=symbol)
    
    # Check if there are any orders
    if len(orders) == 0:
        print(f"No pending orders found for {symbol}.")
        return
    
    # Convert orders to a DataFrame
    df = pd.DataFrame(list(orders), columns=orders[0]._asdict().keys())
    
    # Drop unnecessary columns
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial',
             'price_stoplimit'], axis=1, inplace=True)
    
    # Convert 'time_setup' to a readable datetime format
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    
    # Close each pending order
    for ticket in df.ticket:
        delete_pending(ticket)


# Close all pending orders for EURUSD
# close_all_pending('EURUSD')

# --------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------

symbol = 'GBPUSD'
volume = 0.01
no_of_levels = 10
profit_target = 1  

# --------------------------------------------------------------------------------------------------------------------------------
#Create grid orders
"""
pct_change_sell = 1
tick = mt5.symbol_info_tick("EURUSD")
current_price_sell = tick.bid

for i in range(5):
       price = (pct_change_sell/(100*100) * current_price_sell) + current_price_sell
       #100*100 = 100 * leverage
       sell_limit("EURUSD", 0.01, price)
       pct_change_sell = pct_change_sell + 1

pct_change_buy = -1
tick = mt5.symbol_info_tick("EURUSD")
current_price_buy = tick.bid

for i in range(5):
       price = (pct_change_buy/(100*100) * current_price_buy) + current_price_buy
       #100*100 = 100 * leverage
       buy_limit("EURUSD", 0.01, price)
       pct_change_buy = pct_change_buy - 1
"""

def drow_grid(symbol, volume, no_of_levels):
        pct_change_sell = 1
        tick = mt5.symbol_info_tick(symbol)
        current_price_sell = tick.bid

        for i in range(no_of_levels):
                price = (pct_change_sell/(100*100) * current_price_sell) + current_price_sell
                #100*100 = 100 * leverage
                sell_limit(symbol, volume, price)
                pct_change_sell = pct_change_sell + 1

        pct_change_buy = -1
        tick = mt5.symbol_info_tick(symbol)
        current_price_buy = tick.bid

        for i in range(no_of_levels):
                price = (pct_change_buy/(100*100) * current_price_buy) + current_price_buy
                #100*100 = 100 * leverage
                buy_limit(symbol, volume, price)
                pct_change_buy = pct_change_buy - 1

drow_grid(symbol, volume, no_of_levels)

# --------------------------------------------------------------------------------------------------------------------------------
#Create grid orders

"""
while True:
    # Retrieve all open positions for the symbol "EURUSD"
    positions = mt5.positions_get(symbol="EURUSD")

    # Check if there are any open positions
    if len(positions) > 0:
        # Calculate margin for sell and buy positions
        margin_s = cal_sell_margin("EURUSD")
        margin_b = cal_buy_margin("EURUSD")

        # Check if there are active sell positions
        if margin_s > 0:
            # Calculate profit percentage for sell positions
            pct_profit_sell = cal_sell_pct_profit("EURUSD")
            if pct_profit_sell >= 1:
                # Close all positions if profit threshold is met
                close_all("EURUSD")
                print("Sell positions closed")

        # Check if there are active buy positions
        if margin_b > 0:
            # Calculate profit percentage for buy positions
            pct_profit_buy = cal_buy_pct_profit("EURUSD")
            if pct_profit_buy >= 1:
                # Close all positions if profit threshold is met
                close_all("EURUSD")
                print("Buy positions closed")
        
        # Refresh the positions list after closing orders
        positions = mt5.positions_get(symbol="EURUSD")
        
        # If all positions are closed, cancel all pending orders and exit loop
        if len(positions) == 0:
            close_all_pending("EURUSD")
            print("All positions closed")
            break  # Exit the loop
"""
                
while True:
    # Retrieve all open positions for the symbol "EURUSD"
    positions = mt5.positions_get(symbol=symbol)

    # Check if there are any open positions
    if len(positions) > 0:
        # Calculate margin for sell and buy positions
        margin_s = cal_sell_margin(symbol)
        margin_b = cal_buy_margin(symbol)

        # Check if there are active sell positions
        if margin_s > 0:
            # Calculate profit percentage for sell positions
            pct_profit_sell = cal_sell_pct_profit(symbol)
            if pct_profit_sell >= profit_target:
                close_all(symbol)
                print("Sell positions closed")

        # Check if there are active buy positions
        if margin_b > 0:
            # Calculate profit percentage for buy positions
            pct_profit_buy = cal_buy_pct_profit(symbol)
            if pct_profit_buy >= profit_target:
                close_all(symbol)
                print("Buy positions closed")
        
        # Refresh the positions list after closing orders
        positions = mt5.positions_get(symbol=symbol)
        
        # If all positions are closed, cancel all pending orders and exit loop
        if len(positions) == 0:
            close_all_pending(symbol)
            print("All positions closed")
            break  # Exit the loop