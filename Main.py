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

# font
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('1', True, green, blue)

running = True 
while running: 
   pygame.time.Clock().tick(60)
    blocksize = 20  #Reads each of the rectanges as individauls 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   for x in range(100, width - 100, blocksize): #100 and -100 just adjust where the blocks are
        for y in range(100, height - 100, blocksize):
            rect = pygame.Rect(x , y , blocksize, blocksize)
            pygame.draw.rect(window, white, rect, 1) 
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONUP: 
            start = event.pos 
            print("start", start)
            x = 40
            y = 130
            if start[0] in range(x,y) and start[1] in range (x, y): 
                rect = pygame.draw.rect(window, white, (40, 40, 90, 90))
                rectcenter = 75, 75
                window.blit(text, rectcenter)
    pygame.display.update() 
    
