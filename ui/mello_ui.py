import tkinter as tk
from tkinter import *
ui = tk.Tk()
ui.title('mello')

canvas = Canvas(ui, width=500,height=200)
canvas.pack()

mello = PhotoImage(file='//home/pi//Downloads//mello.gif')
enteremotion = PhotoImage(file='//home/pi//Downloads//enteremotion.gif')
enteremotion.zoom(200,200)
canvas.create_image(0,0, anchor=NW, image=enteremotion)
canvas.create_image(150,100,anchor=NW,image=mello)

ui.mainloop()
