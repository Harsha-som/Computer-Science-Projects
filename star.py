import math
from graphicsPlus import *
import graphicsPlus as gr
import random as random
POINTS = 5
WIDTH, HEIGHT = 600, 600

def main():
    win = gr.GraphWin('hi', WIDTH, HEIGHT)
    #win.setCoords(-WIDTH/2, -HEIGHT/2, WIDTH/2, HEIGHT/2)
    #win.setBackground('pink')

    vertices = []

    length = 25

    theta = -math.pi / 2
    delta = 4 / POINTS * math.pi

    for _ in range(POINTS):
        vertices.append(gr.Point(length * math.cos(theta), length * math.sin(theta)))
        theta += delta

    # Use Polygon object to draw the star
    star = gr.Polygon(vertices)
    star.setFill('blue')
    print("k,",star.getPoints())
    #star.setOutline('red')
    #star.setWidth(1)  # width of boundary line
    setrandompos(star,random.randint(0,600),random.randint(0,600))
    star.draw(win)
    win.getMouse()
    win.close()
def setrandompos(self,px,py):			
 		self.move(px,py)

main()