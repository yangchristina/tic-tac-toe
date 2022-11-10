# Import and initialize the pygame library
import pygame as pg
import sys
from pygame.locals import *

pg.init()

width = 750
height = width


piece_size = (width - 100) / 3

horizontal_offset = (width+25) / 3 + 15

# 0 0 => (15, 15)
# 1 0 (z)
# 0, 1 => 
def applyOffset(x, y):
    return ((width+20) / 3 * x + 15, (width+20) / 3 * y + 15)

# Set up the drawing window
screen = pg.display.set_mode([width, height])

# set the pygame window name
pg.display.set_caption('Tic Tac Toe')

# create a surface object, image is drawn on it.
imp_board = pg.image.load("./board.png")
imp_board = pg.transform.scale(imp_board, (width, height)).convert()


# piece images
imp_o = pg.image.load("./O.png")
imp_o = pg.transform.scale(imp_o, (piece_size, piece_size)).convert()

imp_x = pg.image.load("./X.png")
imp_x = pg.transform.scale(imp_x, (piece_size, piece_size)).convert()

# color background white
screen.fill((255, 255, 255))

# Using blit to copy content from one surface to other; blit to copy imp onto screen
screen.blit(imp_board, (0, 0))

# paint screen one time; flip = update screen
pg.display.flip()

# Run until the user asks to quit
running = True
while running: 

    #   
    screen.blit(imp_o, applyOffset(0, 0))
    screen.blit(imp_o, applyOffset(1, 0))
    screen.blit(imp_o, applyOffset(2, 0))
    screen.blit(imp_x, applyOffset(0, 0))
    screen.blit(imp_x, applyOffset(0, 1))
    screen.blit(imp_x, applyOffset(0, 2))
    screen.blit(imp_x, applyOffset(1, 1))
    screen.blit(imp_x, applyOffset(2, 1))
    screen.blit(imp_x, applyOffset(2, 2))
    screen.blit(imp_o, applyOffset(1, 2))
    # Did the user click the window close button?

    if pg.mouse.get_pressed():
        print('pressed')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            print(pos)
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            print('down')
            print(pos)

    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
