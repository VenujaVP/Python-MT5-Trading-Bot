import MetaTrader5 as mt5
from classes import Bot
from threading import Thread
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

icon = tk.PhotoImage(file="icon.png")
window.iconphoto(False, icon)

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

