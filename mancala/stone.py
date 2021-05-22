from .constants import *
import random
import pygame

# random.randint(32, 218), random.randint(32, 218), random.randint(32, 218)

class Stone:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        #if self.row == 0:
            #self.direction = -1
        #else:
            #self.direction = 1

        self.x = 0 
        self.y = 0 
        self.calc_pos()

    def calc_pos(self):
        self.x = (RECT_SIZE * self.col + RECT_SIZE // 2) + int(random.uniform(-0.22, 0.22) * RECT_SIZE) 
        self.y = (RECT_SIZE * self.row + RECT_SIZE // 2) + int(random.uniform(-0.22, 0.22) * RECT_SIZE)
    
    def calc_score(self):
        if self.col == 0:
            self.x = (RECT_SIZE * self.col + RECT_SIZE // 2) + int(random.uniform(-0.20, 0.20) * RECT_SIZE) 
            self.y = (RECT_SIZE * self.row + RECT_SIZE) + int(random.uniform(-0.20, 0.20) * RECT_SIZE)
        else:
            self.x = (RECT_SIZE * self.col + RECT_SIZE // 2) + int(random.uniform(-0.20, 0.20) * RECT_SIZE) 
            self.y = (RECT_SIZE * self.row + RECT_SIZE // 8) + int(random.uniform(-0.20, 0.20) * RECT_SIZE)
    
    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.x, self.y), 18)
        pygame.draw.circle(win, self.color, (self.x, self.y), 14)
        #if self.color == HI_YELLOW:
            #win.blit(RED_STONE, (self.x - RED_STONE.get_width()//2, self.y - RED_STONE.get_height()//2))
    
    def move(self, row, col):
        self.row = row
        self.col = col

        if self.col in range(1,7):
            self.calc_pos()
        
        else:
            self.calc_score()


    def __repr__(self):
        return str(self.color)
    
    

