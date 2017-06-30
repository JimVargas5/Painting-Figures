#Jim Vargas Painting Figures with OOP
#basically the main

import math
import sys
from Class_List import Point, Figure

def main():
    n = int(input("Number of figures: ").strip())
    if n <= 0:
        print("You need a real and positive number of figures.")
        exit()

    figures = []
    for figures_i in range(n):
        figures_t = [int(figures_temp) for figures_temp in input(("x1 y1 x2 y2 r: figure" + str(figures_i +1) + ": ")).strip().split(' ')]
        figures.append(figures_t)

    for i in range(len(figures)):
        new = Figure(figures[i])
        figures[i] = new

    for p in range(len(figures)):
        print(("Figure"+str(p+1)+": "), figures[p])

    print("Total Area:", TotalArea(figures))


def TotalArea(TheFigs):
    if len(TheFigs) <=1:
        return Figure.FindArea(TheFigs[0])
    else:
        #TODO fith this messssss
        if not Figure.DetectOverLap(TheFigs[0], TheFigs[1]):
            RunningTotal = 0
            for fig in range(len(TheFigs)):
                RunningTotal += Figure.FindArea(TheFigs[fig])
            return RunningTotal
        else:
            pass


if __name__ == '__main__':
    main()