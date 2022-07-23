import math
from graphicsPlus import *
import graphicsPlus as gr
import random as random

POINTS = 8
WIDTH, HEIGHT = 600, 600

# def main():
#     win = gr.GraphWin('anyhting', WIDTH, HEIGHT)
#     #win.setCoords(-WIDTH/2, -HEIGHT/2, WIDTH/2, HEIGHT/2)
#     vertices = []

#     length = random.randint(0,1000)
#     print("lengh is", length)

#     theta = -math.pi / 2
#     delta = 4 / POINTS * math.pi
#     for _ in range(POINTS):
#         vertices.append(gr.Point(length * math.cos(theta), length * math.sin(theta)))
#         theta += delta

#     # Use Polygon object to draw the star
#     if win.checkKey()=="r":
#         star = gr.Polygon(vertices)
#         star.setFill('darkgreen')
#         star.setOutline('red')
#         star.setWidth(4)  # width of boundary line
#         star.draw(win)

#     win.getMouse()
#     win.close()

#main()