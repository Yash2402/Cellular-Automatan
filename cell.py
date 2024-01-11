import random
import pygame


class Cell():
    
    def __init__(self, index, rect:tuple, element):
        self.x = rect[0]
        self.y = rect[1]
        self.i = index[0]
        self.j = index[1]
        self.w = rect[2]
        self.h = rect[3]
        self.element = element
        # self.offset = 
    def show(self, screen):
        if self.element == 'air':
            self.color = (255, 255, 255)
        elif self.element == 'sand':
            self.color = (243, 175, 61)
        elif self.element == 'fluid':
            self.color = (127, 166, 248)
        elif self.element == 'smoke':
            self.color = (200, 200, 200)
        elif self.element == 'wall':
            self.color = (78, 78, 78)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
            

    def neighbour(self, cells):
        if  (self.i != len(cells)-1 and self.i != 0) and (self.j != len(cells[self.i])-1 and self.j != 0):
            return {
                'top'        :cells[ self.i ][self.j-1], 
                'topleft'    :cells[self.i-1][self.j-1], 
                'topright'   :cells[self.i+1][self.j-1], 
                'bottom'     :cells[ self.i ][self.j+1], 
                'bottomleft' :cells[self.i-1][self.j+1], 
                'bottomright':cells[self.i+1][self.j+1], 
                'left'       :cells[self.i-1][ self.j ], 
                'right'      :cells[self.i+1][ self.j ]
                }

    @staticmethod
    def update(cells):
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                if (i != len(cells) or i != 0) or (j != len(cells[0]) or j != 0):
                    nextgen = cells
                    cell = cells[i][j]
                    if cell.element == 'air':
                            continue
                    
                    neighbours = cell.neighbour(cells)
                    if cell.element == 'smoke':
                        if neighbours['top'].element == 'air':
                            nextgen[i][j].element = neighbours['top'].element
                            nextgen[i][j-1].element = 'smoke'
                        elif ((neighbours[   'top'   ].element == 'wall' or neighbours['top'].element == 'smoke')
                            and  neighbours[ 'topleft' ].element == 'air' 
                            and  neighbours[ 'topright'].element == 'air'):

                            if neighbours['left'].element == 'air' and neighbours['right'].element == 'wall':

                                nextgen[i][j].element = neighbours['topleft']
                                nextgen[i-1][j-1].element = 'smoke'

                            elif neighbours['left'].element == 'wall' and neighbours['right'].element == 'air':
                                    
                                nextgen[i][j].element = neighbours['topright']
                                nextgen[i+1][j-1].element = 'smoke'

                            elif neighbours['left'].element == 'air' and neighbours['right'].element == 'air':

                                probality = random.randint(0, 1)
                                if probality:

                                    nextgen[i][j].element = neighbours['topright']
                                    nextgen[i+1][j-1].element = 'smoke'
                                else:

                                    nextgen[i][j].element = neighbours['topleft']
                                    nextgen[i-1][j-1].element = 'smoke'
                                    
                            else: pass

                        elif ((neighbours[   'top'  ].element == 'wall' or neighbours['top'].element == 'smoke')
                            and (neighbours[ 'topleft'].element == 'wall' or neighbours['topleft'].element == 'smoke')
                            and  neighbours['topright'].element == 'air'):
                            if neighbours['right'].element == 'air':

                                nextgen[i][j].element = neighbours['topright']
                                nextgen[i+1][j-1].element = 'smoke'
                            if neighbours['left'].element == 'air' and neighbours['right'].element == 'wall':

                                nextgen[i][j].element = neighbours['left']
                                nextgen[i-1][j].element = 'smoke'

                        elif ((neighbours[   'top'  ].element == 'wall' or neighbours['top'].element == 'smoke')
                            and  neighbours[ 'topleft'].element == 'air' 
                            and (neighbours['topright'].element == 'wall' or neighbours['topright'].element == 'smoke')):

                            if neighbours['left'].element == 'air':

                                nextgen[i][j].element = neighbours['topleft']
                                nextgen[i-1][j-1].element = 'smoke'

                            if neighbours['right'].element == 'air' and neighbours['left'].element == 'wall':

                                nextgen[i][j].element = neighbours['right']
                                nextgen[i+1][j].element = 'smoke'

                        elif ((neighbours[   'top'  ].element == 'wall' or neighbours['top'].element == 'smoke')
                            and (neighbours[ 'topleft'].element == 'wall' or neighbours['topleft'].element == 'smoke')
                            and (neighbours['topright'].element == 'wall' or neighbours['topright'].element == 'smoke')):

                            if ((neighbours['left'].element == 'wall' or neighbours['left'].element == 'smoke') 
                                and neighbours['right'].element == 'air'):
                                    
                                nextgen[i][j].element = neighbours['right']
                                nextgen[i+1][j].element = 'smoke'

                            elif ((neighbours['right'].element == 'wall' or neighbours['right'].element == 'smoke') 
                                and neighbours['left'].element == 'air'): 
                                    
                                nextgen[i][j].element = neighbours['left']
                                nextgen[i-1][j].element = 'smoke'

                            elif (neighbours['left'].element == 'air' and neighbours['right'].element == 'air'):

                                probality = random.randint(-1, 1)

                                if probality < 0:

                                    nextgen[i][j].element = neighbours['right']
                                    nextgen[i+1][j].element = 'smoke'

                                else:

                                    nextgen[i][j].element = neighbours['left']
                                    nextgen[i-1][j].element = 'smoke'

                        else: pass
                    if cell.element == 'sand':
                        if neighbours['bottom'].element == 'air':
                            nextgen[i][j].element = 'air'
                            nextgen[i][j+1].element = 'sand'
                            
                        elif neighbours['bottom'].element == 'fluid':
                            nextgen[i][j].element = nextgen[i][j+1].element
                            nextgen[i][j+1].element = 'sand'

                        elif ((neighbours[   'bottom'   ].element == 'wall' or neighbours['bottom'].element == 'sand')
                            and (neighbours[ 'bottomleft' ].element == 'air' or neighbours[ 'bottomleft' ].element == 'fluid')
                            and (neighbours[ 'bottomright'].element == 'air' or neighbours[ 'bottomright' ].element == 'fluid')):

                            if neighbours['left'].element == 'air' and neighbours['right'].element == 'wall':
                                    nextgen[i][j].element = nextgen[i-1][j+1].element
                                    nextgen[i-1][j+1].element = 'sand'

                            elif neighbours['left'].element == 'wall' and neighbours['right'].element == 'air':
                                nextgen[i][j].element = nextgen[i+1][j+1].element
                                nextgen[i+1][j+1].element = 'sand'

                            elif neighbours['left'].element == 'wall' and neighbours['right'].element == 'wall':
                                pass

                            elif neighbours['left'].element == 'air' and neighbours['right'].element == 'air':
                                nextgen[i][j].element = 'air'
                                probality = random.randint(0, 1)
                                    
                                if probality:
                                    nextgen[i+1][j+1].element = 'sand'
                                else:
                                    nextgen[i-1][j+1].element = 'sand'

                        elif ((neighbours[   'bottom'  ].element == 'wall' or neighbours['bottom'].element == 'sand')
                            and (neighbours[ 'bottomleft'].element == 'wall' or neighbours['bottomleft'].element == 'sand')
                            and (neighbours['bottomright'].element == 'air' or neighbours[ 'bottomright' ].element == 'fluid')):

                            if neighbours['right'].element == 'air':
                                nextgen[i][j].element = nextgen[i+1][j+1].element
                                nextgen[i+1][j+1].element = 'sand'
                            if neighbours['left'].element == 'air' and neighbours['right'].element == 'wall':
                                nextgen[i][j].element = nextgen[i-1][j].element
                                nextgen[i-1][j].element = 'sand'

                        elif ((neighbours[   'bottom'  ].element == 'wall' or neighbours[   'bottom'  ].element == 'sand')
                                and (neighbours[ 'bottomleft'].element == 'air' or neighbours[ 'bottomleft' ].element == 'fluid')
                                and (neighbours['bottomright'].element == 'wall' or neighbours['bottomright'].element == 'sand')):

                            if neighbours['left'].element == 'air':
                                nextgen[i][j].element = nextgen[i-1][j+1].element
                                nextgen[i-1][j+1].element = 'sand'
                            if neighbours['right'].element == 'air' and neighbours['left'].element == 'wall':
                                nextgen[i][j].element = nextgen[i+1][j].element
                                nextgen[i+1][j].element = 'sand'

                        else:
                            pass
                    if cell.element == 'fluid':

                        if neighbours['bottom'].element == 'air':
                                
                            nextgen[i][j].element = nextgen[i][j+1].element
                            nextgen[i][j+1].element = 'fluid'

                        elif ((neighbours[   'bottom'   ].element == 'wall' or neighbours[   'bottom'  ].element == 'sand' or neighbours['bottom'].element == 'fluid')
                                and  neighbours[ 'bottomleft' ].element == 'air' 
                                and  neighbours[ 'bottomright'].element == 'air'):

                            if neighbours['left'].element == 'air' and neighbours['right'].element == 'wall':
                                nextgen[i][j].element = nextgen[i-1][j+1].element
                                nextgen[i-1][j+1].element = 'fluid'
                            elif neighbours['left'].element == 'wall' and neighbours['right'].element == 'air':
                                nextgen[i][j].element = nextgen[i+1][j+1].element
                                nextgen[i+1][j+1].element = 'fluid'
                            elif neighbours['left'].element == 'wall' and neighbours['right'].element == 'wall': pass
                            elif neighbours['left'].element == 'air' and neighbours['right'].element == 'air':
                                nextgen[i][j].element = 'air'
                                probality = random.randint(0, 1)

                                if probality:
                                    nextgen[i+1][j+1].element = 'fluid'
                                else:
                                    nextgen[i-1][j+1].element = 'fluid'

                        elif ((neighbours[   'bottom'  ].element == 'wall' or neighbours['bottom'].element == 'sand' or neighbours['bottom'].element == 'fluid')
                                and (neighbours[ 'bottomleft'].element == 'wall' or neighbours['bottomleft'].element == 'sand' or neighbours['bottomleft'].element == 'fluid')
                                and  neighbours['bottomright'].element == 'air'):

                            if neighbours['right'].element == 'air':
                                nextgen[i][j].element = nextgen[i+1][j+1].element
                                nextgen[i+1][j+1].element = 'fluid'
                            if neighbours['left'].element == 'air' and neighbours['right'].element == 'wall':
                                nextgen[i][j].element = nextgen[i-1][j].element
                                nextgen[i-1][j].element = 'fluid'

                        elif ((neighbours[   'bottom'  ].element == 'wall' or neighbours[   'bottom'  ].element == 'sand' or neighbours[   'bottom'  ].element == 'fluid')
                                and  neighbours[ 'bottomleft'].element == 'air' 
                                and (neighbours['bottomright'].element == 'wall' or neighbours['bottomright'].element == 'sand' or neighbours['bottomright'].element == 'fluid')):

                            if neighbours['left'].element == 'air':
                                nextgen[i][j].element = nextgen[i-1][j+1].element
                                nextgen[i-1][j+1].element = 'fluid'
                            if neighbours['right'].element == 'air' and neighbours['left'].element == 'wall':
                                nextgen[i][j].element = nextgen[i+1][j].element
                                nextgen[i+1][j].element = 'fluid'
                        elif ((neighbours[   'bottom'  ].element == 'wall' or neighbours['bottom'].element == 'sand' or neighbours['bottom'].element == 'fluid')
                            and (neighbours[ 'bottomleft'].element == 'wall' or neighbours['bottomleft'].element == 'sand' or neighbours['bottomleft'].element == 'fluid')
                            and (neighbours['bottomright'].element == 'wall' or neighbours['bottomright'].element == 'sand' or neighbours['bottomright'].element == 'fluid')):

                            if ((neighbours['left'].element == 'wall' 
                                or neighbours['left'].element == 'sand' 
                                or neighbours['left'].element == 'fluid') 
                                and neighbours['right'].element == 'air'):
                                nextgen[i][j].element = nextgen[i+1][j].element
                                nextgen[i+1][j].element = 'fluid'

                            elif (neighbours['left'].element == 'air' 
                                and (neighbours['right'].element == 'wall' 
                                or neighbours['right'].element == 'sand' 
                                or neighbours['right'].element == 'fluid')): 
                                    
                                nextgen[i][j].element = nextgen[i-1][j].element
                                nextgen[i-1][j].element = 'fluid'

                            elif (neighbours['left'].element == 'air' 
                                and neighbours['right'].element == 'air'):
                                probality = random.randint(-1, 1)
                                if probality < 0:
                                    nextgen[i][j].element = nextgen[i+1][j].element
                                    nextgen[i+1][j].element = 'fluid'
                                else:
                                    nextgen[i][j].element = nextgen[i-1][j].element
                                    nextgen[i-1][j].element = 'fluid'

                        else: pass
        return nextgen
