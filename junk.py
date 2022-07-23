# class Star(Thing):
# 	def __init__(self,win):
# 		Thing.__init__(self, win, "star")
# 		self.setrandompos(random.randint(0,1000),random.randint(0,1000))
# 	def create(self):
# 		POINTS = 5
# 		vertices = []
# 		length = 25
# 		theta = -math.pi / 2
# 		delta = 4 / POINTS * math.pi
# 		for i in range(POINTS):
# 			vertices.append(gr.Point(length * math.cos(theta), length * math.sin(theta)))
# 			theta += delta
# 		star = gr.Polygon(vertices)
# 		star.setFill('blue')
# 		print("k",star.getPoints())
# 	def setoutline(self,c):
# 		self.setOutline(c)
# 	def setwidth(self,c):
# 		self.setWidth(c)  # width of boundary line
# 	def setrandompos(self,px,py):			
# 		self.move(px,py)
# 		self.draw(win)

#define the functionality of a block

# class Block(Thing):
# 	def __init__(self, win, width=15,x0=random.randint(0,700),y0=random.randint(0,700),height=25):
# 		Thing.__init__(self,win,"block")
# 		self.setPosition(x0,y0)
# 		self.position=[x0,y0]
# 		self.reshape()
# 		self.width=width
# 		self.height=height
# 	def reshape(self):
# 		print("dx",self.width)
# 		uppercorn=gr.Point(self.position[0]-self.width/2, self.position[1]+self.height/2)
# 		lowercorn=gr.Point(self.position[0]+self.width/2,self.position[1]-self.height/2)
# 		self.vis=[gr.Rectangle(uppercorn,lowercorn)]
# 		for i in self.vis:
# 			i.draw(win)
# 			i.setFill("blue")

# class Asteriod(Thing):
# 	'''construct a ball'''
# 	def __init__(self,win):
# 		Thing.__init__(self, win, "asteriod")
# 		self.refresh() 
# 		#self.setPosition(x0,y0)
# 	def refresh(self):
# 		'''update the scene and draw the ball only if appropriate'''
# 		# if self.drawn: # if the object is drawn 
# 		# 	self.undraw()#undraw the object (use self.undraw())
# 		self.vis = [ gr.Image(gr.Point(random.randint(0,700), 	# define the self.vis list of graphics objects using the current position, radius, and window
#                                 random.randint(0,700)), 
#                          "asteriod.gif")]
# 		for i in self.vis:
# 			i.draw(win)		#set the property of a ball	
# age=gr.Image(gr.Point(350,350),"spaceship2.gif")
		# age.draw(win)
#for _ in range(STEPS):
#numobstacles.append(pic)
#numobstacles.append(star)
			#print(numobstacles)
#print(numberasteriods)
			#x=random.randint(1,530)   #diamter of asteriods in space km
			#https://solarsystem.nasa.gov/asteroids-comets-and-meteors/asteroids/overview/?page=0&per_page=40&order=name+asc&search=&condition_1=101%3Aparent_id&condition_2=asteroid%3Abody_type%3Ailike
#obstalceblock=Block(win,width=15)
			#obstalceblock.reshape()
			#obstacle=random.choice(obstaclelist)
			#obstacle.draw()
			#numobstacles.append(ballobstacle)
# 	if i.getP1().getX()<0 or i.getP1().getY()<0 or i.getP2().getX()>700 or i.getP2().getY()>700:  #if out of bounds
			# 		blueaaaaacenter=i.getCenter()
			# 		dx=350-bluecenter.getX()
			# 		dy=350-bluecenter.getY()
			# 		i.setPostion(dx,dy) #reposition at center of screen
		#if collision.collision(circle, ballobstacle, dt=10) :
		# 	end=gr.Text((gr.Point(500,500)), "OOPS COLISION END OF GAME!")
		# 	end.setTextColor("red")
		# 	end.setTextColor(win)
		#return(len(numobstacles))
		# 	break
def add_till_10(list):
	sum=0
	i=0
	while sum<10:
		print("i:",i)
		sum+=list[i]
		print("sum",sum)
		i+=1
	return sum
#sum_total = add_till_10([1, 2, 3, 3, 5])
#print("The sum is", sum_total)	
# def two (he):
# 	sum=0
# 	for i in he:
# 		sum+=i
# 		if sum>10:
# 			return sum, "k"
# 	return sum
# sum_total = two([1, 2, 3, 2])
# print("The sum is", sum_total)



