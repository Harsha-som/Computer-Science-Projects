'''Harsha Somaya
11/2/2021
CS152
lab7
create a ball colliding with block at bottom or top and regenrates. Bottom block dispaeers upon hit
change directory to project 7 and run py.testfile11.py to call
'''

import graphicsPlus as gr
import physics_objects as pho
import random
import time


def main():
    '''create ball, 2 blocks, and change ball moeemnt when colling'''
    win = gr.GraphWin("Falling", 500, 500, False)
    ball = pho.Ball(win)
    ball.setPosition(100,100)
    ball.setVelocity(random.randint(0,20), random.randint(0,20))# give it a random velocity
    ball.setAcceleration(0,-20)# set the acceleration to (0, -20)
    ball.draw()
    block = pho.Block( win, dx = 20, dy = 3 )  # make a block
    block.setPosition(25, 5)  #block at screen center
    block.draw()
    blockt = pho.Block( win, dx = 20, dy = 3 )  # make a block
    blockt.setPosition(25, 30)  #block at screen center
    blockt.draw()
    while True:
        ball.update(.033)  # call the ball's update method with a dt of 0.033
        time.sleep( 0.033 ) # have the animation go at the same speed
        self=block
        dx=(self.getPosition()[0]-ball.getPosition()[0])  #block x center position-ball x center position
        dy=(self.getPosition()[1]-ball.getPosition()[1])  #block y center position-ball y center position
        dx1=(blockt.getPosition()[0]-ball.getPosition()[0])  #blockt x center position-ball x center position
        dy1=(blockt.getPosition()[1]-ball.getPosition()[1])  #blockt y center position-ball y center position
        if abs(dy)<=ball.getRadius()+self.getHeight()/2 and abs(dx)<=ball.getRadius()+self.getWidth()/2:
            '''if hit bottom block, bottom block undraw and ball reset to center'''
            block.undraw()  #block undrawn if collising
            ball.setPosition(25,25)# reposition the ball to the center of the window
            ball.setVelocity(random.randint(0,20), random.randint(0,20))# give ball a random velocity 
        if abs(dy1)<=ball.getRadius()+blockt.getHeight()/2 and abs(dx1)<=ball.getRadius()+blockt.getWidth()/2:   #if colling
            '''if hits top block, respawn ball at center'''
            blockt.vis[0].setFill("purple")
            ball.setPosition(25,25) #reposition the ball to the center of the window
            ball.setVelocity(random.randint(0,20), random.randint(0,20))# give ball a random velocity
        else:
            '''so default for top block is white. If it is hit it goes to purple though'''
            blockt.vis[0].setFill("white")

        if ball.getPosition()[0]*ball.getScale()>win.getWidth() or win.getHeight()-ball.getPosition()[1]*ball.getScale()>win.getHeight():
            '''ball does not collide, but goes to bottom falling+recenters'''
            ball.setPosition(25,25)# reposition the ball to the center of the windo
            ball.setVelocity(random.randint(0,20), random.randint(0,20))# give ball a random velocity         
        if win.checkKey() == 'q': # did the user type a 'q'?
            break
        if win.checkMouse(): # did the user click the mouse?
            break  
    win.close()
main()

    
    