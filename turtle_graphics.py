import tkinter
import turtle
import math

window=tkinter.Tk()
window.title("TURTLE GRAPHICS WITH TKINTER")
t=turtle.Turtle()
spin = tkinter.IntVar()

def circle_spirograph():
    t.reset()
    wn=turtle.Screen()
    wn.title("CIRCLE SPIROGRAPH")
    wn.bgcolor("black")
    t.pensize(2)
    t.speed(20)
    t.shape('square')
    for i in range(6):
        for colours in ['red','violet','cyan','yellow','magenta','green']:
            t.color(colours,'brown')
            t.circle(100)
            t.left(10)
    turtle.done()
    
def square_spirograph():
    t.reset()
    wn=turtle.Screen()
    wn.title("SQUARE SPIROGRAPH")
    t.shape('arrow')
    t.speed(0)
    t.pensize(3)
    wn.bgcolor("black")
    for i in range(5):
        for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
            t.color(colours,'SlateBlue4')
            t.left(12)
            t.circle(100,steps=4)
    turtle.done()
        
def rainbow_benzene():
    t.reset()
    wn=turtle.Screen()
    wn.title("RAINBOW BENZENE")
    t.shape('circle')
    t.speed(0)
    wn.bgcolor("black")
    colours=["red","purple","blue","green","orange","yellow"]
    for x in range(120):
        t.color(colours[x%6],'VioletRed4')
        t.width(x/100+1)
        t.forward(x)
        t.left(59)
    turtle.done()
    
def draw_tree(i):
    t.speed(0)
    if i<10:
        return
    else:
        t.forward(i)
        t.left(30)
        draw_tree(3*i/4)
        t.right(60)
        draw_tree(3*i/4)
        t.left(30)
        t.backward(i)
def ytree_fractal():
    t.reset()
    wn=turtle.Screen() 
    wn.title("Y TREE FRACTAL")
    wn.bgcolor('white')
    t.shape('turtle')
    t.color('brown','green')
    t.up()
    t.goto(0,-100)
    t.down()
    t.left(90)
    t.speed(150)
    draw_tree(100)
    turtle.done()
    
def spider_web():
    t.reset()
    t.speed(0)
    wn=turtle.Screen()
    wn.title("SPIDER WEB")
    wn.bgcolor('black')
    t.shape('triangle')
    t.color('grey','salmon1')
    for i in range(6):
        t.forward(150)
        t.backward(150)
        t.right(60)
    side=150
    for i in range(15):
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.setheading(0)
        t.forward(side)
        t.right(120)
        for j in range(6):
            t.forward(side)
            t.right(60)
        side=side-10
    turtle.done()
        
def draw_snowflake(lengthSide, levels):
    t.speed(0)
    if levels == 0: 
        t.forward(lengthSide) 
        return
    lengthSide /= 3.0
    draw_snowflake(lengthSide, levels-1) 
    t.left(60) 
    draw_snowflake(lengthSide, levels-1) 
    t.right(120) 
    draw_snowflake(lengthSide, levels-1) 
    t.left(60) 
    draw_snowflake(lengthSide, levels-1) 
def koch_snowflake():
    t.reset()
    wn=turtle.Screen()
    wn.title("KOCH SNOWFLAKE")
    wn.bgcolor('white')
    t.shape('classic')
    t.speed(0)                 
    length = 300.0   
    t.pensize(2)
    t.color('black','SkyBlue')        
    t.penup()                      
    t.backward(length/2.0) 
    t.pendown()
    t.begin_fill()
    for i in range(3):     
        draw_snowflake(length, 4)
        t.right(120) 
    t.fillcolor("SkyBlue")
    t.end_fill()
    turtle.done()
    
def draw_sierpinski(n,length):
    t.speed(0)
    if n==1:
        t.setheading(180)      
        for i in range(3):       
            t.rt(120)          
            t.fd(length)  
    else:
        draw_sierpinski(n-1, length)
        t.rt(120)
        t.fd(length * 2 ** (n - 2))
        draw_sierpinski(n -1, length)
        t.lt(120)
        t.fd(length * 2 ** (n - 2))
        draw_sierpinski(n - 1, length)
        t.fd(length * 2 ** (n - 2))
def sierpinski_triangle():
    t.reset()
    wn=turtle.Screen()
    wn.title("SIERPINSKI TRIANGLE")
    wn.bgcolor('white')
    t.shape('square')
    t.speed(0)
    draw_sierpinski(4,50)
    turtle.done()

def draw_fibonacci(n,factor):
    t.speed(0)
    a=0
    b=1
    square_a=a
    square_b=b
    t.forward(b * factor) 
    t.left(90) 
    t.forward(b * factor) 
    t.left(90) 
    t.forward(b * factor) 
    t.left(90) 
    t.forward(b * factor) 
    temp = square_b 
    square_b = square_b + square_a 
    square_a = temp 
    for i in range(1, n): 
        t.backward(square_a * factor) 
        t.right(90) 
        t.forward(square_b * factor) 
        t.left(90) 
        t.forward(square_b * factor) 
        t.left(90) 
        t.forward(square_b * factor) 
  
        temp = square_b 
        square_b = square_b + square_a 
        square_a = temp 
   
    t.penup() 
    t.setposition(factor, 0) 
    t.seth(0) 
    t.pendown() 
    t.color("red","DarkBlue") 
    t.left(90) 
    for i in range(n): 
        print(b) 
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90): 
            t.forward(fdwd) 
            t.left(1) 
        temp = a 
        a = b 
        b = temp + b 
def fibonacci():
    t.speed(0)
    t.reset()
    wn=turtle.Screen()
    wn.title("FIBONACCI FRACTAL")
    t.shape('arrow')
    t.pensize(2)
    wn.bgcolor("black")
    t.color("white","DarkBlue")
    draw_fibonacci(int(spin.get()),1)
def fibonacci_fractal():
    window2=tkinter.Tk()
    window2.title("FIBONACCI FRACTAL")
    tkinter.Label(window2,text="ENTER THEE NUMBER OF ITERATIONS",fg="black",bg="white").pack()
    global spin    
    spin=tkinter.Spinbox(window2,from_=2,to=20,width=5)
    spin.pack()
    #n=spin.get()
    tkinter.Button(window2,text="OK",fg="red4",bg="white",command=fibonacci).pack()
    turtle.done()
    
def draw_hilbert(t,A,parity,n):
    t.speed(0)
    if n<1:
        return
    t.left(parity*90)
    draw_hilbert(t,A,-parity,n-1)
    t.forward(A)
    t.right(parity*90)
    draw_hilbert(t,A,parity,n-1)
    t.forward(A)
    draw_hilbert(t,A,parity,n-1)
    t.right(parity*90)
    t.forward(A)
    draw_hilbert(t,A,-parity,n-1)
    t.left(parity*90)
def hilbert_curve():
    t.reset()
    wn = turtle.Screen()
    wn.title("Hilbert Curve")
    wn.bgcolor("black")
    t.shape('circle')
    t.color("white","azure4")
    t.speed(0)
    t.pensize(2)
    draw_hilbert(t,10,1,4)
    turtle.done()    
tkinter.Label(window,text="Tap the shape to view",fg="black",bg="white").pack(fill="x")
tkinter.Button(window,text="CIRCLE SPIROGRAPH",fg="red",bg="white",command=circle_spirograph).pack()
tkinter.Button(window,text="SQUARE SPIROGRAPH",fg="orange",bg="white",command=square_spirograph).pack()
tkinter.Button(window,text="RAINBOW BENZENE",fg="cyan",bg="white",command=rainbow_benzene).pack()
tkinter.Button(window,text="Y FRACTAL TREE",fg="green",bg="white",command=ytree_fractal).pack()
tkinter.Button(window,text="SPIDER WEB",fg="blue",bg="white",command=spider_web).pack()
tkinter.Button(window,text="KOCH SNOWFLAKE",fg="darkblue",bg="white",command=koch_snowflake).pack()
tkinter.Button(window,text="SIERPINSKI TRIANGLE",fg="violet",bg="white",command=sierpinski_triangle).pack()
tkinter.Button(window,text="FIBONACCI FRACTAL",fg="brown",bg="white",command=fibonacci_fractal).pack()
tkinter.Button(window,text="HILBERT CURVE",fg="DeepPink",bg="white",command=hilbert_curve).pack()
window.mainloop()