import turtle
import os

win=turtle.Screen()
win.bgcolor("blue")
t = turtle.Pen()
t.color(1,0,0)
t.begin_fill()
#LINEA PARA ARRIBA
t.left(90)
t.forward(100)
#LINEA PARA LA DERECHA
t.right(90)
t.forward(100)
#LINEA PARA ABAJO
t.left(-90)
t.forward(20)
#LINEA IZQUIERDA
t.right(90)
t.forward(70)
#LINEA PARA ABAJO
t.left(90)
t.forward(20)
#LINE PARA LA DERECHA
t.right(-90)
t.forward(50)
#LINEA PARA ABAJO
t.left(-90)
t.forward(20)
#LINEA IZQUIERDA
t.right(90)
t.forward(50)
#LINEA PARA abajo
t.left(90)
t.forward(40)
#LINEA IZQUIERDA
t.right(90)
t.forward(30)
t.end_fill()

turtle.getscreen()._root.mainloop()