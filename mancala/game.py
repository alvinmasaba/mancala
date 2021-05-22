import pygame
from pygame.constants import *
from .constants import *
from .board import *

class Game: 
    def __init__(self, win, players):
        self._init()
        self.win = win
        self.turn = players[0]

    def update(self):
        self.board.draw(self.win)
        self.board.check_if_finished(self.win)
        pygame.display.update()
    
    def pathway(self, stones):
        self.board.draw_path(stones, self.win)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
             
    def reset(self):
        self._init()

    #def select(self, row, col):
        #if self.selected:
          #  result = self._move(row, col)
            #if not result: 
                #self.selected = None
                #self.select(row, col)
        
        #stones = self.board.get_stones(row, col)
        
#        if stones[0] != [] and stones[1] == self.turn:
#            self.selected = stones
#            self.valid_moves = self.board.get_valid_moves(stones[0])
 ##           return True
        
  #      return False

   # def _move(self, row, col):
  #      stones = self.board.get_stones(row, col)
    #    if self.selected and stones[0] == [] and (row, col) in self.path:
   #         self.board.move(stones)
   #         self.change_turn()
   #     else:
   #         return False
        
     #   return True

 #   def change_turn(self):
  #      if self.turn == 0 and self.board.current_col != 0:
    #        self.turn = 1
    #    elif self.turn == 1 and self.board.current_col != 7:
     #       self.turn = 0
    
    
          
    
          