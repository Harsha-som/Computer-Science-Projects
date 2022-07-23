'''Graphics Library Shapes Demo
Vivid hodgepodge of shapes to show usage
CS151 Visual Media, Fall 2018
Lecture 16: Zelle Graphics Library'''


import graphicsPlus as gr


def main_vivid():
    # Define a 500x400 GraphWin window object
    width = 500
    height = 400
    win = gr.GraphWin("My canvas", width, height)
    # Create some shape objects we want to work with
    #
    # A circle filled with a named color
    circCenter = gr.Point(25, 25)
    myCircle = gr.Circle(circCenter, 10)
    myCircle.setFill('blue')
    myCircle.setOutline('yellow')
    myCircle.setWidth(5)

    triPoint1 = gr.Point(100, 100)
    triPoint2 = gr.Point(200, 100)
    triPoint3 = gr.Point(100, 150)

    myTri = gr.Polygon(triPoint1, triPoint2, triPoint3)
    myTri.setFill('green')

    # Draw the shapes on the GraphWin window
    myCircle.draw(win)
    myTri.draw(win)

    # Keep the window open until we click
    win.getMouse()

    # Print that we're close the window after we click the window
    win.close()

if __name__ == '__main__':
    main_vivid()
