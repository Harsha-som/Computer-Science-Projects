'''Harsha Somaya
11/17/2021
CS152
project9
tets collsion of object with rotrating blcok
change directory to project 9 and run py.testcollsion.py to call
'''
# Bruce A. Maxwell
# Fall 2015
# CS 151S Project 10
#
# third test function for RotatingBlock, testing collisions
#
# Updated for Python3 by Caitrin Eaton
# 15 November 2017
#
# Modified by Eric Aaron, Fall 2018, Spring 2019
# Modified by Bruce Maxwell, Fall 2019

import graphicsPlus as gr
import physics  as pho
import collision as coll
import math
import time

            
def test():
    ''' Create a window, rotating block, and ball'''
    win = gr.GraphWin('rotator', 500, 500, False)  #window

    block = pho.RotatingBlock(win, 15, 25, 10, 5)
    block.draw()   #blcok rotating on left
    block.setRotVelocity(108)

    block2 = pho.RotatingBlock(win, 30, 25, 10, 5)
    block2.draw()   #block rotraing on right
    block2.setRotVelocity(108)

    balli = pho.Ball(win, color=(150,150,0))
    balli.setPosition(30, 25)   #anhcor green ball
    balli.draw()

    text=gr.Text(gr.Point(300,250),"anchor")
    text.setSize(10)   #anhcor text on right block
    text.setTextColor("red")
    text.draw(win)

    ball = pho.Ball(win)    #falling ball
    ball.setPosition(30, 45)
    ball.setAcceleration(0, -10)
    ball.draw()

    # execute an update loop, checking for collisions
    dt = 0.02
    for i in range(400):
        block.update(dt)
        block2.update(dt)
        
        if coll.collision(ball, block, dt):
            print('collision')
        if coll.collision(ball, block2, dt):
            print('collision')
        else:
            ball.update(dt)  #updates the ball and block
            block2.update(dt)
        if i % 10:
            win.update()
            time.sleep(0.01)  #temporaialruy delyas execution
            
        if win.checkMouse() != None:
            break

    # wait for a mouse click to quit
    win.getMouse()
    win.close()

if __name__ == "__main__":
    test()  #call function test
    
