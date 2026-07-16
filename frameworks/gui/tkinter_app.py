import tkinter as tk
from frameworks.config import *


class ContactApplication:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Contact Management")

        self.window.geometry("800x600")

    def run(self):

        self.window.mainloop()

