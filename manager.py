from tkinter import *  
from tkinter import ttk
from container import Container
from login import Login
from login import Registro
import sys 
import os

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Manager")
        self.geometry("1100x650+120+20")
        self.resizable(False, False)
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.configure(bg="#f0f0f0")
        
        self.frames = {}
        for i in (Login ,Registro,Container):
            frame = i(container, self)
            self.frames[i] = frame

        self.show_frame(Login)
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()