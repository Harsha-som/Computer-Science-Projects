'''Harsha Somaya
11/3/2021
CS152
lab8


'''
import graphicsPlus as gr
import time
import random
import collision as collision


class Thing:  #The thing class is a parent for all simulated objects
	def __init__(self,win,the_type):
		'''constructor for all thing classes/objects'''
		self.type = the_type
		self.win = win
		#start in the middle of the screen
		self.position = [win.getWidth()/(2*self.scale),win.getHeight()/(2*self.scale)]
		self.velocity = [0,0]
		self.acceleration = [0,0]
		#list of the Zelle graphics that make up an obj
		self.vis = []
		#rgb tuple for color
		self.color  = (0,0,0)
		self.drawn = False

	def getType(self):
		'''return type of object like circle or rectangle'''
		return self.type
	def getMass(self): 
		'''Returns the mass of the object as a scalar value'''
		return self.mass
	def getPosition(self): 
		'''returns a 2-element tuple with the x, y position.'''
		return (self.position[0],self.position[1])
	def getVelocity(self): 
		'''returns a 2-element tuple with the x and y velocities.'''
		return (self.velocity[0],self.velocity[1])
	def getAcceleration(self): 
		'''returns a 2-element tuple with the x and y acceleration values.'''
		return (self.acceleration[0],self.acceleration[1])
	def getColor(self): 
		'''returns a tuple for rgb color'''
		return self.color		
	def draw(self):
		'''draw every shape into the window'''
		for item in self.vis:
			item.draw(self.win)   
		self.drawn = True
	def undraw(self):
		'''undraw evey shape in the window'''
		for item in self.vis:
			item.undraw()
		self.drawn = False    #undrawn, so now self.drawn is false
	def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
		'''set velocty to vx and vy arguments given'''
		self.velocity[0] = vx
		self.velocity[1] = vy
	def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
		'''set acceleration to ax and ay arguments given'''
		self.acceleration[0] = ax
		self.acceleration[1] = ay
	def setPosition(self,px,py):
		'''set position to px and py and then move by difference '''
		dx = px - self.position[0]
		dy = py - self.position[1]
		self.position[0] = px
		self.position[1] = py
		dx = dx*self.scale        #makes the chnage in x be according to the scale
		dy = dy*self.scale*(-1)			
		for item in self.vis:
			item.move(dx,dy)

	def setColor(self,c):  # takes in an (r, g, b) tuple
		'''set color to c for every item '''
		self.color  = c 
		if self.color != None:
			for item in self.vis: 
				item.setFill(gr.color_rgb(c[0],c[1],c[2]))    

	def update(self,dt):
		'''update the shapes position and velocity according to time dt'''
		oldx = self.position[0]
		oldy = self.position[1]
		# update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
		self.position[0] = self.position[0]+self.velocity[0]*dt + .5*self.acceleration[0]*dt**2
		# update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 
		self.position[1] = self.position[1]+self.velocity[1]*dt + .5*self.acceleration[1]*dt**2
		# assign to dx the change in the x position times the scale factor (self.scale)
		dx = (self.position[0] - oldx)
		# assign to dy the negative of the change in the y position times the scale factor (self.scale)
		dy = (self.position[1]- oldy)
		# for each item in self.vis
		# call the move method of the graphics object with dx and dy as arguments..
		for item in self.vis:
			item.move(dx,dy)
       # update the x velocity by adding the acceleration times dt to its old value
		self.velocity[0] += self.acceleration[0]*dt
       # update the y velocity by adding the acceleration times dt to its old value
		self.velocity[1] += self.acceleration[1]*dt

#define fuctionality for a ball
class Ball(Thing):
	'''construct a ball'''
	def __init__(self,win,radius = 1, x0 = 0, y0 =0,color = (0,0,0)):
		Thing.__init__(self, win, "ball")
		self.radius = radius   #ball radius, 1
		self.refresh()
	def refresh(self):
		'''update the scene and draw the ball only if appropriate'''
		if self.drawn: # if the object is drawn 
			self.undraw()#undraw the object (use self.undraw())
		self.vis = [ gr.Circle( gr.Point(self.position[0], 	# define the self.vis list of graphics objects using the current position, radius, and window
                                 self.win.getHeight()-self.position[1]), 
                        self.radius ) ]
		if self.drawn: 		# if the object is drawn 
			self.draw()  #     draw the object
	
	#set the property of a ball	
	def setRadius(self,r):
		'''set radius to r'''
		self.radius = r
		self.refresh()  #update teh ball	

#define the functionality of a block
class Block(Thing):
	def __init__(self, win, x0 = 350, y0 = 350, dx=2, dy=1, color=None):
		'''creaate constructor for ball, chidl class of thing'''
		#use thing's constructor
		Thing.__init__(self,win,"block")
		#set the position of the block 
		self.setPosition(x0,y0)
		#set the demensions of the box
		self.dx = dx
		self.dy = dy
		#set color and then create the vis list w/ reshape
		self.setColor(color)	
		self.reshape()	
	def reshape(self):
		'''undraw the object if it is drawn'''
		if self.drawn:
			self.undraw()
		x0 = self.getPosition()[0]   #current x position
		y0 = self.getPosition()[1]
		upperCorn = gr.Point(x0*self.scale-self.dx*self.scale/2, self.win.getHeight()-y0*self.scale-self.dy*self.scale/2)
		lowerCorn = gr.Point(x0*self.scale+self.dx*self.scale/2, self.win.getHeight()- y0*self.scale+self.dy*self.scale/2)	
		self.vis = [gr.Rectangle(upperCorn,lowerCorn)]

		if self.drawn:
		# if the object is drawn 
			self.draw()
		#     draw the object
	def setWidth(self,width):
		'''set width to argument'''
		self.dx = width
		self.reshape()
	def setHeight(self,height):
		'''set height to argumnet'''
		self.dy = height
		self.reshape
             

WIDTH, HEIGHT = 700, 700
POSITION = gr.Point(350, 350)
RADIUS = float(input("how big is your space sation's radius?"))
STEPS = 1
def MouseTracker():
    '''make ball where i click on screen'''
    win=gr.GraphWin("hi", WIDTH, HEIGHT)
    list=[]
    circle=gr.Circle(POSITION,RADIUS)
    print(circle.getRadius, "k")
    while True:
        intro=gr.Text((gr.Point(350,50)), "can you survive long enough to have a high score and see the flower complete?")
        intro.setTextColor("red")
        intro.draw(win)
        numberasteriods=[]
        asteriodtext=gr.Text((gr.Point(600,600)), "number of asteriods: {0}".format(numberasteriods))
        asteriodtext.draw(win)
        if win.checkMouse():  #makes a pink ball where i click
            circle.undraw()  #undraw circle
            mouseposition = win.getMouse()
            circlecenter = circle.getCenter()
            dx = (mouseposition.getX() - circlecenter.getX())  
            dy = (mouseposition.getY() - circlecenter.getY())
            #for _ in range(STEPS):
            circle.move(dx, dy)  #move by dx, dy, move from current position to mouse position
            circle.setFill("pink")
            circle.draw(win)
        if win.checkKey()=="a":  #if i click a, create a blue circle
            numberasteriods.append(1)
            print(numberasteriods)
            win.update()
            x=random.randint(1,530)   #diamter of asteriods in space
            #https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/overview/?page=0&per_page=40&order=name+asc&search=&condition_1=101%3Aparent_id&condition_2=asteroid%3Abody_type%3Ailike
            bluecircle=gr.Circle(gr.Point(random.randint(0,700),random.randint(0,700)), x/2)
            bluecircle.setFill("blue")
            bluecircle.draw(win)
            list.append(bluecircle)
        for i in list:  #make the circles move
            dx=random.randint(-10,10)
            dy=random.randint(-3,2)
            i.move(dx,dy)
            if i.getP1().getX()<0 or i.getP1().getY()<0 or i.getP2().getX()>700 or i.getP2().getY()>700:  #if out of bounds
                bluecenter=i.getCenter()
                dx=350-bluecenter.getX()
                dy=350-bluecenter.getY()
                i.move(dx,dy) #reposition at center of screen
        win.update()

        time.sleep(.033)
		#win.close()
        # pensize(2)
        # pencolor("orange")
        # bgcolor("green")
        # fillcolor("blue")
        # hideturtle()

        # def halfPetal():
        #     forward(50)
        #     left(30)
        #     forward(75)
        #     left(30)
        #     forward(50)
        #     left(120)

        # def petal():
        #     for i in range(2):
        #         halfPetal()
        # def flower(num, i=1):
        #     if i==1:
        #         begin_fill()
        #         for i in range(num):
        #             petal()
        #             left(360/num)
        #         end_fill()
        # flower(4)
        # time.sleep(2000000)
    
MouseTracker() 

 








