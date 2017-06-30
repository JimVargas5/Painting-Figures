#Jim Vargas Painting Figures with OOP
#The classes and things

import math
import sys

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY


    def distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dsquared = dx**2 + dy**2
        dist = dsquared**0.5
        return dist


    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)   


class Figure(Point):
    def __init__(self, FigureList):
        self.x1 = FigureList[0]
        self.y1 = FigureList[1]
        self.x1y1 = Point(self.x1,self.y1)

        self.x2 = FigureList[2]
        self.y2 = FigureList[3]
        self.x2y2 = Point(self.x2,self.y2)

        self.r = FigureList[-1]
        self.L = Point.distance(self.x1y1, self.x2y2)

        #TODO more here


    def __str__(self):
        return (
            "["+str(self.x1)+","+str(self.y1)+","+
            str(self.x2)+","+str(self.y2)+","+str(self.r)+"]"
            )


    def FindArea(self):
        """Finds the area of one figure"""
        if self.x1y1 != self.x2y2:
            return ((math.pi * (self.r**2)) + (2*self.r*self.L))
        else:
            return (math.pi * (self.r**2))


    def DetectOverLap(self, other):
        def PrelimCheck():
            """To check to see if any of the figures share a point"""
            #for fig in range(-1, (len(TheFigs)-1), 1):
            pass
        False