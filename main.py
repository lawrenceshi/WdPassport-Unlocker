# GitHub : https://github.com/lawrenceshi/WdPassport-Unlocker
# License: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
import tkinter as tk

class main(tk.Tk): # tk.Tk is a class, and main is a child class of it.
    def __init__(self):
        super().__init__() # 所以这里是调用tk.Tk的初始化
        self.title("WdPassport-Unlocker")
        self.geometry("600x800")
        self.resizable(False, False)

        self.mainloop()

if __name__ == "__main__":
    main()