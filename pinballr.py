"your file header here"


import graphicsPlus as gr
import physics_objectsr as pho
import random
import collision as col
#import time

def buildObstacles(win):
    # Create all of the obstacles in the scene and put them in a list
    
    block1 = pho.Block(win, 700, 550, width=50,height=50, color=(150,70,0)) #brown
    block2 = pho.Block(win, 400, 400,width=25,height=250, color=(0,0,0))  #black
    block3 = pho.Block(win, 700, 400, width=150,height=15, color=(100,100,0))   #green
    block4 = pho.Block(win, 140, 400, width=85, height=65, color=(255,69,0))  #red
    trinagle=pho.Triangle(win, 50,30,width=90,height=15,color=(0,0,0))
    #trinagle.setPosition(30,30)

    #triangle1 = pho.Triangle(win, 250, 200, 80, 80, color = (255,69,0))
    #triangle2 = pho.Triangle(win, 350, 50, 80, 80, color = (102,0,204))
    # Each obstacle should be a Thing (e.g. Ball, Block, other)
    # You might want to give one or more the obstacles an elasticity > 1
    Things = [block1, block2, block3, block4]
    return Things
    # Return the list of Things




def main():

    win = gr.GraphWin( 'Ping Pong', 500, 500, False )
    print('win created')

    # call buildObstacles, storing the return list in a variable (e.g. shapes)
    shapes = buildObstacles(win)
    # loop over the shapes list and have each Thing call its draw method
    for item in shapes:
        item.draw()  
    # assign to dt the value 0.02
    dt = .02
    # assign to frame the value 0
    frame = 0
    print('create shapes')

    # create a (yellow) ping pong ball, give it an initial velocity and acceleration, and draw it
    ball = pho.Ball(win, 2, 90, 50, (255,255,0))
    ball.setVelocity(20,20)
    ball.setAcceleration(0,-10)

    ball.draw()
    print('draw ping pong ball')

    # start an infinite loop
    while True:
        # if frame modulo 10 is equal to 0
        if frame %10 == 0:
            # call win.update()
            win.update()
        # using checKey, if the user typed a 'q' then break
        if win.checkKey() == "q":
            break
        #time.sleep(1200)
        # if the ball is out of bounds, re-launch it

        
        if ball.getPosition()[1] < 0 or ball.getPosition()[1] > 50 or ball.getPosition()[0] < 0 or ball.getPosition()[0] > 50:
            ball.setPosition(7, 25)
            ball.setVelocity(1,1)
            ball.setAcceleration(1,1)

        
        collided = False
        #print(collided)
       
        # for each item in the shapes list
        for item in shapes:
            # if the result of calling the collision function with the ball and the item is True
            if col.collision(ball, item, dt):
                # set collided equal to True
                collided = True
                print(item, 'collided with ball')

            # if collided is equal to False
        if collided == False:
                # call the update method of the ball with dt as the time step
                ball.update(dt)
        
        # increment frame
        frame += 1 # I moved this into the for loop

    win.checkMouse()
    # close the window
    win.close()

if __name__ == "__main__":
    main()



##def main():
##    # create a GraphWin
##    win = gr.GraphWin( 'ping pong', 500, 500, False )
##    obstacles=buildObstacles(win)# call buildObstacles, storing the return list in a  variable (e.g. shapes)
##    for i in obstacles:
##        i.draw(win)# loop over the shapes list and have each Thing call its draw method
##    dt=.02#assign to dt the value 0.02
##    frame=0# assign to frame the value 0
##    mainball=Ball(win)# create a ball, give it an initial velocity and acceleration, and draw it
##    mainball.setAcceleration(5,7)
##    mainball.setVelocity(9,7)
##    mainball.draw()
    
##    while True:# start an infinite loop
##        if frame % 10==0:# if frame modulo 10 is equal to 0
##            win.update()# call win.update()
##        if win.checkKey() != "q":   ## using checKey, if the user typed a 'q' then break
##            break
##        # if the ball is out of bounds, re-launch it
##        if mainball.getPosition()[0]*mainball.getScale()>win.getWidth() or win.getHeight()-mainball.getPosition()[1]*mainball.getScale()>win.getHeight():
##            '''ball does not collide, but goes to out of bounds falling+recenters'''
##            mainball.setPosition(25,25)# reposition the ball to the center of the windo
##            mainball.setVelocity(random.randint(0,20), random.randint(0,20))# give ball a random velocity  
##        collided=False# assign to collided the value False
##        for i in obstacles:# for each item in the shapes list
##            if collision.collision_router[('ball',mainball.getType())]==True:# if the result of calling the collision function with the ball and the item is True
##                collided=True# set collided to True
##        if collided==False:# if collided is equal to False
##            mainball.update(dt)# call the update method of the ball with dt as the time step
##        frame+=1# increment frame
##    win.close()# close the windowww
##if __name__ == "__main__":
##    main()
##    
