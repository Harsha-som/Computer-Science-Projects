'''Harsha Somaya
11/3/2021
CS152
lab8
ccreate a pinball machine with objects
change directory to project 8 and run py.wordmap.py to call
'''
from tkinter import Scale
import graphicsPlus as gr
import time
import random
import collision as collision

# class Thing: #the parent class for simulated objects.
#     def __init__(self,win,the_type):
#         self.win=win
#         self.type=the_type
#         self.mass=5
#         self.position=[30,20]
#         self.velocity=[1,3]
#         self.acceleration=[7,8]
#         self.elasticity=1
#         self.scale=10
#         self.vis=[]
#         self.color=(0,0,0)
#         self.drawn=False
#         self.center=(0,0)
#     def getPosition(self):
#         ''' returns a 2-element tuple with the x, y position of self.'''
#         return self.position[:]
#     def getVelocity(self):
#         '''returns a 2-element tuple with the x and y velocities of self.'''
#         return self.velocity[:]
#     def setVelocity(self, vx, vy):
#         '''vx and vy are the new x and y velocities f object self'''
#         self.velocity[0]=vx
#         self.velocity[1]=vy  #set current velocty in x to vx
#         return 
#     def setElasticity(self,elastic):
#         self.elasticity=elastic
#         return 
#     def getAcceleration(self): 
#         '''returns a 2-element tuple with the x and y acceleration values of object self'''
#         return self.acceleration[:]
#     def setPosition(self,px,py):
#         '''set position of self to px and py and then move it'''
#         self.position[0]=px# assign to the x coordinate in self.pos the new x coordinate
#         self.position[1]=py 
#         for i in self.vis:
#             # dx=self.scale*(px-self.position[0])
#             # dy=-self.scale*(px-self.position[1])
#             c=self.center  #center of object
#             dx=self.scale*px-c.getX()  #currnet x position*10-center x
#             dy=self.win.getHeight()-(self.scale*py)-c.getY()  #window height-currnet y position*10-center 
#             i.move(dx,dy)  #move to new position
#         return self.position
#     def setAcceleration(self, ax, ay): 
#         '''ax and ay are new x and y accelerations. of object self returned'''
#         self.acceleration[0]=ax
#         self.acceleration[1]=ay
#         return self.acceleration
#     def getMass(self): 
#         '''Returns the mass of the object/self as a scalar value'''
#         return self.mass  #return mass
#     def setMass(self, m): 
#         '''is the new mass of the object/self'''
#         self.mass=m
#     def getcolor(self):
#         return self.color
#     def setColor(self,c):# takes in an (r, g, b) tuple
#         self.color=c
#         if c !=None:  #if has a color
#             visList = self.vis
#             for i in visList:
#                 i.setFill(c)
#     def getScale(self):
#         '''return sclae of object self'''
#         return self.scale  #scale is 10
#     def getElasticity(self):
#         return self.elasticity
#     def getType(self):
#         return self.type
#     def update(self, dt):
#         #print("in update")
#         '''update the object's velocity and position with timee dt'''
#         x_old=self.position[0]# assign to x_old the current x position
#         y_old=self.position[1]# assign to y_old the current y position
#         self.position[0]=x_old+(self.velocity[0]*dt + 0.5*self.acceleration[0]* dt*dt)# update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
#         self.position[1]=y_old +self.velocity[1]*dt + 0.5*self.acceleration[1]* dt*dt # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
#         # dx=(self.velocity[0]*dt)*self.scale
#         # dy=(self.velocity[1]*dt)*-self.scale
#         dx=(self.position[0]-x_old)*self.scale  #new x position-old times scale
#         dy=(self.position[1]-y_old)*-self.scale
#         for  item in self.vis:  
#             item.move(dx,dy)# call the move method of the graphics object with dx and dy as arguments..
#         self.velocity[0] = self.velocity[0] + self.acceleration[0] * dt
#         self.velocity[1] = self.velocity[1] + self.acceleration[1] * dt# update the y velocity by adding the acceleration times dt to its old value
#         return 
#     def draw(self):
#         '''draw every object in list to window, meaning drawn=True'''
#         if self.drawn==False:
#             for item in self.vis:
#                 item.draw(self.win)
#                 print(item, "x")
#             self.drawn=True 
#     def undraw(self): 
#         '''undraw every object in list to windoww'''
#         for i in self.vis:
#             i.undraw()
#             self.drawn=False  #just undrawed, so self.drawn=False b/c window emplty

# class Ball(Thing):
#     def __init__(self, win, radius=3, x0 =0, y0 =0 ,c= gr.color_rgb(130, 0, 130)):
#         Thing.__init__(self,win,"ball")  #inherit thing class
#         self.radius=radius
#         self.refresh()
#         self.setColor(c)
#         self.position=[x0,y0]
#         self.center=self.vis[0].getCenter()
#         self.elasticity=1
#     def getcolor(self):
#         return self.color
#     def getRadius(self): 
#         '''Returns the radius of the Ball as a scalar value'''
#         return self.radius  #recursive function
#     def refresh(self):
#         drawn=self.drawn
#         if drawn:   #if self.drawn=True
#             self.undraw()   #undraw, so self.drawn=False
#         self.vis=[(gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-self.position[1]*self.scale),self.radius * self.scale) )]  #list of x center coordinate times 10, window height-y coordinate*10,radius*10    
#         if drawn: #if self.drawn=True, which shoud be false now because line 118 
#             self.draw()   
#     def setRadius(self,r):
#         self.radius=r
#         self.refresh()
#     def draw(self):
#         vislist=self.vis
#         for i in vislist:
#             i.draw(self.win)
#         self.drawn=True
#     def undraw(self): # SD added this to undraw shape
#         visList = self.vis 
#         for item in visList:
#             item.undraw()
#         self.drawn=False

# class Block(Thing):
#     def __init__(self, win,x0=0,y0=0,width=25,height=30, color="black"):
#         Thing.__init__(self,win,"block")
#         self.width=width
#         self.height=height
#         self.position=[x0,y0]
#         self.reshape(win)
#         self.setColor(color)
#     def reshape(self, win):
#         '''undraw teh graphics obects if drawn and then redraw teh new shapes'''
#         local=self.drawn
#         print(local, "local")
#         if local:
#             print("first if")
#             self.undraw()
#         self.vis = [gr.Rectangle(gr.Point((self.position[0]-self.width)/2, (self.position[1]-self.height)/2), gr.Point((self.position[0]+self.width)/2, (self.position[1]+self.height)/2))]
#         if local:
#             print("second if")
#             self.draw()
#         self.center=self.vis[0].getCenter()
#     def getWidth(self):
#         return self.width
#     def getHeight(self):
#         return self.height  #return height of object (blcok)
#     def setwidth(self,dx1):
#         self.width=dx1
#         self.reshape()  #undraw the obejcts if drawn and then redraw
#     def setheight(self,dy):
#         self.height=dy
#         self.reshape()   #undraw the obejcts if drawn and then redraw
#     def draw(self):
#         vislist=self.vis
#         for i in vislist:
#             i.draw(self.win)
#         self.drawn=True
#     def undraw(self): # SD added this to undraw shape
#         visList = self.vis 
#         for item in visList:
#             item.undraw()
#         self.drawn=False

# class Triangle(Thing):
#     def __init__(self,win,width,height,x0,y0):
#         Thing.__init__(self,win,"triangle")
#         self.width=width
#         self.height=height
#         self.reshape()
#         self.setColor(c="purple")
#         self.center=gr.Point(width/2,height/2)
#         self.position=[x0,y0]
#     def getWidth(self):
#         return self.width
#     def getHeight(self):
#         return self.height
#     def reshape(self):
#         '''undraw teh graphics obects if drawn and then redraw'''
#         drawn = self.drawn
#         if drawn:
#             self.undraw()
#         self.vis = [gr.Polygon(gr.Point(self.position[0]-(self.width/2),self.position[1]-(self.height/2)),gr.Point(self.position[0]+(self.width/2),self.position[1]-(self.height/2)), gr.Point(self.position[0],self.position[1]+(self.height/2)))]
#         if self.drawn:
#             self.draw()
# def buildObstacles(win):
#     # Create all of the obstacles in the scene and put them  in a list
#     block=Block(win,400, 700, width=40,height=70, color="pink")   
#     trinagle=Triangle(win, 50,200,x0=90,y0=50)
#     trinagle.setPosition(30,30)
#     ball=Ball(win)
#     ball.setPosition(30,30)
#     vis=[block,trinagle,ball]  # Each obstacle should be a Thing (e.g. Ball, Block, 
#     print("length of vis is", len(vis))
#     return vis # Return the list of Things

# def main():
#     # create a GraphWin
#     win1 = gr.GraphWin( 'ping pong', 500, 500, False )
#     obstacles=buildObstacles(win1)# call buildObstacles, storing the return list in a  variable (e.g. shapes)
#     for i in obstacles:
#         i.draw()# loop over the shapes list and have each Thing call its draw method
#         print("test,", i.drawn)
#     dt=.2#assign to dt the value 0.02
#     frame=0# assign to frame the value 0
#     mainball=Ball(win1, c="green")# create a ball, give it an initial velocity and acceleration, and draw it
#     mainball.setPosition(40,30)
#     mainball.setVelocity(random.randint(-5, 5), random.randint(-5, 5))
#     mainball.setAcceleration(random.randint(5, 100), random.randint(5, 100))
#     mainball.draw()
#     print("q",mainball.drawn)
#     mainball.setVelocity(random.randint(-5, 5), random.randint(-5, 5))
#     mainball.setAcceleration(random.randint(-5, 5), random.randint(-5, 5))
#     while True:# start an infinite loop
#         if frame % 10==0:# if frame modulo 10 is equal to 0
#             win1.update()# call win.update()
#         if win1.checkKey()== "q":   ## using checKey, if the user typed a 'q' then break
#             break
#         # if the ball is out of bounds, re-launch it
#         if mainball.getPosition()[1] < 0 or mainball.getPosition()[1] > 50 or mainball.getPosition()[0] < 0 or mainball.getPosition()[0] > 50:
#             '''ball does not collide, but goes to out of bounds falling+recenters'''
#             mainball.setPosition(25,45)# reposition the ball to the center of the windo
#             mainball.setVelocity(random.randint(0,20), random.randint(0,20))# give ball a random velocity  .
#             mainball.setAcceleration(random.randint(5, 10), random.randint(5, 10))
#         collided=False# assign to collided the value False
#         for i in obstacles:# for each item in the shapes list
#             if collision.collision(mainball,i,dt):# if the result of calling the collision function with the ball and the item is True
#                 collided=True# set collided to True
#             elif collided==False:# if collided is equal to False
#                 mainball.update(dt)# call the update method of the ball with dt as the time step
#         frame+=1# increment frame
#     win1.checkMouse()
#     win1.close()# close the windowww


# class Ball:
#     def __init__(self, win):
#         '''make ball and then later change its movement'''
#         self.mass = 1 
#         self.radius = 1
#         self.pos =[0, 0]  #inital conditons
#         self.velocity =[0, 0]
#         self.accelaration = [0, 0]
#         self.win = win
#         self.scale = 10      
#         self.vis = [gr.Circle(gr.Point(self.pos[0]*self.scale, win.getHeight()-self.pos[1]*self.scale),self.radius * self.scale )]  #list of x center coordinate times 10, window height-y coordinate*10,radius*10    
#         print(self.vis)  
#     def getPosition(self):
#         ''' returns a 2-element tuple with the x, y position of self.'''
#         return (self.pos[0],self.pos[1])
#     def setPosition(self, px, py): 
#         '''px and py are the new x,y values of object self returned as output'''
#         self.pos[0]=px# assign to the x coordinate in self.pos the new x coordinate
#         self.pos[1]=py 
#         for i in self.vis:
#             c=i.getCenter()  #center of i
#             dx=self.scale*px-c.getX()  #10*current x position-center x
#             dy=self.win.getHeight()-(self.scale*py)-c.getY()
#             i.move(dx,dy) # call the move method of the item, passing in dx and dy
#     def getVelocity(self):
#         '''returns a 2-element tuple with the x and y velocities of self.'''
#         return (self.velocity[0],self.velocity[1])
#     def setVelocity(self, vx, vy):
#         '''vx and vy are the new x and y velocities f object self'''
#         self.velocity[0]=vx
#         self.velocity[1]=vy  #set current velocty in x to vx
#         return self.velocity
#     def getAcceleration(self): 
#         '''returns a 2-element tuple with the x and y acceleration values of object self'''
#         return (self.accelaration[0],self.accelaration[1])
#     def setAcceleration(self, ax, ay): 
#         '''ax and ay are new x and y accelerations. of object self returned'''
#         self.accelaration[0]=ax
#         self.accelaration[1]=ay
#         return self.accelaration
#     def getMass(self): 
#         '''Returns the mass of the object/self as a scalar value'''
#         return self.mass  #return mass
#     def setMass(self, m): 
#         '''is the new mass of the object/self'''
#         m=self.mass
#     def getScale(self):
#         '''return sclae of object self'''
#         return self.scale  #scale is 10
#     def getRadius(self): 
#         '''Returns the radius of the Ball as a scalar value'''
#         return self.radius  #recursive function
#     def update(self, dt):
#         '''update the objects/self velocity and position with time dt'''
#         x_old=self.pos[0]# assign to x_old the current x position
#         y_old=self.pos[1]# assign to y_old the current y position
#         self.pos[0]=x_old+(self.velocity[0]*dt + 0.5*self.accelaration[0]* dt*dt)# update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
#         self.pos[1]=y_old +self.velocity[1]*dt + 0.5*self.accelaration[1]* dt*dt # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
#         dx=(self.velocity[0]*dt)*self.scale
#         dy=(self.velocity[1]*dt)*-self.scale
#         for  item in self.vis:   
#             item.move(dx,dy)# call the move method of the graphics object with dx and dy as arguments..
#         self.velocity[0]=self.accelaration[0]*dt+self.velocity[0]# update the x velocity by adding the acceleration times dt to its old value
#         self.velocity[1]=self.accelaration[1]*dt+self.velocity[1]# update the y velocity by adding the acceleration times dt to its old value    
#         return self
#     def draw(self):
#         '''draw every object in list to window'''
#         for i in self.vis:
#             i.draw(self.win)
             

WIDTH, HEIGHT = 500, 500
POSITION = gr.Point(250, 250)
RADIUS = 20
STEPS = 1
def MouseTracker(win, shape):
    '''make ball where i click on screen'''
    while True:
        if win.checkMouse():  #makes a black ball where i click
            shape.undraw()
            position = win.getMouse()
            center = shape.getCenter()
            xincr = (position.getX() - center.getX())
            yincr = (position.getY() - center.getY())
            #for _ in range(STEPS):
            shape.move(xincr, yincr)
            shape.setFill("pink")
            shape.draw(win)
        shapes=[]
        if win.checkKey()=="a":  #if i click a, create a blue circle
            circle=gr.Circle(gr.Point(random.randint(0,500),random.randint(0,500)), 10)
            circle.setFill("blue")
            circle.draw(win)
            shapes.append(circle)
        win.update()
        time.sleep(.033)
        for i in shapes:  #make the circles move
            dx=random.randint(-10,10)
            dy=random.randint(-3,2)
            i.move(dx,dy)
MouseTracker(win=gr.GraphWin("hi", WIDTH, HEIGHT),shape=gr.Circle(POSITION,RADIUS) )

 








