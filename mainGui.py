import tkinter
import tkinter.ttk as ttk
import xdotool as xdo
from tkinter import *

def createWidgets(root, ix, app_name):
    name_label = tkinter.Label(root,text=app_name)
    name_label.grid(column=0,row=ix)
    button = tkinter.Button(root,text='起動',command=startUpApp)
    button.grid(column=1,row=ix,padx=10,pady=10)
    val = tkinter.StringVar()
    array = tuple(range(int(xdo.get_workspace_count())))
    combo = ttk.Combobox(root, values = array, textvariable=val, state='readonly', width=4)
    combo.grid(column=2,row=ix)
    combo.bind('<<ComboboxSelected>>', lambda event: changeWorkspace(val.get()))
    combo.current(getCurrentid(app_name))
    return root

def getCurrentid(app_name):
    id_array = xdo.get_window_id(app_name)
    for id in id_array:
        if xdo.get_workspace_num(id) != -1:
            work_num = xdo.get_workspace_num(id)
    return work_num

def changeWorkspace(val):
    print(val)

def startUpApp():
    print('start')
