#Stacy Doore
#CS 152 Fall 2021
#chessboard.py



import graphicsPlus as gr
import random
win = gr.GraphWin("my chessboard", 1000, 1000)
 
def draw_blk_rectangle(x1,y1, x2, y2):
    rectangle = gr.Rectangle(gr.Point(x1,y1), gr.Point(x2, y2))
    rectangle.draw(win)
    rectangle.setFill(gr.color_rgb(0, 0, 0))

def draw_red_rectangle(x1,y1, x2, y2):
    rectangle = gr.Rectangle(gr.Point(x1,y1), gr.Point(x2, y2))
    rectangle.draw(win)
    rectangle.setFill("white")

# k=[11,1,12,2]
# y=[]
# l=[11]
# for s in range (7):  #0,1,2,3,4,5,6
#     l.append(l[s]+10)
# print(l)
#l=[11,21,31]
#110 to 210 to 110   
# for x in range (7):
#     y.append(x)
# #y=[100,200,300,]
# for i in range(7): #give me x rows instead of only 3
#     for r in range(len(k)-1):
#         draw_blk_rectangle(10*k[r]+200*i,10+(y[x])+200*i, 110+100*k[r]+200*i, 110+y[x])
#         draw_red_rectangle(110+200*i,10, 210+200*i, 110)
    #row 1 function 'hardcoding it' -- can you use parameters to optimize it?
def row_1(x):
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(10+200*i,10, 110+200*i, 110)
        draw_red_rectangle(110+200*i,10, 210+200*i, 110)
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(110+200*i,110, 210+200*i, 210)
        draw_red_rectangle(10+200*i,110, 110+200*i, 210)
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(10+200*i,210, 110+200*i, 310)
        draw_red_rectangle(110+200*i,210, 210+200*i, 310)
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(10+200*i,10, 110+200*i, 110)
        draw_red_rectangle(110+200*i,10, 210+200*i, 110)
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(10+200*i,10, 110+200*i, 110)
        draw_red_rectangle(110+200*i,10, 210+200*i, 110)
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(10+200*i,10, 110+200*i, 110)
        draw_red_rectangle(110+200*i,10, 210+200*i, 110)
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(10+200*i,10, 110+200*i, 110)
        draw_red_rectangle(110+200*i,10, 210+200*i, 110)
    for i in range(x): #give me x rows instead of only 3
        draw_blk_rectangle(10+200*i,10, 110+200*i, 110)
        draw_red_rectangle(110+200*i,10, 210+200*i, 110)
row_1(9)
win.getMouse()
win.close()
