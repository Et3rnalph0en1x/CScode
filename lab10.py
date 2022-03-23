#prelab10

#Rajesh Balasamy

#CS177

# Import the Graphics library and two random functions
from graphics import *
from random import randint, choice


# The clicked() function accepts a mouse click Point and a Circle 
#   and returns True if the click is inside the Circle. If the
#   click is not inside the Circle it returns False
def clicked(click, circle):
    # if no mouse click was detected return False
    if not click:
        return False
    # get the x,y coordinates of the center Point of the Circle
    center = circle.getCenter()
    cx,cy = center.getX(), center.getY()
    # get the x,y coordinates of the mouse click
    x,y = click.getX(), click.getY()
    radius = circle.getRadius()
    # use Pythagorean's equation to calculate distance between
    #   mouse click and center of Circle
    distance = ((x-cx)**2 + (y-cy)**2)**.5
    # was the mouse click inside the Circle?
    if distance < radius:
        return True
    else:
        return False

# The make() function creates a List of 10 Circles using randomly selected
#   coordinates, a random radius and fill color. 
def make(win):
    # List of colors to choose from for the Circles
    colors = ['red','blue','yellow','green','grey','black']
    # Create empty List that will be used to store the Circles
    circles = []
    # Loop 10 times to create 10 Circles
    for i in range(10):
        # Choose a random x,y coordinate and random radius
        x = randint(20,380)
        y = randint(20,380)
        radius = randint(10,20)
        # Create a Circle using the random coordinates and radius
        c = Circle(Point(x,y),radius)
        # Randomly choose a fill color from the List of colors
        c.setFill(choice(colors))
        c.draw(win)
        # append the new Circle to the List of Circles
        circles.append(c)
    # return the completed List of Circles
    return circles

win2 = GraphWin('Click me', 400, 400)
circleList = make(win2)

while len(circleList) > 0:
    click = win2.getMouse()
    for i in range(len(circleList)-1):
        if clicked(click,circleList[i]):
            d = circleList[i]
            d.setOutline('white')
            d.setFill('white')
            d.draw(win2)
            del circleList[i]
            for j in range(len(circleList)-1):
                c = circleList[j]
                colors = ['red','blue','yellow','green','grey','black']
                # Randomly choose a fill color from the List of colors
                c.setFill(choice(colors))
                c.draw(win2)
                
       

 # pause for click in window
win2.close()




