# main.py
from tkinter import Tk
from db import Database
from gui import GUI

db = Database('mysql+pymysql://root:@localhost/python')
session = db.create_session()

root = Tk()
gui = GUI(root, session)
gui.run()