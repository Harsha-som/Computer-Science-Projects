#project 5

import graphicsPlus as gr
import random
import time


win = gr.GraphWin('messing', 400, 400)


# to draw a point

pt = gr.Point(100,50)
pt.draw(win)

#to draw a circle
cir = gr.Circle(pt, 25)
cir.draw(win)
cir.setOutline('red')
cir.setFill('blue')


#to draw a line
line = gr.Line(pt,gr.Point(150, 200))
line.draw(win)


# to draw a rectangle and move it

rect = gr.Rectangle(gr.Point(300,200), pt)
rect.draw(win)

line.move(10, 40)

def draw_shapes():
    my_circle = gr.Circle(gr.Point(100, 150), 20)
    my_circle.setFill(gr.color_rgb(200, 30, 210))
    #my_rec = gr.
    my_circle.draw(win)
    win.getMouse()
draw_shapes()

def animation_test():
    win = gr.GraphWin("Animation Test", 800, 600)
    circ = gr.Circle(gr.Point(100,100), 20)
    circ.draw(win)
    for frame in range(300):
        dy = random.randint(-2, 3)
        circ.move(2, dy)
        print(frame, "center:" , circ.getCenter())
        time.sleep(.001) # human-friendly animation speed
    #win.getKey()
    win.getMouse()
    win.close()
animation_test()
win.close() #closes window