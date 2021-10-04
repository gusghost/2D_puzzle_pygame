from numpy.core.records import array
import pygame
import numpy
import stageMap 
from stage_variable import *
import os

pygame.init()

#create screen
screen = pygame.display.set_mode((1176,664))

#caption and Icon
image_directry = os.path.normpath("E:/picture/puzzle/pygame_sand/image/")
pygame.display.set_caption("ZIKKEN")
icon = pygame.image.load("karicon.png")
pygame.display.set_icon(icon)
sc_width = pygame.display.get_window_size()[0]
sc_height = pygame.display.get_window_size()[1]

#Player
stage_num = 5
selected_stage = stageMap.stage_gene(stage_num,sc_width, sc_height)[0]
class map_chip_class():
    def __init__(self, location):
        self.chipimage = n
        self.chip_location = location
        self.chip_action = "none" # none, jump, drop, stop, turn
        self.arrow_direction = [0,1]
    #BG
    def create_chip_image(self):
        # type = "string"
        chipimage = pygame.image.load("{}\\{}.png".format(image_directry,self.chipimage))
        chipimage = pygame.transform.scale(chipimage,(100,100))
        return chipimage

    def get_chip_attr(self):

        return

def tiling_chip(index, image):
        # index = int
        gene = stageMap.stage_gene(index, sc_width, sc_height)
        map  = gene[0]
        margin = gene[1]
        gridsizex = len(map[index])
        gridsizey = len(map)

        t = "O"
        for i in range(gridsizex):
            for d in range(gridsizey):
                t = map[d][i]
                tile = image  
                tileX = tile.get_width()
                tileY = tile.get_height()
                screen.blit(tile,(margin[0]+tileX*i, margin[1] + tileY*d))

class player_class():

    def __init__(self) :
        self.location = [0,0] # grid zahyou
        self.playerImg = pygame.image.load('image0.png')
        self.playerImg =  pygame.transform.scale(self.playerImg,(120,300))
        self.player_start_point = [6,4] # grid
        self.pixel_imalocation = [0, 0]
        #self.grid_imalocation = [0,0]
        self.player_direction = [1,0] # Up[0,-1], Down[0,1], Left[-1,0], Right[1,0]
        self.player_status = ""
        self.player_HP = 20

    def player_move(self, x, y):
        # ほぼ描画しかしてない
        location = self.hamidasanai((x, y))
        margin = stageMap.stage_gene(stage_num, sc_width, sc_height)[1]
        screen.blit(self.playerImg,(location[0] + margin[0], location[1] + margin[1]))
        return location

    def find_player_location(self, location) :
        stage = stageMap.stage_gene(stage_num, sc_width, sc_height)[0]
        chipImage = pygame.image.load('N.png')
        chipImage = pygame.transform.scale(chipImage,(100,100))
        speed  = 3
        chipW = chipImage.get_width()
        chipH = chipImage.get_height()
        map_gridX = len(stage[0])
        map_gridY = len(stage)
        standingPointX = 0
        standingPointY = 0
        location[0] = max(location[0], 1)
        location[0] = min(location[0], map_gridX)
        location[1] = max(location[1], 1)
        location[1] = min(location[1], map_gridY)

        standingPointX = location[0]*chipW-(chipW/2)
        standingPointY = location[1]*chipH-(chipH/3)
        standingPointX -= (self.playerImg.get_width()/2)
        standingPointY -= self.playerImg.get_height()
        mokuhyou = [standingPointX,standingPointY]
        ret_mokuhyou = mokuhyou
        imalocation = self.pixel_imalocation
        imalocationX = self.pixel_imalocation[0]
        imalocationY = self.pixel_imalocation[1]

        mokuhyou[0] = mokuhyou[0] - imalocation[0]
        imalocationX += numpy.sign(mokuhyou[0]) * min(abs(mokuhyou[0]), speed)
        mokuhyou[1] = mokuhyou[1] - imalocation[1]
        imalocationY += numpy.sign(mokuhyou[1]) * min(abs(mokuhyou[1]), speed)

        return (imalocationX, imalocationY), ret_mokuhyou

    def find_player_destination(self):
        # 現在位置、プレイヤーの向き、マップチップから目標マス座標を決める
        grid_location = []
        stage  =stageMap.stage_gene(stage_num, sc_width, sc_height)[0]
        direction = self.player_direction
        location = self.location
        length = max(len(stage), len(stage[0]))
        chip = n
        for i in range(length):
            try:
                location[0] += direction[0] 
                location[1] += direction[1] 
                chip = stage[location[0]][location[1]]
            except Exception as e:
                continue
            if chip == n or chip == s or chip == b or chip == f:
                self.location = location
                

        return grid_location

    def hamidasanai(self, location):
        playerX = location[0]
        playerY = location[1]
        if playerX <= 0:
            playerX = 0
        elif playerX>= sc_width- self.playerImg.get_width():
            playerX = sc_width - self.playerImg.get_width()

        if playerY <= -self.playerImg.get_height():
            playerY = -self.playerImg.get_height()
        elif playerY>= sc_height- self.playerImg.get_height():
            playerY = sc_height - self.playerImg.get_height()
        
        return (playerX, playerY)
    
    def reset_player_in_startPoint(self):
        startpixelpoint = self.find_player_location(self.location)[1]
        self.pixel_imalocation = startpixelpoint

    def find_start_mapchip(self):
        startmap = stageMap.stage_gene(stage_num,sc_height,sc_width)[0]
        gridsizex = len(startmap[0])
        gridsizey = len(startmap)    
        for i in range(gridsizex):
            for d in range(gridsizey):
                if startmap[d][i] == s:
                    self.player_start_point = [1+i,1+d] #今はあれだけど逆だからあとで直してね



def  testdback( text, gyou=1):
    mozi = pygame.font.Font(None,50)
    mozimozi = mozi.render(text, True,(0,0,0))
    screen.blit(mozimozi,[50,60*gyou])

def puzzle_select():
    # 後でちゃんと書いてね
    stage_bangou = 1
    return stage_bangou

object_player = player_class()
object_player.find_start_mapchip()
object_player.location = object_player.player_start_point
object_player.reset_player_in_startPoint()
gene = stageMap.stage_gene(stage_num, sc_width, sc_height)
map  = gene[0]
object_mapchip = map
margin = gene[1]
gridsizex = len(map[0])
gridsizey = len(map)
t = "N"
for i in range(gridsizex):
    for d in range(gridsizey):
        chipType = map[d][i]
        object_mapchip[d][i] = map_chip_class((d,i))
        object_mapchip[d][i].chipimage = chipType
        chip = object_mapchip[d][i].create_chip_image()

#Game Loop
running = True

while running:
     #RGB- Red, Green, Blue
    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                puzzle_state = 1 # 適当に書いている
            if event.key == pygame.K_LEFT:
                object_player.player_direction = [-1,0] 
            elif event.key == pygame.K_RIGHT:
                object_player.player_direction = [1,0] 
            elif event.key == pygame.K_UP:          
                object_player.player_direction = [0,-1] 
            elif event.key == pygame.K_DOWN:      
                object_player.player_direction = [0,1] 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                continue
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                continue
                
    
    for i in range(gridsizex):
        for d in range(gridsizey):
            chip = object_mapchip[d][i].create_chip_image()
            tile = chip 
            tileX = tile.get_width()
            tileY = tile.get_height()
            screen.blit(tile,(margin[0]+tileX*i, margin[1]+tileY*d))

    object_player.find_player_destination()

    loc =  object_player.find_player_location(object_player.location)[0]
    
    object_player.pixel_imalocation  = object_player.player_move(loc[0], loc[1])
    object_player.grid_imalocation = [0,0]
    testdback(str(object_player.location), 1)
    testdback(str(object_player.pixel_imalocation), 2)
    pygame.display.update()

surface = pygame.image.load('N.png').convert()

