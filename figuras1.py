import time
from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
canvas.create_rectangle(150,150,200,200)
canvas.create_oval(80,80,120,120)
def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
        canvas.move(3,1,4)
        canvas.move(2,4,5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
        canvas.move(3,1,-4)
        canvas.move(2,-4,5)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
        canvas.move(3,1,4)
        canvas.move(2,4,5) 
    else:
        canvas.move(1, 3, 0)
        canvas.move(3,1,-4)
        canvas.move(2,-4,5)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()