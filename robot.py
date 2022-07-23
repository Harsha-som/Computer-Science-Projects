
import graphicsPlus as gr

def main():
    win = gr.GraphWin("Robot", 1000, 1000)
    def body():
        rectangle = gr.Rectangle(gr.Point(400,400), gr.Point(500,500))
        rectangle.draw(win)
        rectangle.setFill("purple")
    body()

    def head():
        pt = gr.Point(450,370)
        pt.draw(win)
        cir= gr.Circle(pt, 30)
        cir.draw(win)
        cir.setOutline('orange')
        cir.setWidth(3)
        cir.setFill('green')
    head()

    def leftarm():
        line = gr.Line(gr.Point(398,450),gr.Point(350,500))
        line.setWidth(3)
        line.setFill("pink")
        line.draw(win)
    leftarm()

    def rightarm():
        line=gr.Line(gr.Point(502,450), gr.Point(550,500))
        line.draw(win)
        line.setWidth(3)
        line.setFill("pink")
    rightarm()
    win.getKey() #pause for click in window win.close()
    win.close()
main()