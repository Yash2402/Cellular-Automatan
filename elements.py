import pygame

class Element():
    def __init__(self, cell, color:tuple, element_type = (0, 0, 1)):
        if element_type[0]:
            self.issand = True
            self.isfluid = False
            self.iswall = False
            element = 'sand'
        elif element_type[1]:
            self.isfluid = True
            self.issand = False
            self.iswall = False
            element = 'fluid'
        elif element_type[2]:
            self.isfluid = False
            self.issand = False
            self.iswall = True
            element = 'wall'
        self.element = element
        self.cell = cell
        self.color = color
    def show(self, screen): 
            pygame.draw.rect(screen, (self.color), (self.cell.x, self.cell.y, self.cell.w, self.cell.h))

    
