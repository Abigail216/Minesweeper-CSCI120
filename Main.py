import pygame #importing lobby
import os #importing oppertating system
import random


class Box: 
    def __init__(self, x, y, blocksize, is_bomb) -> None:
        self.x = x
        self.y = y 
        self.blocksize = blocksize 
        self.rect = pygame.Rect(x , y, blocksize, blocksize)
        self.color = white
        self.is_bomb = is_bomb
        self.bombs = 0

# Initialize Pygame
pygame.init()

#window size
width = 800
height = 800
window = pygame.display.set_mode((width, height)) #just displaying obviously. Don't neccessarily need width & height but more for organization.
pygame.display.set_caption("Mine Sweeper") #Top bar (like where x, minimize, full window go)

#colors
white = (200, 200, 200)
green = (0, 255, 0)
blue = (0, 0, 128) 
red = (255, 0, 0) 
black = (0, 0, 0)


# font
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('1', True, green, blue)

#creating the bombs
BOMB_COUNT = (30,50) #for how many bombs will be created. 
blocksize = 50  #Reads each of the rectanges as individauls 
running = True 
BOXES = [] #creating a list of boxes. Also keeps the boxes as individuals.

for x in range(100, width - 100, blocksize): #100 and -100 just adjust where the blocks are
    row = []
    for y in range(100, height - 100, blocksize):
        new_box = Box(x, y, blocksize, False)
        row.append(new_box) #referring back the lists. 
        #this makes the boxes before the loops. 
    BOXES.append(row)

for bomb in range(random.randrange(BOMB_COUNT[0], BOMB_COUNT[1] + 1)): #makes sure the bombs are within the grid itself. 
    bomb_row = random.randrange(0,len(BOXES))
    bomb_col = random.randrange(0,len(BOXES))
    #BOXES[bomb_row][bomb_col].color = red #will currently show where bombs are as red. 
    BOXES[bomb_row][bomb_col].is_bomb = True 

direction = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)] #checking to see how close bomb is (so basically 1 away). If there is touching more than 1, it is noted. 
for row in range(len(BOXES)):
    for col in range(len(BOXES[row])):
        counter = 0
        for item in direction:
            if 0 <= row + item[0] < len(BOXES) and 0 <= col + item[1] < len(BOXES):
                if BOXES[row + item[0]][col + item[1]].is_bomb == True:
                    counter += 1
        BOXES[row][col].bombs = counter #checking for the bombs


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: 
            pos = pygame.mouse.get_pos()
            for row in BOXES:
                for box in row:
                    if box.rect.collidepoint(pos):
                        clicked_box = box
            if clicked_box: #makes sure nothing happens if area that isn't a boxed is clicked it doesn't do anything. Also fills box.
                if clicked_box.is_bomb:   
                    print("You're dead") 
                    clicked_box.color = red
                else: 
                    clicked_box.color = green
                    print(pos, clicked_box.bombs)
            
            
                    
                #all of this checks to see if there is a collision within the box. These are empty boxes. 
            # start = event.pos 
            # print("start", start)
            # x = 40
            # y = 130
            # if start[0] in range(x,y) and start[1] in range (x, y): 
            #     rect = pygame.draw.rect(window, white, (40, 40, 90, 90))
            #     rectcenter = 75, 75
            #     window.blit(text, rectcenter)
    
    window.fill((0, 0, 0))
    for row in BOXES:
        for box in row:
            if box.color == white:
                pygame.draw.rect(window, box.color, box.rect, 1) #this helps store each of the boxes. Rerenders the boxes in the boxes list. 
            else: 
                pygame.draw.rect(window, box.color, box.rect) #referring back to elif event. 
    pygame.display.update()
    pygame.time.Clock().tick(60)
   
#need to show num. of bombs. Bombs are showing. 
#that is num. of bombs surrounding that box. 
#Next step is make sure the 
#DFS- def first search. Checks for connections. How far can I go with that? (Should be used to create the "flood zone".)