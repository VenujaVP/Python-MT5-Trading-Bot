import MetaTrader5 as mt5
from classes import Bot
from threading import Thread
import os
from PIL import Image, ImageTk 
import tkinter as tk
# print(tk.TkVersion)

# bot1 = Bot('EURUSD', 0.01, 10, 1)
# bot2 = Bot('GBPUSD', 0.01, 10, 1)
# bot3 = Bot('USDCAD', 0.01, 10, 1)

# meheme demm run wenne nee object 3 m
# bot1.run()
# bot2.run()
# bot3.run()

# def b1():
#     bot1.run()

# def b2():
#     bot2.run()

# def b3():
#     bot3.run()


# thread1 = Thread(target=b1)
# thread2 = Thread(target=b2)
# thread3 = Thread(target=b3)

# thread1.start()
# thread2.start()
# thread3.start()

window = tk.Tk()
window.title("Trading Bot")
window.configure(bg='black')
window.resizable(False, False)
window.geometry("450x750")

img = Image.open("icon.jpeg")  # Use your existing JPEG
icon = ImageTk.PhotoImage(img)
window.iconphoto(False, icon)

login_var = tk.StringVar()
password_var = tk.StringVar()
server_var = tk.StringVar()

bot1_symbol = tk.StringVar()
bot1_volume = tk.StringVar()
bot1_no_of_levels = tk.StringVar()
bot1_profit_target = tk.StringVar()

bot2_symbol = tk.StringVar()
bot2_volume = tk.StringVar()
bot2_no_of_levels = tk.StringVar()
bot2_profit_target = tk.StringVar()

bot3_symbol = tk.StringVar()
bot3_volume = tk.StringVar()
bot3_no_of_levels = tk.StringVar()
bot3_profit_target = tk.StringVar()

# login=5032895927, password="1mMtR-Mb", server="MetaQuotes-Demo"
def initialize(): 
    login =int(login_var.get())
    password = password_var.get()
    server = server_var.get()
    if not mt5.initialize(login=login, password=password, server=server):
        print("Failed to initialize MT5")
        mt5.shutdown()
        exit()

def run_bot1():
    symbol = bot1_symbol.get()
    volume = float(bot1_volume.get())
    no_of_levels = int(bot1_no_of_levels.get())
    profit_target = float(bot1_profit_target.get())
    bot1 = Bot(symbol, volume, no_of_levels, profit_target)
    thread  = Thread(target=bot1.run)
    thread.start()

def run_bot2():
    symbol = bot2_symbol.get()
    volume = float(bot2_volume.get())
    no_of_levels = int(bot2_no_of_levels.get())
    profit_target = float(bot2_profit_target.get())
    bot2 = Bot(symbol, volume, no_of_levels, profit_target)
    thread  = Thread(target=bot2.run)
    thread.start()
        
def run_bot3():
    symbol = bot3_symbol.get()
    volume = float(bot3_volume.get())
    no_of_levels = int(bot3_no_of_levels.get())
    profit_target = float(bot3_profit_target.get())
    bot3 = Bot(symbol, volume, no_of_levels, profit_target)
    thread  = Thread(target=bot3.run)
    thread.start()       

login_label = tk.Label(window, text="Login", bg='black', fg='white')
login_entry = tk.Entry(window, textvariable=login_var, bg='black', fg='white')
password_label = tk.Label(window, text="password", bg='black', fg='white')
password_entry = tk.Entry(window, textvariable=password_var, bg='black', fg='white')
server_label = tk.Label(window, text="server", bg='black', fg='white')
server_entry = tk.Entry(window, textvariable=server_var, bg='black', fg='white')
initialize_button = tk.Button(window, text="Initialize", command=initialize, bg='black', fg='white')

#bot1
symbol_bot1_label = tk.Label(window, text="Symbol", bg='black', fg='white')
symbol_bot1_entry = tk.Entry(window, textvariable=bot1_symbol, bg='black', fg='white')
volume_bot1_label = tk.Label(window, text="Volume", bg='black', fg='white')
volume_bot1_entry = tk.Entry(window, textvariable=bot1_volume, bg='black', fg='white')
no_of_level_bot1_label = tk.Label(window, text="No Of Levels", bg='black', fg='white')
no_of_level_bot1_entry = tk.Entry(window, textvariable=bot1_no_of_levels, bg='black', fg='white')
profit_target_bot1_label = tk.Label(window, text="Profit Target", bg='black', fg='white')
profit_target_bot1_entry = tk.Entry(window, textvariable=bot1_profit_target, bg='black', fg='white')
bot1_run_button = tk.Button(window, text="Run Bot 1", command=run_bot1, bg='black', fg='white')

#bot2
symbol_bot2_label = tk.Label(window, text="Symbol", bg='black', fg='white')
symbol_bot2_entry = tk.Entry(window, textvariable=bot2_symbol, bg='black', fg='white')
volume_bot2_label = tk.Label(window, text="Volume", bg='black', fg='white')
volume_bot2_entry = tk.Entry(window, textvariable=bot2_volume, bg='black', fg='white')
no_of_level_bot2_label = tk.Label(window, text="No Of Levels", bg='black', fg='white')
no_of_level_bot2_entry = tk.Entry(window, textvariable=bot2_no_of_levels, bg='black', fg='white')
profit_target_bot2_label = tk.Label(window, text="Profit Target", bg='black', fg='white')
profit_target_bot2_entry = tk.Entry(window, textvariable=bot2_profit_target, bg='black', fg='white')
bot2_run_button = tk.Button(window, text="Run Bot 2", command=run_bot2, bg='black', fg='white')

#bot3
symbol_bot3_label = tk.Label(window, text="Symbol", bg='black', fg='white')
symbol_bot3_entry = tk.Entry(window, textvariable=bot3_symbol, bg='black', fg='white')
volume_bot3_label = tk.Label(window, text="Volume", bg='black', fg='white')
volume_bot3_entry = tk.Entry(window, textvariable=bot3_volume, bg='black', fg='white')
no_of_level_bot3_label = tk.Label(window, text="No Of Levels", bg='black', fg='white')
no_of_level_bot3_entry = tk.Entry(window, textvariable=bot3_no_of_levels, bg='black', fg='white')
profit_target_bot3_label = tk.Label(window, text="Profit Target", bg='black', fg='white')
profit_target_bot3_entry = tk.Entry(window, textvariable=bot3_profit_target, bg='black', fg='white')
bot3_run_button = tk.Button(window, text="Run Bot 3", command=run_bot3, bg='black', fg='white')


login_label.grid(row=0, column=0, padx=10, pady=10)
login_entry.grid(row=0, column=1, padx=10, pady=5)
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)
server_entry.grid(row=2, column=1, padx=10, pady=5)
server_label.grid(row=2, column=0, padx=10, pady=5)
initialize_button.grid(row=1, column=0, padx=10, padx=10, pady=5)
#bot1


window.mainloop()

