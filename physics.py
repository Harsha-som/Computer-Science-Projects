'''Harsha Somaya
11/17/2021
CS152
project9
create rotaing block
change directory to project 9 and run py.phsyics.py to call
'''
import graphicsPlus as gr
import collision as coll
import math
import time

class Thing:  #The thing class is a parent for all simulated objects
	def __init__(self,win,the_type):
		'''constructor for all thing classes/objects'''
		self.type = the_type
		self.win = win
		self.mass = 10
		self.scale = 10
		#start in the middle of the screen
		self.position = [win.getWidth()/(2*self.scale),win.getHeight()/(2*self.scale)]
		self.velocity = [0,0]
		self.acceleration = [0,0]
		self.elasticity = 1
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
	def getScale(self):
		'''return scale, 10'''
		return self.scale
	def getPosition(self): 
		'''returns a 2-element tuple with the x, y position.'''
		return (self.position[0],self.position[1])
	def getVelocity(self): 
		'''returns a 2-element tuple with the x and y velocities.'''
		return (self.velocity[0],self.velocity[1])
	def getAcceleration(self): 
		'''returns a 2-element tuple with the x and y acceleration values.'''
		return (self.acceleration[0],self.acceleration[1])
	def getElasticity(self): 
		'''returns a scalar value for elasticity'''
		return self.elasticity
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

	def setMass(self, m): # m is the new mass of the object
		'''set mass to argumnt m'''
		self.mass = m
	def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
		'''set velocty to vx and vy arguments given'''
		self.velocity[0] = vx
		self.velocity[1] = vy
	def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
		'''set acceleration to ax and ay arguments given'''
		self.acceleration[0] = ax
		self.acceleration[1] = ay

	def setElasticity(self, elasticity):
		'''set elasticity to argumnt given'''
		self.elasticity = elasticity   #elasticty is now given argument

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
		dx = (self.position[0] - oldx)*self.scale
		# assign to dy the negative of the change in the y position times the scale factor (self.scale)
		dy = (self.position[1]- oldy)*-self.scale
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
		self.setColor(color)
	def refresh(self):
		'''update the scene and draw the ball only if appropriate'''
		if self.drawn: # if the object is drawn 
			self.undraw()#undraw the object (use self.undraw())
		self.vis = [ gr.Circle( gr.Point(self.position[0]*self.scale, 	# define the self.vis list of graphics objects using the current position, radius, and window
                                 self.win.getHeight()-self.position[1]*self.scale), 
                        self.radius * self.scale ) ]

		if self.drawn: 		# if the object is drawn 
			self.draw()  #     draw the object

	#get the properties of a balle
	def getRadius(self):
		'''give ball radius'''
		return self.radius	
	#set the property of a ball	
	def setRadius(self,r):
		'''set radius to r'''
		self.radius = r
		self.refresh()  #update teh ball	

#define the functionality of a block
class Block(Thing):
	def __init__(self, win, x0 = 0, y0 = 0, dx=2, dy=1, color=None):
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
	def getWidth(self):
		'''return width'''
		return self.dx
	def getHeight(self):
		'''return height'''
		return self.dy
	def setWidth(self,width):
		'''set width to argument'''
		self.dx = width
		self.reshape()
	def setHeight(self,height):
		'''set height to argumnet'''
		self.dy = height
		self.reshape()


############ Task 1 #############
class RotatingBlock(Thing):
	'''Rotating block is a rectangular object that spins around a given axis of rotation'''
	def __init__(self,win, x0 = 0, y0 =0, height = 1, width = 1, Ax = None, Ay = None,color = (100,0,0)):
		Thing.__init__(self,win,the_type="rotating block")	
		self.position=[x0,y0]
		self.width=width
		self.height=height
		self.points=[[-self.width/2,-self.height/2],[self.width/2,-self.height/2],[self.width/2,self.height/2],[-self.width/2, self.height/2]]
		self.angle=0.0 #The current orientation of the line. Initialize it to 0.0.
		self.rvel=0.0 #rotationalvelocity(in degrees/s). Initialize it to 0.0.
		self.drawn=False
		if Ax!= None and Ay!= None:
			self.anchor=[Ax,Ay]#the Ax and Ay values as a 2-element list, if both are given, otherwise x0, y0 (this involves an if statement) points
		else:
			self.anchor=[x0,y0]
	
	def refresh(self):
		'''it recreates the visual representation based on the current state of the objec'''
		drawn=self.drawn
		if drawn:
			self.undraw()
		self.render()
		if drawn:
			self.draw()

	def getAngle(self):
		'''return current value of self.angle'''
		return self.angle	#ange of object
	
	def setAngle(self, angle):
		'''set the angle to a new value and refresh the shapes'''
		self.angle=angle
		self.refresh() 

	def rotate(self, angleToMove):
		'''increment angle with a specific value and move the shapes'''
		self.angle+=angleToMove     
		self.refresh()   #updates the shape and moves it

	def setAnchor(self, Ax, Ay):
		'''set a new anchor point'''
		self.anchor=[Ax,Ay]
		self.refresh()  #update the balls' position


	def getAnchor(self):
		'''return the anchor point'''
		return self.anchor    #will rotate about teh anchor
	
	def getRotVelocity(self):
		'''return orattional velocity'''
		return self.rvel
	
	def setRotvelocity(self,v):
		'''set roational velocity to argumnt v'''
		self.rvel=v
		self.refresh()

############ Task 3 #############


	def render(self):
		'''micmics the rotation using sin and cosine'''
			# assign to theta the result of converting self.angle from degrees to radians
		theta  = self.angle*math.pi/180.0
		# assign to cth the cosine of theta
		cth = math.cos(theta)
		# assign to sth the sine of theta
		sth = math.sin(theta)
		# assign to pts the empty list
		pts = []
		
		for vertex in self.points:
		# for each vertex in self.points
		  # (2 lines of code): assign to x and y the result of adding the vertex to self.pos and subtracting self.anchor
		  x = vertex[0]+self.getPosition()[0] - self.anchor[0]
		  y = vertex[1]+self.getPosition()[1] - self.anchor[1]

		  # assign to xt the calculation x * cos(Theta) - y * sin(Theta) using your precomputed cos/sin values above
		  xt = x*cth - y*sth
		  # assign to yt the calculation x * sin(Theta) + y * cos(Theta)
		  yt = x*sth+ y*cth
		  # (2 lines of code): assign to x and y the result of adding xt and yt to self.anchor
		  x = xt + self.anchor[0]
		  y = yt + self.anchor[1]

		  # append to pts a Point object with coordinates (self.scale * x, self.win.getHeight() - self.scale*y)
		  pts.append(gr.Point(self.scale*x,self.win.getHeight()-self.scale*y))
		 
		# assign to self.vis a list with a Zelle graphics Rectangle object using the Point objects in pts
		self.vis  = [gr.Polygon(pts[0],pts[1], pts[2], pts[3])]

	def setRotVelocity(self,value):
		'''alter the angular velocity to value'''
		self.rvel = value
		self.refresh()   #updates the object accoridng to if drawn or not, can refer to render
		
	
	def getRotVelocity(self):
		'''return the angular velocity'''
		return self.rvel

	def update(self,dt):
		''' block should appear to rotate around the center of the screen once.'''
		da=self.rvel*dt
		if da!=0:
			self.rotate(da)
			Thing.update(self,dt)   #refers to thing update of parent class with dt as the paramenter
