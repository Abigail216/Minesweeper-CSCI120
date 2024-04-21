import pygame #importing lobby
import os #importing oppertating system


# Initialize Pygame
pygame.init()


#window size
width = 800
height = 800
window = pygame.display.set_mode((width, height)) #just displaying obviously. Don't neccessarily need width & height but more for organization.
pygame.display.set_caption("Mine Sweeper") #Top bar (like where x, minimize, full window go)
white = (200, 200, 200)


# Limit the frame rate
pygame.time.Clock().tick(60)


#formatting the grid
def grid_formatting(): #found this code from Stack Overflow
    blocksize = 20  
    for x in range(0, width, blocksize):
        for y in (0, height, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(window, white, rect, 1)
#is bringing up the window but quickly goes away.
