#graph_paper.py
#
#This is the first code sample in graphics.pdf, Section 1: Overview
#It demonstrates how to create a GraphWin window and a Circle.
#
#Author: John Zelle
#Adapted for CS 152, Fall 2021 by Stacy Doore

import graphicsPlus as gr

def main(x):
    win = gr.GraphWin("Graph Paper", 1000, 1000)
    #circle = gr.Circle(gr.Point(50, 50), 10)
    #circle.draw(win)
    #win.getMouse() #pause for click in window win.close()

    def vertical():
        for i in range (x):
            v_line = gr.Line(gr.Point(80*i, 30), gr.Point(80*i, 1000)) # set endpoints
            v_line.setWidth(3)
            v_line.draw(win)
            h_line = gr.Line(gr.Point(5, 30*i), gr.Point(1000, 30*i)) # set endpoints
            h_line.setWidth(3)
            h_line.draw(win)
    vertical() 
    # Text message and close window on click
    message = gr.Text(gr.Point(win.getWidth()/5, 10), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()
main(30)
