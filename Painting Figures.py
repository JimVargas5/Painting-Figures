#Jim Vargas Painting Figures, non OOP

import sys
import math

def main():
    n = int(input("Number of figures: ").strip())
    figures = []
    for figures_i in range(n):
        figures_t = [int(figures_temp) for figures_temp in input(("x1, y1, x2, y2, r: figure" + str(figures_i +1) + ": ")).strip().split(' ')]
        figures.append(figures_t)
    print(figures)
    print(TotalArea(figures))


def distance(x1y1, x2y2):
    dx = x2y2[0] - x1y1[0]
    dy = x2y2[1] - x1y1[1]
    dsquared = dx**2 + dy**2
    dist = dsquared**0.5
    return dist


def FindArea(FigureList):
    """Finds the area of one figure"""
    r = FigureList[-1]
    x1y1 = [FigureList[0], FigureList[1]]
    x2y2 = [FigureList[2], FigureList[3]]
    d = distance(x1y1, x2y2)
    if x1y1 != x2y2:
        return ((math.pi * (r**2)) + (2*r*d))
    else:
        return (math.pi * (r**2))


def TotalArea(TheFigs):
    if len(TheFigs) <=1:
        return FindArea(TheFigs[0])
    else:
        if not DetectOverLap(TheFigs):
            RunningTotal = 0
            for fig in range(len(TheFigs)):
                RunningTotal += FindArea(TheFigs[fig])
            return RunningTotal
        else:
            pass


def DetectOverLap(TheFigs):
    def PrelimCheck():
        """To check to see if any of the figures share a point"""
        #for fig in range(-1, (len(TheFigs)-1), 1):
        pass
    False




if __name__ == '__main__':
    main()