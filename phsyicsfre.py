'''Harsha Somaya
11/3/2021
CS152
lab8
create a ball/2 balls moing in pinball motion
change directory to project 8 and run py.phsyicsfre.py to call
'''
#from tkinter import Scale
import graphicsPlus as gr  #import libaries
import time
import random
import collision as collision

class Thing: #the parent class for simulated objects.
    def __init__(self,win,the_type):
        '''initalize all of the fields/attributes'''
        self.win=win
        self.type=the_type
        self.mass=1
        self.position = [170,250]  #in particular for triangle
        self.velocity=[0,0]
        self.acceleration=[0,0]
        self.elasticity=.2
        self.scale=10
        self.vis=[]
        self.color=(0,0,0)
        self.drawn=False

    #Thing getters and setters

    def getPosition(self):
        ''' returns a 2-element tuple with the x, y position of self.'''
        return self.position[:]
    def getVelocity(self):
        '''returns a 2-element tuple with the x and y velocities of self.'''
        return self.velocity[:]
    def setVelocity(self, vx, vy):
        '''vx and vy are the new x and y velocities f object self'''
        self.velocity[0]=vx
        self.velocity[1]=vy  #set current velocty in x to vx
        return
    def setElasticity(self,elastic):
        '''set the elasticity of the objects'''
        self.elasticity=elastic
        return
    def getAcceleration(self): 
        '''returns a 2-element tuple with the x and y acceleration values of object self'''
        return self.acceleration[:]
    def setPosition(self,px,py):
        '''set position of self to px and py and then move it'''
        self.position[0]=px# assign to the x coordinate in self.pos the new x coordinate
        self.position[1]=py 
        xold = self.position[0]
        yold = self.position[1]
        dx = (px - xold)*self.scale  #dx=new x -old x times scale
        dy = (py - yold)*-self.scale
        for i in self.vis:
            i.move(dx,dy)  #move to new position by dx,dy
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
        '''return the ojects's current color'''
        return self.color
    def setColor(self,c):
        '''set the object's color accoridng to c, which is a string or rgb tuple'''
        self.color=c
        if c !=None:  #if has a color
            visList = self.vis
            for i in visList:
                i.setFill(c)   #fill objects in visList/self.vis with the secified colors
        return
    def getScale(self):
        '''return sclae of object self'''
        return self.scale  #scale is 10
    def getElasticity(self):
        '''return elastciity of object self'''
        return self.elasticity
    def getType(self):
        '''return type of shape of object self'''
        return self.type
    def draw(self):
        '''draw every object in list to window, meaning drawn=True'''
        for item in self.vis:
            item.draw(self.win)
            self.drawn=True

    def undraw(self): 
        '''undraw every object in list to windoww'''
        for i in self.vis:
            i.undraw(self.win)
            self.drawn=False  #just undrawed, so self.drawn=False b/c window emplty

    def update(self, dt):
        '''update the object's velocity and position with timee dt'''
        x_old=self.position[0]# assign to x_old the current x position
        y_old=self.position[1]# assign to y_old the current y position
        
        self.position[0]=x_old+ self.velocity[0]*dt + 0.5*self.acceleration[0]* dt*dt# update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[1]=y_old +self.velocity[1]*dt + 0.5*self.acceleration[1]* dt*dt # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt 

        dx=(self.position[0]-x_old)*self.scale  #new x position-old times scale
        dy=(self.position[1]-y_old)*-self.scale

        for  item in self.vis:  
            item.move(dx,dy)# call the move method of the graphics object with dx and dy as arguments..
        self.velocity[0] = self.velocity[0] + self.acceleration[0] * dt
        self.velocity[1] = self.velocity[1] + self.acceleration[1] * dt
        return

class Ball(Thing):
    '''create child class ball'''
    def __init__(self, win, radius= 3.2, x0 = 25, y0 = 60, c= "orange"):
        Thing.__init__(self,win,"ball")  #inherit thing class
        self.setPosition(x0,y0)
        self.radius=radius
        self.refresh()  #will reshape/update the ball
        self.setColor(c)
        self.elasticity = .2  #elasticty
        print("i am a ball")  #so i know ball is printing
        
    def getRadius(self): 
        '''Returns the radius of the Ball as a scalar value'''
        return self.radius   
    def refresh(self):
        '''undraw the shapes an then redraw accordingly'''
        drawn=self.drawn
        if drawn:   #if self.drawn=True
            self.undraw()   #undraw, so self.drawn=False
        self.vis=[gr.Circle(gr.Point(self.position[0]*self.scale,self.win.getHeight()-self.position[1]*self.scale),self.radius * self.scale )]  #list of x center coordinate times 10, window height-y coordinate*10,radius*10    
        if drawn: #if self.drawn=True, which shoud be false now 
            self.draw()  
    def setRadius(self,r):
        '''set radius of ball again'''
        self.radius=r
        self.refresh()
   
    
class Block(Thing):
    '''create block parent class'''
    def __init__(self, win,x0=0,y0=0,width=2,height=1, color=(0,0,0)):
        '''initalize ball fields'''
        Thing.__init__(self,win,"block")  #child class of thing
        self.position[0] = x0
        self.position[1] = y0
        self.width=width   #initalize width
        self.height=height
        self.reshape()  #use this to reshape the block
        self.setColor(color)
        print('i am a block')   

    def reshape(self):   
        '''undraw teh graphics obects if drawn and then redraw'''
        drawn = self.drawn
        if drawn:
            self.undraw()  #from parent class thing
        self.vis = [gr.Rectangle(gr.Point(self.position[0]-(self.width*self.scale)/2, self.win.getHeight()-self.position[1]-(self.height*self.scale)/2), gr.Point(self.position[0]+(self.width*self.scale)/2, self.win.getHeight() - self.position[1]+(self.height*self.scale)/2))]
        if drawn:
            self.draw()  

    def getWidth(self):
        '''return width of block specifically'''
        return self.width

    def getHeight(self):
        '''return height of block specifically'''
        return self.height  

    def setwidth(self,dx1):
        '''set width accoridng to dx1'''
        self.width=dx1
        self.reshape()  
        return
    
    def setheight(self,dy):
        '''set height accoridng to dy'''
        self.height=dy
        self.reshape()  #undraw teh graphics obects if drawn and then redraw
        return
    
class Triangle(Thing):
    '''initalize triangle objects'''
    def __init__(self,win,width,height,c,x0=250,y0=250,radius=5):
        Thing.__init__(self,win,"triangle")  #inherited thing class
        self.width=width
        self.radisfromcenter = radius  #will serve as radius
        self.height=height
        self.reshape()  #reshape the object 
        self.position[0] = x0  #set positon to x0
        self.position[1] = y0
        self.setColor(c)
        print('i am a triangle')

    def get_radius(self):
        '''returns the current distance from center of the tiangle to the vertices'''
        return self.radisfromcenter  
    def set_radius(self, r):
        '''redraw with radius r'''
        self.radisfromcenter = r
        self.redefine()
    def reshape(self):
        '''reshape  triangle vertice with  updated self.vis '''
        win = self.win  #local vairbales to save typeing space in self.vis
        drawn = self.drawn
        pos = self.position
        if drawn:  #if anything is drawn, undraw
            self.undraw()
        self.vis = [gr.Polygon(gr.Point(pos[0]-(self.radisfromcenter*self.scale), win.getHeight()-(pos[1]-(self.radisfromcenter*self.scale))), gr.Point(pos[0]+(self.radisfromcenter*self.scale), win.getHeight()-(pos[1]-(self.radisfromcenter*self.scale))), gr.Point(pos[0], win.getHeight()-(pos[1]+(self.radisfromcenter*self.scale))))]
        if drawn:
            self.draw()

    def getWidth(self): 
        '''return triangle width'''
        return self.width
    
    def getHeight(self): 
        '''return triangle height'''
        return self.width

    def setWidth(self, dx): 
        '''set triangle width to dx'''
        self.width = dx
        return

    def setHeight(self, dy):
        '''return triangle height to dy'''
        self.height = dy
        return
    def setPosition(self, px, py):
        '''set triangle psotion to px and py'''
        self.position[0]=px
        self.position[1]=py

class Twpballs(Thing):
    '''make two balls connected'''
    def __init__(self,win,x0,y0,radius=1,c="green"):
        '''initalize connected balls'''
        Thing.__init__(self, win, 'ball')
        self.radius = radius
        self.reshpae()
        self.setColor(c)
        self.position=[x0,y0]  #this time do self.position as a list 

    def reshpae(self):
        '''resape the circles or establish them to be 2 circles'''
        if self.drawn:
            self.undraw()
        self.vis = [gr.Circle(gr.Point(self.position[0], (self.win.getHeight()-self.position[1]+(self.radius*self.scale))), self.radius*self.scale), gr.Circle(gr.Point(self.position[0], (self.win.getHeight()-self.position[1]-(self.radius*self.scale))), self.radius*self.scale)]
        if self.drawn:
            self.draw()  #draws updated two circles

    def getRadius(self):
        '''return radius of  balls'''
        return self.radius*2  #radius of one ball times 2


    def setRadius(self, radius):
        ''' redraws the shape with the new radius'''
        self.rad = radius
        self.reshpae()

def buildObstacles(win):
    '''Create all of the obstacles in the scene and put them  in a list'''
    block=Block(win,550, 300, width=2,height=50, color="blue")  #works creates block
    block2=Block(win,100, 300, width=2,height=50, color="blue") 
    trinagle=Triangle(win, x0=300,y0=300,width=5,height=10,c="yellow")
    ball1=Ball(win,c="red",x0=25,y0=50)  #other ball
    vis=[block,trinagle,ball1,block2]  # Each obstacle should be a Thing (e.g. Ball, Block, 
    print("length of vis is", len(vis))  #prints number of obstacles
    return vis # Return the list of Things

def main():
    '''this function is the main function of the project, it sets up the window, the obstacles, the ball, and models the collisions'''
    win = gr.GraphWin('Pinball', 600, 600, False) #making the window for all our graphics
    obstacle = buildObstacles(win) #assigning the result of calling buildObstacles to obstacles
    for shape in obstacle: #looping over shape in obstacles to draw each one
        shape.draw() 
    dt = 0.002
    frame = .5
    ball = Ball(win)  #make pin ball
    ball.setRadius(2.3)
    ball.setVelocity(.1,.1)  #to make slow set low velocity
    ball.setAcceleration(.04,.04)
    ball.draw()
    while True:
        if frame%10 == 0:
            win.update()
        if win.checkKey() == 'q': #lets the user quit by pressing q
            break



0.

        
        if pos[0]*ball.scale > win.getWidth() or pos[1]*ball.scale> win.getHeight(): #if the ball is out of the window, replace the ball at the 35,35
            ball.setPosition(35, 35)
            ball.setVelocity(random.randint(-5,5),random.randint(-5, 5))  #set ranndom velocity
            ball.setAcceleration(0, -2)
        collided = False
        if pos[0]*ball.scale < 0 or pos[1]*ball.scale < 0:  #if it is too left or too low, rest at 35,35
            ball.setPosition(35, 35)
            ball.setVelocity(random.randint(-10,10), random.randint(-5, 5)) #set ranndom velocity
            ball.setAcceleration(0, -2)
        
 
        
        for shape in obstacle:
            if collision.collision(ball, shape, dt):  #if collides with any obstaces
                collided = True

            elif collided == False:  
                ball.update(dt)  #update ball's position if hs not collided, 
        frame += 1
    win.checkMouse()  #check for moue click
    win.close() #closing the window 

if __name__ == "__main__":
    main()


class Block(Thing):
	def __init__(self, win, dx=15,x0 = random.randint(0,700),y0=random.randint(0,700), dy=25):
		'''creaate constructor for ball, chidl class of thing'''
		#use thing's constructor
		Thing.__init__(self,win,"block")
		#set the position of the block 
		self.setPosition(x0,y0)
		self.reshape()
		#set the demensions of the box
		self.dx=dx
		self.dy = dy
		#self.vis.append(Block)
		#set color and then create the vis list w/ reshape	
	def reshape(self):
		'''undraw the object if it is drawn'''
		print("dx", self.dx)
		upperCorn = gr.Point(self.position[0]-self.dx/2,self.position[1]+self.dy/2)
		lowerCorn = gr.Point(self.position[0]+self.dx/2, self.position[1]-self.dy/2)	
		self.vis = [gr.Rectangle(upperCorn,lowerCorn)]
		for i in self.vis:
			i.draw(win)	
			i.setFill("blue")
	def setWidth(self,width):
		'''set width to argument'''
		self.dx = width
	def setHeight(self,height):
		'''set height to argumnet'''
		self.dy = height






