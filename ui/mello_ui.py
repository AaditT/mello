import tkinter as tk
from tkinter import *
ui = tk.Tk()
ui.title('mello')

def gen():
    emotion = entry.get()
    print("You are feeling "+emotion)
    print("Generating melody...")

canvas = Canvas(ui, width=500,height=300)
canvas.pack()

mello = PhotoImage(file='//home/pi//Downloads//mello.gif')
canvas.create_image(150,50,anchor=NW,image=mello)

label = Label(ui, text='Enter Emotion:')
label.pack()
entry = Entry(ui)
entry.pack()
button = Button(ui, text="Generate Melody",command=gen)
button.pack()

ui.mainloop()
