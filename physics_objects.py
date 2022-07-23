import graphicsPlus as gr
import time
import random
'''Harsha Somaya
11/2/2021
CS152
lab7
create a class of ball and block and that follow kinetamatics motion
change directory to project 7 and run py.physics_objects.py to call
'''
class Ball:
    def __init__(self, win):
        '''make ball and then later change its movement'''
        self.mass = 1 
        self.radius = 1
        self.pos =[0, 0]  #inital conditons
        self.velocity =[0, 0]
        self.accelaration = [0, 0]
        self.win = win
        self.scale = 10      
        self.vis = [gr.Circle(gr.Point(self.pos[0]*self.scale, win.getHeight()-self.pos[1]*self.scale),self.radius * self.scale )]  #list of x center coordinate times 10, window height-y coordinate*10,radius*10    
        print(self.vis)  
    def getPosition(self):
        ''' returns a 2-element tuple with the x, y position of self.'''
        return (self.pos[0],self.pos[1])
    def setPosition(self, px, py): 
        '''px and py are the new x,y values of object self returned as output'''
        self.pos[0]=px# assign to the x coordinate in self.pos the new x coordinate
        self.pos[1]=py 
        for i in self.vis:
            c=i.getCenter()  #center of i
            dx=self.scale*px-c.getX()  #10*current x position-center x
            dy=self.win.getHeight()-(self.scale*py)-c.getY()
            i.move(dx,dy) # call the move method of the item, passing in dx and dy
    def getVelocity(self):
        '''returns a 2-element tuple with the x and y velocities of self.'''
        return (self.velocity[0],self.velocity[1])
    def setVelocity(self, vx, vy):
        '''vx and vy are the new x and y velocities f object self'''
        self.velocity[0]=vx
        self.velocity[1]=vy  #set current velocty in x to vx
        return self.velocity
    def getAcceleration(self): 
        '''returns a 2-element tuple with the x and y acceleration values of object self'''
        return (self.accelaration[0],self.accelaration[1])
    def setAcceleration(self, ax, ay): 
        '''ax and ay are new x and y accelerations. of object self returned'''
        self.accelaration[0]=ax
        self.accelaration[1]=ay
        return self.accelaration
    def getMass(self): 
        '''Returns the mass of the object/self as a scalar value'''
        return self.mass  #return mass
    def setMass(self, m): 
        '''is the new mass of the object/self'''
        m=self.mass
    def getScale(self):
        '''return sclae of object self'''
        return self.scale  #scale is 10
    def getRadius(self): 
        '''Returns the radius of the Ball as a scalar value'''
        return self.radius  #recursive function
    def update(self, dt):
        '''update the objects/self velocity and position with time dt'''
        x_old=self.pos[0]# assign to x_old the current x position
        y_old=self.pos[1]# assign to y_old the current y position
        self.pos[0]=x_old+(self.velocity[0]*dt + 0.5*self.accelaration[0]* dt*dt)# update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.pos[1]=y_old +self.velocity[1]*dt + 0.5*self.accelaration[1]* dt*dt # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        dx=(self.velocity[0]*dt)*self.scale
        dy=(self.velocity[1]*dt)*-self.scale
        for  item in self.vis:   
            item.move(dx,dy)# call the move method of the graphics object with dx and dy as arguments..
        self.velocity[0]=self.accelaration[0]*dt+self.velocity[0]# update the x velocity by adding the acceleration times dt to its old value
        self.velocity[1]=self.accelaration[1]*dt+self.velocity[1]# update the y velocity by adding the acceleration times dt to its old value    
        return self
    def draw(self):
        '''draw every object in list to window'''
        for i in self.vis:
            i.draw(self.win) 
 
class Block:
    '''make new class block'''
    def __init__(self,win,dx,dy):
        '''initalize object with window and length of x-dx-a dn length of y-dy'''
        self.win = win
        self.dx=dx
        self.dy=dy
        self.velocity=[0,0]
        self.position=[0,0]
        self.width=0  #inital conditions
        self.height=0
        self.scale=10
        self.accelaration=[0,0]
        self.vis = [gr.Rectangle(gr.Point((self.position[0]-dx/2)*self.scale,win.getHeight()-((self.position[1]-dy)/2)*self.scale),gr.Point((self.position[0]+dx/2)*self.scale,win.getHeight()-(self.position[1]+dy/2)*self.scale))]
    def draw(self):
        '''draw every object in list to window'''
        for item in self.vis:
            item.draw(self.win)  #draw
    def undraw(self): 
        '''undraw every object in list to window'''
        for i in self.vis:
            i.undraw()
    def getPosition(self):
        ''' returns a 2-element tuple with the x, y position of self.'''
        return self.position[0],self.position[1]
    def setPosition(self,px,py):
        '''set position of self to px and py and then move it'''
        self.position[0]=px# assign to the x coordinate in self.pos the new x coordinate
        self.position[1]=py 
        for i in self.vis:
            c=i.getCenter()  #center of object
            dx=self.scale*px-c.getX()  #currnet x position*10-center x
            dy=self.win.getHeight()-(self.scale*py)-c.getY()  #window height-currnet y position*10-center y
            i.move(dx,dy)  #move to new position
    def getVelocity(self): 
        '''returns a 2-element tuple with the x and y velocities of self.'''
        return (self.velocity)
    def setVelocity(self, vx, vy): 
        '''vx and vy are the new x and y velocities of object self'''
        self.velocity[0]=vx
        self.velocity[1]=vy
        return self.velocity
    def getAcceleration(self): 
        '''returns a 2-element tuple with the x and y acceleration values. of object self'''
        return (self.accelaration)
    def setAcceleration(self, ax, ay): 
        '''ax and ay are new x and y accelerations. of object self'''
        self.accelaration[0]=ax
        self.accelaration[1]=ay
        return self.accelaration
    def getWidth(self): 
        '''Returns the width/  a scalar value'''
        return self.dx
    def getHeight(self): 
        '''Returns the height/  a scalar value'''
        return self.dy
    def update(self, dt):
        '''update the objects/self velocity and position with time dt'''
        x_old=self.position[0]# assign to x_old the current x position
        y_old=self.position[1]# assign to y_old the current y position
        self.position[0]=x_old+(self.velocity[0]*dt + 0.5*self.accelaration[0]* dt*dt)# update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[1]=y_old +self.velocity[1]*dt + 0.5*self.accelaration[1]* dt*dt # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 
        dx=(self.velocity[0]*dt)*self.scale
        dy=(self.velocity[1]*dt)*-self.scale
        for  item in self.vis:  
            item.move(dx,dy)# call the move method of the graphics object with dx and dy as arguments..
        self.velocity[0]=self.accelaration[0]*dt+self.velocity[0]# update the x velocity by adding the acceleration times dt to its old value
        self.velocity[1]=self.accelaration[1]*dt+self.velocity[1]# update the y velocity by adding the acceleration times dt to its old value
        return self
    def collision(self, ball):
        '''if colliding, block is blue. Otherwise it is white'''
        dx=(self.getPosition()[0]-ball.getPosition()[0])  #block x center position-ball x center position
        dy=(self.getPosition()[1]-ball.getPosition()[1])  #block y center position-ball y center position
        if abs(dy)<=ball.getRadius()+self.getHeight()/2 and abs(dx)<=ball.getRadius()+self.getWidth()/2:   #if colling
            self.vis[0].setFill("blue")  #block is blue
            
            return True
        else:
            self.vis[0].setFill("white")
            return False

    
