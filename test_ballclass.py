'''Harsha Somaya
11/3/2021
CS152
lab8
simulate two balls colliding
change directory to project 8 and run py.test_ballclass.py to call
'''
# Bruce Maxwell
# Fall 2015
# CS 151S Project 9
#
# ball class test
#
# modified slightly by Eric Aaron for CS 152, Spring '19
# slightly updated by Bruce Maxwell for CS 152, Fall 2019
# simplified the constructor call to just the win variable
# update F2021 by Stacy Doore

import graphicsPlus as gr
import physics_objects as pho
import collision as coll
import time

# create two balls heading towards one another
def main():
    win = gr.GraphWin( 'balls colliding', 500, 500, False )

    ball1 = pho.Ball( win )
    ball2 = pho.Ball( win )
    ball1.setPosition( 0, 0 )
    ball2.setPosition( 30, 20 )
    print("set ball1 position = (0 ,0)")
    print("set ball2 position = (30 ,20)")
    ball1.draw()
    ball2.draw()
    # Block = pho.Block( win )
    # Block.setPosition( 30, 20 )
    # Block.draw()

##    Triangle = pho.Triangle( win )
##    Triangle.setPosition( 10, 20 )
##    Triangle.draw()
    # set up velocity and acceleration so they collide
    ball1.setVelocity( 20, 37 )  
    ball2.setVelocity( -20, 20 )
    ball1.setAcceleration( 0, -20 )
    ball2.setAcceleration( 0, -20 )
    # #ball1.draw()
    # #ball2.draw()
    print("drawing ball1 and ball2")
    # loop for some time and check for collisions
    dt = 0.01
    for frame in range(120):
        if not coll.collision_ball_ball( ball1, ball2, dt ):  #if not colliding
            ball1.update(dt)  #update ball1 position and velocity
        if not coll.collision_ball_ball( ball2, ball1, dt ):
            ball2.update(dt)
        if frame % 10 == 0:  #for every number divisble by 10
            win.update()   #update window
        time.sleep(0.5*dt)   #stops the porgram and waits for .5*dt seconds
        if win.checkMouse() != None:   #if i click
            break
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
