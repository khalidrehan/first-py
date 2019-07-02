import turtle
window = turtle.Screen()
window.bgcolor("lightgreen") # Set the window background color
window.title("Hello, Tess!") # Set the window title

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue") # Tell tess to change her color
tess.pensize(3) # Tell tess to set her pen width


for i in range(20):
    tess.speed(10)
    tess.color("darkgreen")
    #tess.stamp()
    tess.left(120)
    tess.forward(50+i*10)
    
tess.left(180)


for o in range(20):
    tess.speed(2)
    tess.color("lightgreen")
    o=o+1
    tess.forward(250-o*10)
    tess.right(120)

window.mainloop()
