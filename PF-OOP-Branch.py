#Jim Vargas Painting Figures with OOP

import math
import sys

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY  



class Figure:
    def __init__(self, figure):
        self.r = figure[-1]
        self.x1 = figure[0]
        self.y1 = figure[1]
        self.x2 = figure[2]
        self.y2 = figure[3]






def main():
    n = int(input("Number of figures: ").strip())
    figures = []
    for figures_i in range(n):
        figures_t = [int(figures_temp) for figures_temp in input(("x1, y1, x2, y2, r: figure" + str(figures_i +1) + ": ")).strip().split(' ')]
        figures.append(figures_t)
    print(figures)
    #print(TotalArea(figures))


if __name__ == '__main__':
    main()