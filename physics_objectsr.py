'''Harsha Somaya
11/3/2021
CS152
lab8

change directory to project 8 and run py.wordmap.py to call
'''
# you need to separate your function by 2 lines to make it easier for someone to read your code
#from tkinter import Scale
import graphicsPlus as gr
import time
import random
import collision as collision

class Thing: #the parent class for simulated objects.
    def __init__(self,win,the_type):
        self.win=win
        self.type=the_type
        self.mass=1
        
        
        self.position = [0,0]
        self.velocity=[0,0]
        self.acceleration=[0,0]
        self.elasticity=.5
        self.scale=10
        self.vis=[]
        self.color=(0,0,0)
        self.drawn=False

    #Thing getters and setters

    def getPosition(self):
        ''' returns a 2-element tuple with the x, y position of self.'''
        return (self.position[0],self.position[1])


    def getVelocity(self):
        '''returns a 2-element tuple with the x and y velocities of self.'''
        return (self.velocity[0],self.velocity[1])


    def setVelocity(self, vx, vy):
        '''vx and vy are the new x and y velocities f object self'''
        self.velocity[0]=vx
        self.velocity[1]=vy  #set current velocty in x to vx
        return


    def setElasticity(self,elastic):
        self.elasticity=elastic
        return


    def getAcceleration(self): 
        '''returns a 2-element tuple with the x and y acceleration values of object self'''
        return (self.acceleration[0],self.acceleration[1])


    def setPosition(self,px,py):
        '''set position of self to px and py and then move it'''
        self.position[0]=px# assign to the x coordinate in self.pos the new x coordinate
        self.position[1]=py 
        for i in self.vis:
            # dx=self.scale*(px-self.position[0])
            # dy=-self.scale*(px-self.position[1])
            c=i.getCenter()  #center of object
            dx=self.scale*px-c.getX()  #currnet x position*10-center x
            dy=self.win.getHeight()-(self.scale*py)-c.getY()  #window height-currnet y position*10-center 
            i.move(dx,dy)  #move to new position


    def setAcceleration(self, ax, ay): 
        '''ax and ay are new x and y accelerations. of object self returned'''
        self.acceleration[0]=ax
        self.acceleration[1]=ay
        return


    def getMass(self): 
        '''Returns the mass of the object/self as a scalar value'''
        return self.mass  #return mass


    def setMass(self, m): 
        '''is the new mass of the object/self'''
        self.mass = m
        return


    def getcolor(self):
        return self.color


    def setColor(self,c):# takes in an (r, g, b) tuple
        self.color=c
        if c !=None:  #if has a color
            visList = self.vis
            for i in visList:
                i.setFill(gr.color_rgb(c[0], c[1], c[2]))

    def getScale(self):
        '''return sclae of object self'''
        return self.scale  #scale is 10


    def getElasticity(self):
        return self.elasticity


    def getType(self):
        return self.type

    def update(self, dt):
        '''update the object's velocity and position with timee dt'''
        x_old=self.position[0]# assign to x_old the current x position
        y_old=self.position[1]# assign to y_old the current y position
        
        self.position[0]=x_old+ self.velocity[0]*dt + 0.5*self.acceleration[0]* dt*dt# update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[1]=y_old +self.velocity[1]*dt + 0.5*self.acceleration[1]* dt*dt # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 

        # dx=(self.velocity[0]*dt)*self.scale
        # dy=(self.velocity[1]*dt)*-self.scale

        dx=(self.position[0]-x_old)*self.scale  #new x position-old times scale
        dy=(self.position[1]-y_old)*-self.scale

        for  item in self.vis:  
            item.move(dx,dy)# call the move method of the graphics object with dx and dy as arguments..

        #I changed this slightly
        self.velocity[0] = self.velocity[0] + self.acceleration[0] * dt
        self.velocity[1] = self.velocity[1] + self.acceleration[1] * dt

        return


    def draw(self):
        '''draw every object in list to window, meaning drawn=True'''
        for item in self.vis:
            item.draw(self.win)
            self.drawn=True

    def undraw(self): 
        '''undraw every object in list to windoww'''
        for i in self.vis:
            i.undraw()
            self.drawn=False  #just undrawed, so self.drawn=False b/c window emplty

class Ball(Thing):
    def __init__(self, win, radius= 10, x0 = 0, y0 = 0, c = (0,0,0)):
        Thing.__init__(self,win,"ball")  #inherit thing class
        self.position = [x0, y0]
        self.radius=radius
        self.refresh(win)
        self.setColor(c)
        self.elasticity = 1
        print("i am a ball")
        
    def getcolor(self):
        return self.color
    
    def getRadius(self): 
        '''Returns the radius of the Ball as a scalar value'''
        return self.radius  #recursive function
    
    def refresh(self,win):
        '''undraw the shapes an then redraw accordingly'''
        drawn=self.drawn
        if drawn:   #if self.drawn=True
            self.undraw()   #undraw, so self.drawn=False
        self.vis=[gr.Circle(gr.Point(self.position[0]*self.scale, win.getHeight()-self.position[1]*self.scale),self.radius * self.scale )]  #list of x center coordinate times 10, window height-y coordinate*10,radius*10    
        if drawn: #if self.drawn=True, which shoud be false now because line 118 
            self.draw()  #took out win 

    def setRadius(self,r):
        self.radius=r
        self.refresh(win)
    

class Block(Thing):
    def __init__(self, win,x0=0,y0=0,width=2,height=1, color=(0,0,0)):
        Thing.__init__(self,win,"block")
        # self.dx=dx
        # self.dy=dy
        self.width=width
        self.height=height
        self.position = [x0,y0]
        self.reshape(win)
        self.setColor(color)
        print('i am a block')

    def draw(self):
        vislist=self.vis
        for i in vislist:
            i.draw(self.win)

    def undraw(self): # SD added this to undraw shape
        visList = self.vis 
        for item in visList:
            item.undraw()

    def reshape(self, win):
        '''undraw teh graphics obects if drawn and then redraw'''
        drawn = self.drawn
        if drawn:
            self.undraw()
        #self.vis = [gr.Rectangle(gr.Point((self.position[0]-(self.width/2))* self.scale, win.getHeight() - (self.position[1]-(self.height/2))* self.scale, gr.Point((self.position[0]+(self.width/2))* self.scale, win.getHeight() - (self.position[1]+(self.height/2))* self.scale)))]
        self.vis = [gr.Rectangle(gr.Point((self.position[0]-self.width)/2, (self.position[1]-self.height)/2), gr.Point((self.position[0]+self.width)/2, (self.position[1]+self.height)/2))]
        if drawn:
            self.draw()
            

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height  #return height of object (blcok)

    def setwidth(self,dx1):
        self.width=dx1
        #self.reshape()  #undraw the obejcts if drawn and then redraw
        return
    
    def setheight(self,dy):
        self.height=dy
        #self.reshape()   #undraw the obejcts if drawn and then redraw
        return
    
class Triangle(Thing):
    def __init__(self,win,x0 = 0, y0 = 0, width = 2, height = 1, color = (0,0,0)):
        Thing.__init__(self,win,"triangle")
        self.width=width
        self.height=height
        self.position = [x0,y0]
        self.elasticity = 1.5
        self.reshape(win)
        self.setColor(color)
        print('i am a triangle')

    def draw(self): # draws shape
        visList = self.vis
        for item in visList:
            item.draw(self.win)

    def undraw(self): # undraws shape
        visList = self.vis 
        for item in visList:
            item.undraw()
        
    def reshape(self,win):
        '''undraw teh graphics obects if drawn and then redraw'''
        drawn = self.drawn
        if drawn:
            self.undraw()
        self.vis = [gr.Polygon(gr.Point(self.position[0]-(self.width/2),self.position[1]-(self.height/2)),gr.Point(self.position[0]+(self.width/2),self.position[1]-(self.height/2)), gr.Point(self.position[0],self.position[1]+(self.height/2)))]
        if drawn:
            self.draw()

    def getWidth(self): # gets width
        return self.width

    def getHeight(self): # gets height
        return self.width

    def setWidth(self, dx): # sets width
        self.width = dx
        return

    def setHeight(self, dy): # sets height
        self.height = dy
        return







