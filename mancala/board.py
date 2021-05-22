import pygame
pygame.init()
from .constants import * 
from .stone import Stone
import random

class Board: 
    def __init__(self):
        self.board = []
        self.player1_points = 0
        self.player2_points = 0
        self.create_board()
        self.current_row = 0 
        self.current_col = 0
        self.turn = 0
        self.game_finished = False
    
    def print_turn(self, win):
        font = pygame.font.Font('freesansbold.ttf', 30)
        turn = ('Player 1', 'Player 2')
        text = font.render(turn[self.turn] + ' it\'s your turn!', True, WHITE)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT/2))
        win.blit(text, text_rect)
    
    def check_if_finished(self, win):
        for row in range(ROWS):
            num_stones = 0
            for col in range(1, COLS-1):
                num_stones += len(self.board[row][col])
            if num_stones == 0:
                self.final_move(win)
                if len(self.board[0][0]) > len(self.board[1][7]):
                    winner = 'Player 1'
                else:
                    winner = 'Player 2'
                self.draw_win(win, winner)

    #def pick_winner(self):
        #if len(self.board[0][0]) > len(self.board[0][7]):
            #return 'Player 1'
        #elif len(self.board[0][0]) < len(self.board[0][7]):
            #return 'Player 2'

    def draw_wells(self, win):
        win.fill(BLACK)
        if self.game_finished == False:
            self.print_turn(win)

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 and (col == 0 or col == COLS - 1):
                    if col == COLS -1:
                        pygame.draw.circle(win, GREEN, ((col * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT / 2), 110)
                        #pygame.draw.rect(win, WHITE, [col * RECT_SIZE + 23, RECT_SIZE + RECT_SIZE* 0.55, RECT_SIZE * 0.58, RECT_SIZE*0.30])
                        font = pygame.font.Font('freesansbold.ttf', 40)
                        text = font.render(str(len(self.board[1][7])), True, WHITE)
                        win.blit(text, (col * RECT_SIZE + 90, RECT_SIZE + RECT_SIZE* 0.55 + (RECT_SIZE*0.35)//3))
                    else:
                        pygame.draw.circle(win, GREEN, ((col * RECT_SIZE + RECT_SIZE / 2) + 10, HEIGHT / 2), 110)
                        #pygame.draw.rect(win, WHITE, [col * RECT_SIZE + 43, RECT_SIZE / 8, RECT_SIZE * 0.58, RECT_SIZE*0.30])
                        font = pygame.font.Font('freesansbold.ttf', 40)
                        text = font.render(str(len(self.board[0][0])), True, WHITE)
                        win.blit(text, (col * RECT_SIZE + RECT_SIZE//2, RECT_SIZE // 4))
                
                elif col != 0 and col != COLS - 1:
                    if row == 0:
                        pygame.draw.ellipse(win, RED, [col * RECT_SIZE,  row * RECT_SIZE + 25, RECT_SIZE*0.9, RECT_SIZE*0.70])
                        font = pygame.font.Font('freesansbold.ttf', 25)
                        text = font.render(str(len(self.board[row][col])), True, WHITE)
                        win.blit(text, (col * RECT_SIZE + RECT_SIZE*0.75, 10))
                    else:
                        pygame.draw.ellipse(win, RED, [col * RECT_SIZE,  row * RECT_SIZE + 25, RECT_SIZE*0.9, RECT_SIZE*0.70])
                        font = pygame.font.Font('freesansbold.ttf', 25)
                        text = font.render(str(len(self.board[row][col])), True, WHITE)
                        win.blit(text, (col * RECT_SIZE + 10, RECT_SIZE + RECT_SIZE* 0.50 + (RECT_SIZE*0.55)//2))

    def p1_move(self, stones):
        current_row = 0
        current_col = stones[0][0].col
        self.board[current_row][current_col] = []

        for stone in stones[0]:
            if current_row == 0:
                if current_col > 0:
                    self.board[current_row][current_col - 1].append(stone)
                    stone.move(current_row, current_col - 1)
                    current_col -= 1
                else:
                    current_row += 1
                    self.board[current_row][current_col + 1].append(stone)
                    stone.move(current_row, current_col + 1)    
                    current_col += 1
                    self.player1_points += self.player1_points              
            else: 
                if current_col + 1 < COLS-1:
                    self.board[current_row][current_col + 1].append(stone)
                    stone.move(current_row, current_col + 1)
                    current_col += 1     
                else:
                    current_row = current_row - 1
                    self.board[current_row][current_col].append(stone)
                    stone.move(current_row, current_col)

        if current_row == 0:
            if len(self.board[current_row][current_col]) == 1 and len(self.board[current_row + 1][current_col]) >= 1:
                capture = len(self.board[current_row + 1][current_col]) + 1
                for stone in self.board[current_row][current_col]:
                    self.board[0][0].append(stone)
                    stone.move(0, 0)
                for stone in self.board[current_row + 1][current_col]:
                    self.board[0][0].append(stone)
                    stone.move(0, 0)
                self.board[current_row][current_col] = []
                self.board[current_row + 1][current_col] = []
                self.player1_points += capture 

        #else:
            #if len(self.board[current_row][current_col]) == 1 and len(self.board[current_row - 1][current_col]) >= 1:
               # capture = len(self.board[current_row - 1][current_col]) + 1
              #  for stone in self.board[current_row][current_col]:
                 #   self.board[0][0].append(stone)
                #    stone.move(0, 0)
              #  for stone in self.board[current_row - 1][current_col]:
              #      self.board[0][0].append(stone)
             #       stone.move(0, 0)
              #  self.board[current_row][current_col] = []
             #   self.board[current_row - 1][current_col] = []
             #   self.player1_points += capture 

        self.current_row = current_row
        self.current_col = current_col
        if self.current_col == 0:
            self.turn = 0
        else:
            self.turn = 1

    def p2_move(self, stones):
        current_row = 1
        current_col = stones[0][0].col
        self.board[current_row][current_col] = []
        for stone in stones[0]:
            if current_row == 0:
                if current_col > 1:
                    self.board[current_row][current_col - 1].append(stone)
                    stone.move(current_row, current_col - 1)
                    current_col -= 1
                else:
                    current_row += 1
                    self.board[current_row][current_col].append(stone)
                    stone.move(current_row, current_col)                         
            else: 
                if current_col + 1 < COLS:
                    self.board[current_row][current_col + 1].append(stone)
                    stone.move(current_row, current_col + 1)
                    current_col += 1     
                else:
                    current_row = current_row - 1
                    self.board[current_row][current_col - 1].append(stone)
                    stone.move(current_row, current_col - 1)
                    current_col -= 1
                    self.player2_points += self.player2_points   
        
      #  if current_row == 0:
        #    if len(self.board[current_row][current_col]) == 1 and len(self.board[current_row + 1][current_col]) >= 1:
       #         capture = len(self.board[current_row + 1][current_col]) + 1
         #       for stone in self.board[current_row][current_col]:
          #          self.board[1][7].append(stone)
          #          stone.move(1, 7)
             #   for stone in self.board[current_row + 1][current_col]:
            #        self.board[1][7].append(stone)
           #         stone.move(1, 7)
           #     self.board[current_row][current_col] = []
           #     self.board[current_row + 1][current_col] = []
           #     self.player2_points += capture
        
        if current_row == 1:
            if len(self.board[current_row][current_col]) == 1 and len(self.board[current_row - 1][current_col]) >= 1:
                capture = len(self.board[current_row - 1][current_col]) + 1
                for stone in self.board[current_row][current_col]:
                    self.board[1][7].append(stone)
                    stone.move(1, 7)
                for stone in self.board[current_row - 1][current_col]:
                    self.board[1][7].append(stone)
                    stone.move(1, 7)
                self.board[current_row][current_col] = []
                self.board[current_row - 1][current_col] = []
                self.player2_points += capture

        self.current_row = current_row
        self.current_col = current_col
        if self.current_col == 7:
            self.turn = 1
        else: 
            self.turn = 0

    def move(self, stones):
        if stones[0][0].row == 0 and self.turn == 0:
            self.p1_move(stones)
        
        elif stones[0][0].row == 1 and self.turn == 1:
            self.p2_move(stones)
        
        self.board = self.board

    def final_move(self, win):
        for row in range(ROWS):
            for col in range(1, COLS-1):
                if row == 0:
                    for stone in self.board[row][col]:
                        self.board[0][0].append(stone)
                    self.board[row][col] = []
                else:
                    for stone in self.board[row][col]:
                        self.board[1][7].append(stone)
                    self.board[row][col] = []     
        self.draw(win)
        self.board = self.board
        self.game_finished = True
    
    def get_stones(self, row, col):
        return (self.board[row][col], row)

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append([])
                if col != 0 and col != COLS - 1:
                    for i in range(4):
                        self.board[row][col].append(Stone(row, col, random.choice(COLORS)))

    def draw(self, win):
        self.draw_wells(win)
        for row in range(ROWS):
            for col in range((COLS)):
                stones = self.board[row][col]
                for stone in stones:
                    stone.draw(win)
    
    def draw_win(self, win, player):
        self.draw(win)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render(player + ' WINS!', True, WHITE)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT/2))
        win.blit(text, text_rect)
        
    def draw_path(self, stones, win):
        self.draw(win)
        pot_stone = stones[0][0]
        pot_row = pot_stone.row
        pot_col = pot_stone.col
        
        if pot_stone.row == 0 and self.turn == 0:
            for stone in stones[0]:
                if pot_row == 0:
                    if pot_col > 1:
                        pygame.draw.circle(win, P1, (((pot_col - 1) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT / 4), 8)
                        pot_col -= 1

                    elif pot_col == 1:
                        pygame.draw.circle(win, P1, (((pot_col - 1) * RECT_SIZE + RECT_SIZE / 2), HEIGHT / 2), 8)
                        pot_col -= 1

                    else:
                        pot_row += 1
                        pygame.draw.circle(win, P1, (((pot_col + 1) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT * 0.75), 8)
                        pot_col += 1              
                else: 
                    if pot_col + 1 < COLS-1:
                        pygame.draw.circle(win, P1, (((pot_col + 1) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT * 0.75), 8)
                        pot_col += 1     
                    else:
                        pot_row = pot_row - 1
                        pygame.draw.circle(win, P1, (((pot_col) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT / 4), 8)

        elif pot_stone.row == 1 and self.turn == 1:
            for stone in stones[0]:
                if pot_row == 0:
                    if pot_col > 1:
                        pygame.draw.circle(win, P2, (((pot_col - 1) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT / 4), 8)
                        pot_col -= 1
                    else:
                        pot_row += 1
                        pygame.draw.circle(win, P2, (((pot_col) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT * 0.75), 8)   
                                 
                else: 
                    if pot_col + 1 < COLS - 1:
                        pygame.draw.circle(win, P2, (((pot_col + 1) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT * 0.75), 8)
                        pot_col += 1     
                    
                    elif pot_col + 1 == COLS - 1:
                        pygame.draw.circle(win, P2, (((pot_col + 1) * RECT_SIZE + RECT_SIZE / 2), HEIGHT / 2), 8)
                        pot_col += 1

                    else:
                        pot_row -= 1
                        pygame.draw.circle(win, P2, (((pot_col - 1) * RECT_SIZE + RECT_SIZE / 2) - 15, HEIGHT / 4), 8) 
                        pot_col -= 1   
        