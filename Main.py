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
        self.is_flagged = False

    def draw_flag(self, window, flag_image):
        if self.is_flagged: 
            window.blit(flag_image, self.rect.topleft)

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

flag_image = pygame.image.load(os.path.join('Assets', 'flag.png'))
flag = pygame.transform.scale(flag_image, (35, 35))
flag_dest = (blocksize/2, blocksize/2)

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
            if event.type == pygame.MOUSEBUTTONUP: 
                    if not clicked_box.is_flagged: 
                        clicked_box.is_flagged = True 
                        clicked_box.draw_flag(window, flag)
                        pygame.display.update(box.rect)
                    else: 
                        clicked_box.is_flagged = False 
                        box.draw_flag(window, white, box.rect)
                        pygame.display.update(box.rect)
