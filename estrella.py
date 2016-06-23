import turtle
t=turtle.Pen()
x=int(input("Ingrese el numero de lados"))
grado=180+(180/x)
for i in range(0,x):
	t.forward(100)
	t.left(grado)
#t.reset()
turtle.getscreen()._root.mainloop()
