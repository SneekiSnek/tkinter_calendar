import tkinter as tk
from tkinter import *
from tkcalendar import *
import datetime as dt

root = tk.Tk()
root.geometry("500x500")
root.title("Calendar")
#img = tk.PhotoImage(file="icon.png")
#root.iconphoto(False, img)
rootCanvas = tk.Canvas(root)
rootCanvas.pack(fill=tk.BOTH, expand=True)
TK_SILENCE_DEPRECATION=1

today = str(dt.date.today())
today_list = today.split("-")
for i in range(len(today_list)):
    today_list[i] = int(today_list[i])

cal = Calendar(root, selectmode="day", year=today_list[0], month=today_list[1], day=today_list[2])
cal.pack(pady=20)

def grab_date():
    gd_label.config(text=cal.get_date())

gd_button = Button(root, text="Get date", command=grab_date)
gd_button.pack(pady=20)

gd_label = Label(root, text="")
gd_label.pack(pady=20)





root.mainloop()