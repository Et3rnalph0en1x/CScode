# CS 177 – project4.py

# Rajesh Balasamy

# Uses the graphics library to visualize Riemann Sums

from graphics import *

def createWindow(windowWidth, windowHeight):
    
    win = GraphWin('Area Approximation', windowWidth, windowHeight)
    
    return win

def getXCoordinates(interval, rectangleWidth):
    
    resultList = []
    
    resultList.append(interval[0])
    
    tempX = rectangleWidth + interval[0]
    
    while tempX < interval[1]:
        
        resultList.append(tempX)
        
        tempX = tempX + rectangleWidth
        
    return resultList

def f(x):
    
    y = .001 * (x**2)
    
    return y

def getYCoordinates(x_coordinates):
    
    y_coordinates = []
    
    for i in range(len(x_coordinates)):
        
        temp = f(x_coordinates[i])
        
        y_coordinates.append(temp)
        
    return y_coordinates
    
def getRectanlgesList(x_coordinates, y_coordinates, windowHeight):
    
    rectangles = []
    
    for i in range(len(x_coordinates)-1):
        
        PointA = Point(x_coordinates[i], windowHeight - y_coordinates[i])
        
        PointB = Point(x_coordinates[i+1], windowHeight)
        
        rectangle = Rectangle(PointA, PointB)
        
        rectangles.append(rectangle)
        
    return rectangles

def plotRectangles(rectanglesList, window):
    
    for i in rectanglesList:
        
        p1 = i.getP1()
        
        p2 = i.getP2()
        
        rectangle = Rectangle(p1, p2)
        
        rectangle.draw(window)
        
        rectangle.setFill('red')
    
def getApproxArea(x_coordinates, y_coordinates):
    
    area = 0
    
    for i in range(len(x_coordinates)-1):
        
        width = x_coordinates[i+1]-x_coordinates[i]
    
        height = y_coordinates[i]
        
        area = area + (width * height)
        
    return area


def displayArea(area, window):
    
    areaStr = str(area)
    
    str1 = 'Area of Rectangles = '
    
    textString = str1 + areaStr
    
    message = Text(Point(150,15), textString)
    
    message.setFace('arial')
    
    message.setSize(10)
    
    message.draw(window)

