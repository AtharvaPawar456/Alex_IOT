from tkinter import *
import os
def all():
    path = os.path.join(os.path.dirname(__file__), "About_us.txt")
    ws = Tk()
    ws.resizable(False, False) 
    ws.title("PythonGuides")
    ws.geometry("400x400")
    ws['bg']='#fb0'
    file1 = open(path,"r+")
    data=  file1.read(1000)
    txtarea = Text(ws, width=40, height=20)
    txtarea.insert('end', data)
    txtarea.config(state='disabled')
    txtarea.pack(pady=20)
    file1.close()
    ws.mainloop()
