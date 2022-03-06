#prelab09 

#Rajesh Balasamy

#CS177

#import graphics library

from graphics import *

#draws a spaceship
#def main():
    
def drawSpaceship():
    
    #window = GraphWin('Spaceship', 500, 500)
    
    win = GraphWin('spaceship', 500, 500)
    c = Circle(Point(250,200), 150)
    c.setFill('red1')
    c.setOutline('black')
    c.draw(win)
    c2 = Circle(Point(325,125), 25)
    c2.setFill('blue1')
    c2.setOutline('black')
    c2.draw(win)
    d = Polygon(Point(100,200), Point(400,200), Point(500,350), Point(0,350))
    d.setFill('yellow1')
    d.setOutline('black')
    d.draw(win)
    w1 = Rectangle(Point(100,250), Point(200,300))
    w1.setFill('green1')
    w1.setOutline('black')
    w1.draw(win)
    w2 = Rectangle(Point(300,250), Point(400,300))
    w2.setFill('green1')
    w2.setOutline('black')
    w2.draw(win)
    p1 = Polygon(Point(145,345), Point(155,355), Point(65,455),  Point(55,445))
    p1.setFill('darkorchid')
    p1.setOutline('darkorchid')
    p1.draw(win)
    p2 = Polygon(Point(355,345), Point(345,355), Point(435,455),  Point(445,445))
    p2.setFill('darkorchid')
    p2.setOutline('darkorchid')
    p2.draw(win)
    p3 = Rectangle(Point(242,350), Point(258,450))
    p3.setFill('darkorchid')
    p3.setOutline('darkorchid')
    p3.draw(win)
    win.getMouse() # pause for click in window
    win.close()

drawSpaceship()