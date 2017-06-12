#coding: UTF-8
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_get()
r.clipboard_append(123)
print (r)