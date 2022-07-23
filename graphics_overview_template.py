#graphics_overview.py
#
#This is the first code sample in graphics.pdf, Section 1: Overview
#It demonstrates how to create a GraphWin window and a Circle.
#
#Author: John Zelle
#Adapted for CS 152, Fall 2021 by Stacy Doore

import graphicsPlus as gr

def main():
    win = gr.GraphWin("My Circle", 100, 100)
    circle = gr.Circle(gr.Point(50, 50), 10)
    circle.draw(win)
    win.getMouse() #pause for click in window win.close()
    hi=gr.GraphWin("rect",100,10)
    square=gr.Rectangle(gr.Point(100,25),gr.Point(14,66))
    square.draw(hi)
    hi.getMouse()

main()
