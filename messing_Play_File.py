'''Harsha Somaya
11/3/2021
CS152
final project
chnage folder to final run messign.py from directory to run file
represent space with a black hole and obstacles/spaceships around it using keys
press q to close window. press o to guess blackhole location. Double click mouse to move. key A for obstacles.
'''
import math
import graphicsPlus as gr
import random

RADIUS = float(input("how big is your rocket's window radius (number from 0 to 30?)"))  #user interface for radius of spaceship window
while RADIUS >30:  #if the user typed a big radius that would cover teh spaceship
	print("hey that too big radius. Try again")
	RADIUS = float(input("how big is your rocket's window radius (number from 0 to 30?)"))  #user interface for radius of spaceship window

win=gr.GraphWin("hi", 2000, 2000)   #create window
win.setBackground("black")


class Thing:  
	'''The thing class is a parent for all simulated objects'''
	def __init__(self,the_type):
		'''constructor for all thing classes/objects'''
		self.type = the_type
		self.position = [250,150]
		self.velocity = [0,0]
		self.acceleration = [0,0]
		self.color  = (0,0,0)
		self.drawn = False
		self.vis=[]


	def getType(self):
		'''return type of object like circle or rectangle'''
		return self.type


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
		for item in self.vis:
			item.move(dx,dy)
		self.position[0] = px
		self.position[1] = py


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


	def undraw1(self):
		'''undraw all  things'''
		for i in self.vis:
			print("undrawing")
			return i.undraw()  #undrawsball obstacles


	def move(self,dx,dy):
		'''make all things move'''
		for i in self.vis:
			i.move(dx,dy)
	


class Ball(Thing):
	'''construct a ball'''
	def __init__(self,radius=10 , x0=100, y0 =100,color = (0,0,0)):
		Thing.__init__(self, "ball")  #type ball
		self.radius = radius   #ball radius, 10 default
		self.setPosition(x0,y0)
		self.refresh()
	

	def refresh(self):
		'''update the scene and draw the ball only if appropriate'''
		self.vis = [ gr.Circle(gr.Point(random.randint(0,1500), 	# define the self.vis list of graphics objects using the radius of asteriods and a random point on teh scren
                                random.randint(0,1700)), 
                        random.randint(1,530)/2  )]
		for i in self.vis:
			i.draw(win)		#set the property of a ball	
			i.setFill("blue")


	def setRadius(self,r):
		'''set radius to r'''
		self.radius = r
		self.refresh()  #update teh ball


	def getcenter(self):
		'''give center of ball obstacle'''
		for i in self.vis:
			return i.getCenter()



	def getRadius(self): 
		'''Returns the radius of the Ball as a scalar value'''
		return self.radius




def MouseTracker():
	'''represent space with black hole and obstales'''
	numobstacles=[]  #initally emplty
	POSITION = gr.Point(270, 350)   #intial position of spaceship
	circle=gr.Circle(POSITION,RADIUS)   #create spaceship's window
	ship=gr.Image(gr.Point(230,330),"spaceship4.gif")
	asteriods=[]
	balllist=[]
	while True:
		intro=gr.Text((gr.Point(700,50)), "can you find the blackhole (A,B,C,D) while using obstacles? Click a for obstacles. \n Move mouse to move spaceship. Starting score is 10000000, but the more times a is pressed the lower score by a factorial. \n Press o to guess location. Only two trials are allowed before the window closes. Press q to close anytime")
		intro.setTextColor("red")
		intro.draw(win)   #draws instructions
		blackholeA=gr.Text((gr.Point(1300,200)), "A")
		blackholeA.setTextColor("lightgreen")
		blackholeA.draw(win)  #draw text for black hole A
		blackholeA.setSize(20)
		blackholeB=gr.Text((gr.Point(1300,700)), "B")
		blackholeB.setTextColor("lightgreen")
		blackholeB.draw(win)
		blackholeB.setSize(20)
		blackholeC=gr.Text((gr.Point(200,700)), "C")
		blackholeC.setTextColor("lightgreen")
		blackholeC.draw(win)
		blackholeC.setSize(20)
		blackholeD=gr.Text((gr.Point(200,200)), "D")   #creates text "D"
		blackholeD.setTextColor("lightgreen")
		blackholeD.draw(win)
		blackholeD.setSize(20)
		if win.checkMouse():  #makes a pink ball where i click with spaceship as window
			circle.undraw()  #undraw circle, so i cna then redraw it to wherever i click mouse
			ship.undraw()    #ship and circle(window of ship) both undraw
			mouseposition = win.getMouse()
			circlecenter = circle.getCenter()
			shipcenter=ship.getAnchor()
			dx = (mouseposition.getX() - circlecenter.getX())   #difference between where the circle center is and the mouse position 
			dy = (mouseposition.getY() - circlecenter.getY())
			dxs=(mouseposition.getX()-shipcenter.getX())
			dys=(mouseposition.getY()-shipcenter.getY())
			circle.move(dx, dy)  #move by dx, dy, move from current position to mouse position
			ship.move(dxs,dys)  #move spaceship to where the mouse is clicked
			circle.setFill("pink")
			ship.draw(win)  #redraw at new position
			circle.draw(win)
			if abs(ship.getAnchor().getX()-blackholeA.getAnchor().getX())<=85 and abs( ship.getAnchor().getY()-blackholeA.getAnchor().getY())<=85 :  #if is close to blackholeA
				ship.undraw()  #undraw both spaceshp and it's window
				circle.undraw()
				print("spaceship close to black hole A")
			if abs(circle.getCenter().getX()-blackholeA.getAnchor().getX())<=85 and abs( circle.getCenter().getY()-blackholeA.getAnchor().getY())<=85 :  #same code as above but for circle (window specifically)
				ship.undraw()
				circle.undraw()	
				print("spaceship window close to black hole A")
		key=win.checkKey()
		if key=="a":  #adds obstacles
			pic=gr.Image(gr.Point(random.randint(0,2000),random.randint(0,2000)),"asteriod.gif")	
			pic.draw(win)
			asteriods.append(pic)  #add asteriod picure to the empty list
			numobstacles.append(1)   #adsteriod, ball count against you by a factorial of 1
			ballobstacle=Ball(win)  #create blue ball obstacles  #size: https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/overview/?page=0&per_page=40&order=name+asc&search=&condition_1=101%3Aparent_id&condition_2=asteroid%3Abody_type%3Ailike
			balllist.append(ballobstacle)
			POINTS = 5
			vertices = []
			length = random.randint(20,40) #neutron star size-https://www.schoolsobservatory.org/learn/astro/stars/class/starsize
			theta = -math.pi / 2
			delta = 4 / POINTS * math.pi
			for i in range(POINTS):
				vertices.append(gr.Point(length * math.cos(theta), length * math.sin(theta)))
				theta += delta
			star = gr.Polygon(vertices)  #make star gven vertices
			star.draw(win)  #draw stars into window
			star.move(random.randint(0,1500),random.randint(0,2000))  #put stars randomly inside window
			star.setFill(random.choice(["red", "white","orange","yellow", "lightblue"]))  #colors of stars in space
		for i in asteriods:
			if abs(i.getAnchor().getX()-blackholeA.getAnchor().getX())<=150 and abs( i.getAnchor().getY()-blackholeA.getAnchor().getY())<=150 :  #if asteriods are to close to black hole A
				print("asteriod close to A")
				i.undraw()
			if i.getAnchor().getX()<0:  #if too much to left
				i.move(900,0)  #reposition to center of window
				print("asteriod too left")
			if i.getAnchor().getX()>2000:#if too much to right
				i.move(-900,0)
				print("asteriod too right")
			if i.getAnchor().getY()>2000:#if too down
				i.move(0,-800)
				print("asteriod too down")
			if i.getAnchor().getY()<0:#if too up
				i.move(0,800)	
				print("asteriod too up")	
		for i in balllist:
			if abs(i.getcenter().getX()-blackholeA.getAnchor().getX())<=100 and abs( i.getcenter().getY()-blackholeA.getAnchor().getY())<=100:  #if ball obstacles too close to black hole A
				print("ball too close to balck hole A")
				i.undraw1()   #undraw blue ball obstacles
			if i.getcenter().getX()<0 or i.getcenter().getX()>2000 or i.getcenter().getY()>2000 or i.getcenter().getY()<0:  #if out of bound
				i.setPosition(random.randint(0,2000),random.randint(0,2000))
				print("ballout of bound, recenetering")
		for i in balllist:
			dx=random.randint(-11,11)  #make ball move
			dy=random.randint(-5,5)
			i.move(dx,dy)			
		for i in asteriods:  #every asteriod in list of asteriod
			dx=random.randint(-11,11)  #make asteriods move
			dy=random.randint(-5,5)
			i.move(dx,dy)
		factorial(len(numobstacles))  #continuoslly print the high score
		if key=="o":  #allow user to guess b/c then answer() is called
			break
		if key=="q":  #closes wndow
			win.close()
	answer()
	while True:  #runs after first gess is wrong
		intro=gr.Text((gr.Point(700,50)), "can you find the blackhole (A,B,C,D) while using obstacles? Click a for obstacles. \n Move mouse to move spaceship. Starting score is 10000000, but the more times a is pressed the lower score by a factorial. \n Press o to guess location. Only two trials are allowed before the window closes. Press q to close anytime")
		intro.setTextColor("red")
		intro.draw(win)  #draws instructions
		blackholeA=gr.Text((gr.Point(1300,200)), "A")
		blackholeA.setTextColor("lightgreen")
		blackholeA.draw(win) #draw text for black hole A
		blackholeA.setSize(20)
		blackholeB=gr.Text((gr.Point(1300,700)), "B")
		blackholeB.setTextColor("lightgreen")
		blackholeB.draw(win)
		blackholeB.setSize(20)
		blackholeC=gr.Text((gr.Point(200,700)), "C")
		blackholeC.setTextColor("lightgreen")
		blackholeC.draw(win)
		blackholeC.setSize(20)
		blackholeD=gr.Text((gr.Point(200,200)), "D") #creates text "D"
		blackholeD.setTextColor("lightgreen")
		blackholeD.draw(win)
		blackholeD.setSize(20)
		if win.checkMouse():  #makes a pink ball where i click
			circle.undraw()  #undraw circle, so i cna then redraw it to wherever i click mouse
			ship.undraw()  #ship and circle(window of ship) both undraw
			mouseposition = win.getMouse()
			circlecenter = circle.getCenter()  #center of circle currently
			shipcenter=ship.getAnchor()
			dx = (mouseposition.getX() - circlecenter.getX()) #difference between where the circle center is and the mouse position  
			dy = (mouseposition.getY() - circlecenter.getY())
			dxs=(mouseposition.getX()-shipcenter.getX())
			dys=(mouseposition.getY()-shipcenter.getY())
			circle.move(dx, dy)  #move by dx, dy, move from current position to mouse position
			ship.move(dxs,dys) #move spaceship to where the mouse is clicked
			circle.setFill("pink")
			ship.draw(win)
			circle.draw(win)
			if abs(ship.getAnchor().getX()-blackholeA.getAnchor().getX())<=85 and abs( ship.getAnchor().getY()-blackholeA.getAnchor().getY())<=85 :  #if close to black hole A
				ship.undraw()  #undraw both spaceshp and it's window
				circle.undraw()
				print("spaceship close to black hole A")
			if abs(circle.getCenter().getX()-blackholeA.getAnchor().getX())<=85 and abs( circle.getCenter().getY()-blackholeA.getAnchor().getY())<=85 :  #same code as above but for circle (window specifically)
				ship.undraw()
				circle.undraw()	
				print("spaceship window close to black hole A")
		key=win.checkKey()
		if key=="a": 
			pic=gr.Image(gr.Point(random.randint(0,2000),random.randint(0,2000)),"asteriod.gif")	
			pic.draw(win)
			asteriods.append(pic)  #add asteriod picure to the empty list
			numobstacles.append(1)  #adsteriod, ball count against you by a factorial of 3#https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/overview/?page=0&per_page=40&order=name+asc&search=&condition_1=101%3Aparent_id&condition_2=asteroid%3Abody_type%3Ailike
			ballobstacle=Ball(win)  #create blue ball obstacles
			balllist.append(ballobstacle)
			POINTS = 5
			vertices = []
			length = random.randint(20,40) #neutron stars-https://www.schoolsobservatory.org/learn/astro/stars/class/starsize
			theta = -math.pi / 2
			delta = 4 / POINTS * math.pi
			for i in range(POINTS):
				vertices.append(gr.Point(length * math.cos(theta), length * math.sin(theta)))
				theta += delta
			star = gr.Polygon(vertices) #make star gven vertices
			star.draw(win) #draw stars into window
			star.move(random.randint(0,1500),random.randint(0,2000))   #put stars randomly inside window
			star.setFill(random.choice(["red", "yellow", "lightblue", "orange", "white"]))  #colors of stars in space
		for i in asteriods:
			if abs(i.getAnchor().getX()-blackholeA.getAnchor().getX())<=150 and abs( i.getAnchor().getY()-blackholeA.getAnchor().getY())<=150 :  #if asteriods to close to black hole A
				i.undraw()
				print("asteriod close to A")
			if i.getAnchor().getX()<0:  #if too much to left
				i.move(900,0)  #reposition to center of window
				print(" asteriod too left")
			if i.getAnchor().getX()>2000:#if too much to right
				i.move(-900,0)
				print("asteriod too right")
			if i.getAnchor().getY()>2000:#if too down
				i.move(0,-800)
				print("asteriod too down")
			if i.getAnchor().getY()<0:#if too up
				i.move(0,800)
				print("asteriod too up")
		for i in balllist:
			if abs(i.getcenter().getX()-blackholeA.getAnchor().getX())<=100 and abs( i.getcenter().getY()-blackholeA.getAnchor().getY())<=100:  ##if ball obstacles too close to black hole A
				i.undraw1()  #undraw blue ball obstacles
				print("ball too close to balck hole A")
			if i.getcenter().getX()<0 or i.getcenter().getX()>2000 or i.getcenter().getY()>2000 or i.getcenter().getY()<0:
				i.setPosition(random.randint(0,2000),random.randint(0,2000))  #if out of bound
				print("ballout of bound, recenetering")
		for i in balllist:
			dx=random.randint(-11,11)  #make ball move
			dy=random.randint(-5,5)
			i.move(dx,dy)
		for i in asteriods:  #every asteriod in list of asteriod
			dx=random.randint(-11,11)  #make asteriods move
			dy=random.randint(-5,5)
			i.move(dx,dy)
		factorial(len(numobstacles))  #continusolly print teh high score
		if key=="o":  #allow user to guess
			break
		if key=="q": #closes wndow
			win.close()
	answer()


def factorial (num):  
	'''caculates the high score as a recursive function based on the number of obstacles'''
	fact  = 1
	for num in range(num, 0, -1):  
		fact *= num  
	print("your score is",10000000-fact)


def answer():
	'''ask user to guess where the black hole is'''
	question=input("where's the hole?")
	if question=="A" or question=="a":
		print("correct!, window closing")
		win.close()  #close window
	else: 
		print("try again, keep playing around with the obstacles to guess. After two incorrect attempts, you must reurn the file to guess.")


if __name__ == '__main__':
	MouseTracker()  #call main simulation



