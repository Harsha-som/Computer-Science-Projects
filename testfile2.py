'''Harsha Somaya
11/2/2021
CS152
lab7
create a ball colliding with block at bottom and regenrates
change directory to project 7 and run py.testfile2.py to call
'''

# template written by Bruce A. Maxwell
# updated by <your name here>
# Fall 2019
# CS 152
# Project 8

import graphicsPlus as gr
import physics_objects as pho
import random
import time

# def __init__(self,win,dx,dy):
#     '''create rectangle'''
#     self.win = win
#     self.dx=dx
#     self.dy=dy
#     self.velocity=[0,0]
#     self.position=[400,400]         
#     self.width=0
#     self.height=0
#     self.scale=10
#     self.accelaration=[0,0]
#     self.vis = [gr.Rectangle(gr.Point((self.position[0]-dx/2)*self.scale,win.getHeight()-((self.position[1]-dy)/2)*self.scale),gr.Point((self.position[0]+dx/2)*self.scale,win.getHeight()-(self.position[1]+dy/2)*self.scale))]
def main():
        win = gr.GraphWin("Falling", 500, 500, False)
        ball = pho.Ball(win)
        ball.setPosition(100,100)
        ball.setVelocity(random.randint(0,20), random.randint(0,20))# give it a random velocity
        ball.setAcceleration(0,-20)# set the acceleration to (0, -20)
        ball.draw()
        # block = pho.Block( win, dx = 6, dy = 3 )  # make a block
        # block.setPosition(25, 25)  #block at screen center
        # block.draw()
        while True:
            ball.update(.033)  # call the ball's update method with a dt of 0.033
            time.sleep( 0.033 ) # have the animation go at the same speed
            if win.checkKey() == 'q': # did the user type a 'q'?
                break
            if win.checkMouse(): # did the user click the mouse?
                break
        if ball.getPosition()[0]*ball.getScale()>win.getWidth() or win.getHeight()-ball.getPosition()[1]*ball.getScale()>win.getHeight():
            ball.setPosition(25,25)# reposition the ball to the center of the windo
            ball.setVelocity(random.randint(0,20), random.randint(0,20))# give it a random velocity     
        #     def collision(block,ball):
        #         '''if colliding, block is blue. Otherwise it is white'''
        #         dx=(block.getPosition()[0]-ball.getPosition()[0])  #block x center position-ball x center position
        #         dy=(block.getPosition()[1]-ball.getPosition()[1])  #block y center position-ball y center position
        #         if abs(dy)<=ball.getRadius()+block.getHeight()/2 and abs(dx)<=ball.getRadius()+block.getWidth()/2:   #if collide
        #             block.undraw()
        #     collision()
        win.close()
main()

    
    