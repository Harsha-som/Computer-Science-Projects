'''Lecture20_zelle_demo.py
A basic program with a shape in the Zelle Graphics Module
CS 152: Computational Thinking
Fall2021
'''

import graphicsPlus as gr


# Create the screen
screen = gr.GraphWin('Title of my screen', width=600, height=600)

# Create an oval shape
myOval = gr.Oval(gr.Point(0, 0), gr.Point(300, 400))

# Create an rectangle shape
rectangle = gr.Rectangle(gr.Point(270, 100), gr.Point(300, 400))

# Set the fill color, outline width, and outline color (as RGB color)
myOval.setFill('blue')
myOval.setOutline('yellow')


# Set rectangle fill using RGB colors
# rect.setFill(gr.color_rgb(255, 0, 255))
rectangle.setFill(gr.color_rgb(0, 255, 0))

# Draw the oval to the screen
myOval.draw(screen)
screen.getMouse()

# Draw the rectangle to the screen
rectangle.draw(screen)
screen.getMouse()

# Customize the outline width and fill color of the oval
myOval.setWidth(20)
myOval.setFill('red')

# Let's move the oval over
myOval.move(100, 100)
# Pause until we click
screen.getMouse()

# Let's get the (x, y) coordinates of the top left point of rectangle
print(rectangle.getP1().getX() + 100)
topLeftPt = rectangle.getP1()
xValue = topLeftPt.getX()
print(xValue + 100)

# After we click, remove the oval from the screen, pausing again to
#see the blank screen
screen.getMouse()
# Close the window after the 2nd click
screen.close()
