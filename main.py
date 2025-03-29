import MetaTrader5 as mt5
from classes import Bot
from threading import Thread
import os
from PIL import Image, ImageTk 
import tkinter as tk
# print(tk.TkVersion)


# Initialize MT5 properly
if not mt5.initialize(login=5032895927, password="1mMtR-Mb", server="MetaQuotes-Demo"):
    print("Failed to initialize MT5")
    mt5.shutdown()
    exit()

bot1 = Bot('EURUSD', 0.01, 10, 1)
bot2 = Bot('GBPUSD', 0.01, 10, 1)
bot3 = Bot('USDCAD', 0.01, 10, 1)

# meheme demm run wenne nee object 3 m
# bot1.run()
# bot2.run()
# bot3.run()

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

def initialize(): 
    login =int(login_var.get())
    password = password_var.get()
    server = server_var.get()

def run_bot1():
    symbol = bot1_symbol.get()
    volume = float(bot1_volume.get())
    no_of_levels = int(bot1_no_of_levels.get())
    profit_target = float(bot1_profit_target.get())
        
        

def b1():
    bot1.run()

def b2():
    bot2.run()

def b3():
    bot3.run()


thread1 = Thread(target=b1)
thread2 = Thread(target=b2)
thread3 = Thread(target=b3)

# thread1.start()
# thread2.start()
# thread3.start()

window.mainloop()

