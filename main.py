# GitHub : https://github.com/lawrenceshi/WdPassport-Unlocker
# License: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
import tkinter as tk
from tkinter import ttk

class main(tk.Tk): # tk.Tk is a class, and main is a child class of it.
    def __init__(self):
        super().__init__() # 所以这里是调用tk.Tk的初始化

        self.title("WdPassport-Unlocker")
        self.geometry("600x800")
        self.resizable(False, False)

        self.create_main_interface()
    def create_main_interface(self):
        
        unlock_butten = ttk.Button(text="Unlock",command=self.unlock_disk)
        unlock_butten.place(relx=0.5, rely=0.5)


        self.mainloop()

    def unlock_disk(self):
        print("Clicked the butten!")

if __name__ == "__main__":
    main()