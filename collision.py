'''Harsha Somaya
11/2/2021
CS152
lab7
create window with ball and block moving and colliding
change directory to project 7 and run py.collision.py to call
'''
# Test function written by Bruce A. Maxwell
# Fall 2019
# CS 152
# Project 8

import graphicsPlus as gr
import physics_objects as pho
import random
import time

def main():
    '''create window with ball  moving and colliding with stationary block'''
    win = gr.GraphWin("Intersections", 500, 500, False)
    win.setBackground("orange")
    ball = pho.Ball( win )  #make ball
    block = pho.Block( win, dx = 6, dy = 3 )  # make a block
    block.setPosition(25, 25)  #block at screen center
    block.draw()
    ball.setPosition( 25, 25 )  #ball at center
    ball.draw()
    textbox = gr.Text( gr.Point( 275, 50 ), "Clear" )  #textbox
    textbox.draw(win)
    def vertical():
        '''make graph paper into window'''
        for i in range (20):
            v_line = gr.Line(gr.Point(80*i, 30), gr.Point(80*i, 1000)) # set endpoints
            v_line.setWidth(3)
            v_line.draw(win)
            h_line = gr.Line(gr.Point(5, 30*i), gr.Point(1000, 30*i)) # set endpoints
            h_line.setWidth(3)
            h_line.draw(win)
    vertical() 
    block.collision( ball )  #call collision function just to make block be blue first
    while True:  #infnite loop until break
        time.sleep( 0.033 )
        key = win.checkKey()  #return last key pressed or "" 
        if key == 'q': 
            break
        elif key == 'space':
            ball.setPosition( random.randint( 15, 35), random.randint(15, 35) )  #set ball position randomly
            if block.collision( ball):  #if collide
                textbox.setText( 'Collision' )
                ball.vis[0].setFill("pink")  #ball is pik
            else:
                textbox.setText( 'clear' )
                ball.vis[0].setFill("white")  #else ball is white in no collisions
        if win.checkMouse():
            break
    win.close()
if __name__ == "__main__":
    main()