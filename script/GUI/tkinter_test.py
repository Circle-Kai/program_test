#! /bin/usr/python3
import tkinter as tk

# <--- init the window
win = tk.Tk()
win.geometry("300x100")
win.title("標題視窗")

def btn1_click():
    btnvar.set("按下了按紐1")

def btn2_click():
    btn2.config(fg = "red")

def btn3_click():
    btn2.config(fg = "black")

# <--- Add ...
btnvar = tk.StringVar()

btn1 = tk.Button(win, width=25, textvariable=btnvar, command=btn1_click)
btn1.pack()
btn2 = tk.Button(win, width=25, text="按按鈕2", command=btn2_click)
btn2.pack(expand=1, fill=tk.X)
btn3 = tk.Button(win, width=25, text="按按鈕3", command=btn3_click)
btn3.pack(expand=1, fill=tk.Y)
label1 = tk.Label(win, bg="#ffff00", fg="#ff0000", font="Helvetica 15 bold", padx=20, pady=5, text="我是Label")
label1.pack()

# <--- Run
win.mainloop()
