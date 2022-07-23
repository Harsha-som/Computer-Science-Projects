'''A simple graphics example constructs a face from basic shapes.
'''

import graphicsPlus as gr


def main():
    win = gr.GraphWin('Face', 200, 150) # give title and dimensions
    #wingr.yUp() # make right side up coordinates!

    head = gr.Circle(gr.Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = gr.Circle(gr.Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = gr.Line(gr.Point(45, 105), gr.Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = gr.Oval(gr.Point(30, 90), gr.Point(50, 85)) # set corners of bounding box
    mouth.setFill("red")
    mouth.draw(win)

    label = gr.Text(gr.Point(100, 120), 'A face')
    label.draw(win)

    message = gr.Text(gr.Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()
