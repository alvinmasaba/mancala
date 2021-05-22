import pygame
pygame.init()
from mancala.constants import WIDTH, HEIGHT, RECT_SIZE, PLAYERS, THEME
from mancala.board import Board
from mancala.game import Game

FPS = 60 # frames per second

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mancala')
pygame.mixer.music.set_volume(0.10)

def get_row_col_from_mouse(pos):
    x, y = pos 
    row = y // RECT_SIZE
    col = x // RECT_SIZE
    return row, col 

def main():
    run = True 
    clock = pygame.time.Clock() # so game plays at same speed on all computers
    game = Game(WIN, PLAYERS)
    show_path = False
    pygame.mixer.music.play(-1)

    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if col in range(1,7):
                    stones = game.board.get_stones(row, col)
                    if stones[0] != []:
                        game.pathway(stones)
                        show_path = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if col in range(1,7):
                    stones = game.board.get_stones(row, col)
                    if stones[0] != []:
                        game.board.move(stones)
                        game.update()        
            
            if not show_path:
                game.update()
                    

    pygame.quit()


main()
