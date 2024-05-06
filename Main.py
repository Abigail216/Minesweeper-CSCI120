import pygame #importing lobby
import os #importing oppertating system
import random

#Creating the board
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
        self.row = -1
        self.col = -1
        self.open = False

    def set_row_col(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return f'Box: row{self.row}, col:{self.col}'
          
# Initialize Pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

#window size
width = 800
height = 800
window = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Mine Sweeper") 

#colors
white = (200, 200, 200)
green = (0, 255, 0)
blue = (0, 0, 128) 
red = (255, 0, 0) 
black = (0, 0, 0)

# font & directions
font = pygame.font.Font('freesansbold.ttf', 32)
smallfont = pygame.font.Font('freesansbold.ttf', 20)
directionsline1 = smallfont.render('This is a traditional minesweeper game.', True, white, black)
directionsline2 = smallfont.render('30 bombs are hidden within the gameboard', True, white, black)
directionsline3 = smallfont.render("Left click to clear the box. Right click to mark a flag. 'Q' to quit.", True, white, black)
directionsline4 = smallfont.render("Don't hit the bombs!", True, white, black)

#creating the bombs
BOMB_COUNT = (30,30)
blocksize = 50  
running = True 
winning = False
gameover = False
BOXES = [] 
FLAGS = BOMB_COUNT[0]
FLAGS2 = FLAGS

#Finding the boxes
def find_all(r, c):
    direction = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    used = []
    stack = []
    stack.append(BOXES[r][c])
    while stack:
        box = stack.pop(-1)
        print(box)
        box.open = True
        box.color = (220,220,220)
        row = box.row
        col = box.col
        used.append(box)
        for item in direction:  
            if 0 <= row + item[0] < len(BOXES) and 0 <= col + item[1] < len(BOXES):
                if BOXES[row + item[0]][col + item[1]].bombs == 0 and BOXES[row + item[0]][col + item[1]].is_bomb == False:
                    if (BOXES[row + item[0]][col + item[1]] not in used and BOXES[row + item[0]][col + item[1]] not in stack):
                        stack.append(BOXES[row + item[0]][col + item[1]])
                elif BOXES[row + item[0]][col + item[1]].bombs != 0 and BOXES[row + item[0]][col + item[1]].is_bomb == False:
                    BOXES[row + item[0]][col + item[1]].open = True
                    BOXES[row + item[0]][col + item[1]].color = (220,220,220)
          
#Customizing the boxes more
row_index = 0
for y in range(100, height - 100, blocksize): 
    row = []
    col_index = 0
    for x in range(100, width - 100, blocksize):
        new_box = Box(x, y, blocksize, False)
        new_box.set_row_col(row_index, col_index)
        row.append(new_box) 
        col_index += 1
    BOXES.append(row)
    row_index += 1

#Bomb creation
for bomb in range(random.randrange(BOMB_COUNT[0], BOMB_COUNT[1] + 1)):
    bomb_row = random.randrange(0,len(BOXES))
    bomb_col = random.randrange(0,len(BOXES))
    BOXES[bomb_row][bomb_col].is_bomb = True 

#Checks for the bombs in the boxes next to it. 
direction = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]  
for row in range(len(BOXES)):
    for col in range(len(BOXES[row])):
        counter = 0
        for item in direction:
            if 0 <= row + item[0] < len(BOXES) and 0 <= col + item[1] < len(BOXES):
                if BOXES[row + item[0]][col + item[1]].is_bomb == True:
                    counter += 1
        BOXES[row][col].bombs = counter 

#Flag information
flag_image = pygame.image.load(os.path.join('CSCI Final','Assets', 'flag.png'))
flag = pygame.transform.scale(flag_image, (40, 40))
flag_dest = (blocksize//2, blocksize//2)
flag_x = 100
flag_y = 50
flag_font = pygame.font.Font('freesansbold.ttf', 20)

#Win screen 
def checkWin():
    for row in BOXES:
        for box in row:
            if box.open == True or box.is_bomb == True:
                continue
            else:
                return False
            
    return True

#Game initiation
while running: 
    window.fill((0, 0, 0)) 
    flag_score = font.render(f'Flags remaining: {FLAGS} / {FLAGS2}', True, white)
    window.blit (flag_score, (flag_x, flag_y))
    window.blit(directionsline1, (100, 707))
    window.blit(directionsline2, (100, 727))
    window.blit(directionsline3, (100, 747))
    window.blit(directionsline4, (100, 767))
    for event in pygame.event.get():
        if checkWin():
            winning = True
            running = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q: 
                running = False 
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_box = None
            for row in BOXES:
                for box in row:
                    if box.rect.collidepoint(pos):
                        clicked_box = box
            if clicked_box and event.button == 1: 
                if clicked_box.is_bomb:  
                    running = False
                    gameover = True 
                    clicked_box.color = red
                else: 
                    find_all(clicked_box.row, clicked_box.col)
                    print(pos, clicked_box.bombs)  
                    print(clicked_box.row, clicked_box.col)
            elif clicked_box and event.button == 3: 
                    if not clicked_box.is_flagged: 
                        if FLAGS > 0:
                            clicked_box.is_flagged = True
                            FLAGS -= 1
                    else: 
                        clicked_box.is_flagged = False 
                        FLAGS += 1

#Box and flag check
    for row in BOXES:
        for box in row:                
            if box.color == white:
                pygame.draw.rect(window, box.color, box.rect, 1)
            else: 
                pygame.draw.rect(window, box.color, box.rect) 
                pygame.draw.rect(window, white, box.rect,1) 
                if box.bombs != 0 and box.is_bomb == False:
                    w, h = font.size(str(box.bombs))
                    text = font.render(str(box.bombs),False, (105, 105, 105))
                    window.blit(text, (box.x + (50 - w) // 2, box.y + (50 - h) //2 ))

            if box.is_flagged == True:
                pygame.draw.rect(window, box.color, box.rect, 1) == False
                pygame.draw.rect(window, box.color, box.rect) == False
                pygame.draw.rect(window, white, box.rect,1) == False
                window.blit(flag, (box.x+5, box.y+5))
            
    pygame.display.update()
    pygame.time.Clock().tick(60)

#end sequence text initialization
endfont = pygame.font.Font('freesansbold.ttf', 40)
gameOvertext = endfont.render('Game Over. You hit a mine!', True, red, black)
endfont = pygame.font.Font('freesansbold.ttf', 40)
winText = endfont.render('You won!', True, green, black)

#losing sequence loop
while gameover == True: 
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            gameover = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: 
               running = False 
               gameover = False #press q to quit. 
   window.fill((0,0,0))
   window.blit(gameOvertext, (140, 375))
   pygame.display.update()
   pygame.time.Clock().tick(60)

#winning sequence loop. 
while winning == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            winning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: 
                running = False 
                winning = False 
    window.fill((0,0,0))
    window.blit(winText, (305, 365))
    pygame.display.update()
    pygame.time.Clock().tick(60)
