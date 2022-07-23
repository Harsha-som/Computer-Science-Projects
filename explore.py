'''Harsha Somaya
10/20/2021
CS152
lab5
simulate elephnat population to make sure is wihtin carrying capacity
change directory to project 7 and run py elephant.py to call
'''
import graphicsPlus as gr
import time
import random
import math
from graphicsPlus import *

def test1():   
    '''returns position of where i click in window and makes circle'''  #explain parameters+units
    win = gr.GraphWin('My Window', 500, 500, False )
    circle = gr.Circle( gr.Point(100, 200), 10 )
    circle.draw( win )
    win.update()
    xy=win.getMouse()
    print(xy)
    win.close()
#if __name__ == "__main__":
   # test1()

def test2():
    '''makes circle move whereever i click on window'''
    win = gr.GraphWin('My Window', 500, 500, False )
    shapes=[]
    while True:
        pos=win.checkMouse()
        if pos!=None:
            circle=gr.Circle(pos, 10)
            circle.setFill("blue")
            shapes.append(circle)
            circle.draw(win)
        if win.checkKey()=="q":
            break
        win.update()
        time.sleep(.033)
        for i in shapes:
            dx=random.randint(-10,10)
            dy=random.randint(-3,2)
            i.move(dx,dy)
    vertices = []
    WIDTH=400
    HEIGHT=400
    length = min(WIDTH, HEIGHT) / 2
    print("leng is", length)
    POINTS=5
    theta = -math.pi / 2
    delta = 4 / POINTS * math.pi
    for i in range(POINTS):
        vertices.append(gr.Point(length * math.cos(theta), length * math.sin(theta)))
        theta += delta
    # Use Polygon object to draw the star
    star = gr.Polygon(vertices)
    star.setFill("red")
    star.setWidth(4)
    star.draw(win)
    win.close()
if __name__ == "__main__":
    test2()

# aCircle = gr.Circle(gr.Point(3,4), 10.5)
# print(aCircle.getCenter())
# print("r", aCircle.getRadius())
# print(aCircle.getP1())
