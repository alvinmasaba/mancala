import pygame

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1800, 450
ROWS, COLS = 2, 8
RECT_SIZE = WIDTH//COLS 

# rgb
RED = (168, 66, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (108, 163, 110)
GREY = (128, 128, 128)
HI_YELLOW = (255, 214, 102)
PURPLE = (160, 129, 227)
PINK = (227, 129, 217)
LIGHT_RED = (222, 91, 91)
HI_BLUE = (91, 152, 222)
HI_GREEN = (91, 222, 145)
SILVER = (159, 191, 172)
GOLD = (242, 191, 73)
MAUVE = (48, 14, 14)
AQUA = (16, 130, 84)
MILK = (182, 209, 198)

COLORS = (GREY, HI_YELLOW, HI_GREEN, HI_BLUE, SILVER, GOLD, MAUVE, AQUA, MILK, PINK, PURPLE)

#RED_STONE = pygame.transform.scale(pygame.image.load('mancala demo/assets/redstone.jpg'), (35, 25))

PLAYERS = (0, 1)

P1 = (0, 255, 26)
P2 = (255, 15, 83)

pygame.mixer.music.load('mancala demo/theme.mp3')




