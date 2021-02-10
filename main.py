import tkinter as tk
from idlelib import window

window = tk.Tk()
window.title("my first pyhton app")
window.geometry("600x400")
newLabel = tk.Label(text="i hope i didnt get any errors")
newLabel.grid(column=0,row=0)
window.mainloop()

