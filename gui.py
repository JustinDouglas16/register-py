# gui.py
import tkinter as tk
from form import UserForm

class GUI:
    def __init__(self, root, session):
        self.root = root
        self.root.geometry('300x200')
        self.form = UserForm(self.root, session)

    def run(self):
        self.root.mainloop()