# GitHub : https://github.com/lawrenceshi/WdPassport-Unlocker
# License: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import platform
import os
# , or lazy import in python 3.15
# The main file of https://github.com/0-duke/wdpassport-utils includes a special symbol, using the power of the internet and AI, I found out I should use importlib.
import importlib
WdPassportUtils = importlib.import_module("WdPassportUtils.wdpassport-utils") #very important basic package


class main(tk.Tk): # tk.Tk is a class, and main is a child class of it.
    def __init__(self): 
        super().__init__() # 所以这里是调用tk.Tk的初始化

        if platform.system() != "Linux":
            messagebox.WARNING(title = "Warning", text = "If you are not using Linux, please use the offical WD Drive Unlock program.")
            if not messagebox.askyesno(title= "Warning", text = "Are you using Linux?"):
                return 0
        
        self.title("WdPassport-Unlocker")
        self.geometry("600x800")
        self.resizable(False, False)
        self.configure(background="#9acffc")

        self.create_main_interface()
    def create_main_interface(self):

        removable_device_names = []

        for d in psutil.disk_partitions(all=False):
            if "/run/media/" not in d.mountpoint:
                removable_device_names.append(d)
    
        unlock_butten = ttk.Button(text="Unlock",command=self.unlock_disk)
        unlock_butten.place(relx=0.5, rely=0.5)

        self.mainloop()

    def unlock_disk(self):
        
        WdPassportUtils.unlock() # Test code, not using GUI.


if __name__ == "__main__":
    main()