import tkinter
from tkinter import Tk
from tkinter.constants import *
tk = tkinter.Tk()
tk.title('fy')
tk.geometry('600x600')

frame = tkinter.Frame(tk,background='red',relief='sunken',borderwidth=2)
frame.pack(fill='x')
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill='y')
#
# label = tkinter.Label(frame, text="lllll")
# label.pack(fill=X, expand=1)
#
# button = tkinter.Button(frame,text="Exit",command=tk.keys)
# button.pack(side=LEFT)
#
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()