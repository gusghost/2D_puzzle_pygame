import glob
import os

import numpy
import pygame
from genericpath import exists

import stageMap
from stage_variable import *

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
stage_num = 4
selected_stage = stageMap.stage_gene(stage_num,sc_width, sc_height)[0]

chipimage = n
chip_location = [0,0]
chip_action = "walk" # walk, dash, jump, drop, stop, turn
arrow_direction = [0,1]

def create_chip_image(type):
    # type = "string"
    image = pygame.image.load("{}\\{}.png".format(image_directry, type))
    image = pygame.transform.scale(image,(100,100))
    return image

object_chip = []
def tiling_chip(stage_num):
    index = stage_num
    gene = stageMap.stage_gene(index, sc_width, sc_height)
    map  = gene[0]
    margin = gene[1]
    gridsizex = len(map[0])
    gridsizey = len(map)
    t = "O"
    object_chip = map
    for x in range(gridsizex):
        for y in range(gridsizey):
            t = map[y][x]
            tile = create_chip_image(t) 
            tileX = tile.get_width()
            tileY = tile.get_height()
            object_chip[y][x] = sprite_chip_class(t)

            screen.blit(tile,(margin[1]+tileX*x, margin[0] + tileY*y))

class sprite_chip_class(pygame.sprite.Sprite):
    def __init__(self, chip_type) -> None:
        super(sprite_chip_class, self).__init__()
        self.image = pygame.image.load(os.path.join(image_directry, "{}.png".format(chip_type)))
        self.location = [1, 1]
        self.action = "walk"
        self.rect = self.image.get_rect()

    def draw(self):
        screen.blit(self.Image,self.rect)

    def update(self):
        a = 1

class sprite_player_class(pygame.sprite.Sprite):

    def __init__(self) :
        super(sprite_player_class, self).__init__()

        scale = 12
        self.location = [0,0] # grid zahyou 原点は０，０。[Y,X]
        names = glob.glob(image_directry+"//chara1 (*).png")
        names = glob.glob(image_directry+"//image0.png")
        self.playerImages = [None]*len(names)
        self.player_index = 0

        for i,name in enumerate(names) :
            self.playerImages[i] = pygame.image.load(os.path.normpath(name))
            print(name)
            self.playerImages[i] =  pygame.transform.scale(self.playerImages[i],(int(self.playerImages[i].get_width()/scale),
                                                int(self.playerImages[i].get_height()/scale)))
        self.playerImage = self.playerImages[self.player_index]
        self.rect = self.playerImage.get_rect()
        self.player_start_point = [0,0] # grid
        self.pixel_imalocation = [0, 0]
        self.player_direction = [1,0] # [Y, X]で表記するUp[-1,0], Down[1,0], Left[0,-1], Right[0,1]
        self.player_status = ""
        self.player_HP = 20


    def draw(self):
        screen.blit(self.playerImage,self.rect)

    def find_player_location(self, location) :
        player_dummy_image = self.playerImage
        stage = stageMap.stage_gene(stage_num, sc_width, sc_height)[0]
        chipImage = pygame.image.load('N.png')
        chipImage = pygame.transform.scale(chipImage,(100,100))
        speed  = 3
        # 変数を計算する
        chipW = chipImage.get_width()
        chipH = chipImage.get_height()
        map_gridX = len(stage[0])
        map_gridY = len(stage)
        standingPointX = 0
        standingPointY = 0
        # tmp_location = [0,0]
        # マス座標をステージのサイズに制限する
        tmp_location = grid_hamidasanai(location)
        # ここからピクセル座標を計算し始める
        # チップの画像サイズをもとにして計算
        # 画像の右下を基準にして-(chipH/3)-(chipW/2)
        # はマップチップの上に立ってるように見せかけるためにずらしてる
        standingPointY = (tmp_location[0]+1)*chipW-(chipW/2)
        standingPointX = (tmp_location[1]+1)*chipH-(chipH/3)
        # 描画位置のために右上になるように計算する
        standingPointX -= (player_dummy_image.get_width()/2)
        standingPointY -= player_dummy_image.get_height()
        mokuhyou = [standingPointY,standingPointX]
        ret_mokuhyou = mokuhyou
        imalocation = self.pixel_imalocation
        imalocationY = self.pixel_imalocation[0]
        imalocationX = self.pixel_imalocation[1]
        # 目標が超振動を起こしているみたい
        mokuhyou[0] = mokuhyou[0] - imalocation[0]
        imalocationY += numpy.sign(mokuhyou[0]) * min(abs(mokuhyou[0]), speed)
        mokuhyou[1] = mokuhyou[1] - imalocation[1]
        imalocationX += numpy.sign(mokuhyou[1]) * min(abs(mokuhyou[1]), speed)

        margin = stageMap.stage_gene(stage_num, sc_width, sc_height)[1]
        self.rect = (imalocationX, imalocationY)
        return (imalocationX, imalocationY), ret_mokuhyou

    def find_player_destination(self):
        # 現在位置、プレイヤーの向き、マップチップから目標マス座標を決める
        grid_location = []
        location = self.location
        stage  = selected_stage
        # print(location,stage)
        zokusei = stageMap.chip_effect(stage[location[0]][location[1]])
        testdback(str(zokusei), 4)
        # if zokusei[0] == "turn":
        #     self.player_direction = zokusei[1]

        direction = self.player_direction
        length = max(len(stage)*numpy.sign(direction[0]), len(stage[0])*numpy.sign(direction[1]))
        chip = n
        for i in range(length):
            
            if location[0]+direction[0] >= length:
                break
            chip = stage[location[0]][location[1]]
            zokusei = stageMap.chip_effect(chip)
            if zokusei[0] == "turn":
                self.player_direction = zokusei[1]
            elif zokusei[0] == "walk":
                a = 1
            elif zokusei[0]== "stop":
                break
            location[0] += direction[0] 
            location[1] += direction[1]         
            
        self.location = location
        return grid_location

    def hamidasanai(self, location):
        # [Y,X]
        player_dummy_image = self.playerImage
        playerY = location[0]
        playerX = location[1]
        if playerX <= 0:
            playerX = 0
        elif playerX>= sc_width- player_dummy_image.get_width():
            playerX = sc_width - player_dummy_image.get_width()

        if playerY <= -player_dummy_image.get_height():
            playerY = -player_dummy_image.get_height()
        elif playerY>= sc_height- player_dummy_image.get_height():
            playerY = sc_height - player_dummy_image.get_height()
        
        return (playerY, playerX)
    
    def reset_player_in_startPoint(self):
        startpixelpoint = self.find_player_location(self.player_start_point)[1]
        self.pixel_imalocation = startpixelpoint

    def find_start_mapchip(self):
        startmap = stageMap.stage_gene(stage_num,sc_height,sc_width)[0]
        gridsizex = len(startmap[0])
        gridsizey = len(startmap)    
        for x in range(gridsizex):
            for y in range(gridsizey):
                if startmap[y][x] == s:
                    self.player_start_point = [y,x]

    def update(self):

        if self.player_index >= len(self.playerImages):
            self.player_index = 0


        self.playerImage = self.playerImages[self.player_index]
        self.player_index += 1                   

def grid_hamidasanai(location):
    stage = stageMap.stage_gene(stage_num, sc_width, sc_height)[0]
    map_gridX = len(stage[0])
    map_gridY = len(stage)
    tmp_location = location
    # マス座標をステージのサイズに制限する
    tmp_location[0] = max(location[0], 1)
    tmp_location[0] = min(location[0], map_gridX)
    tmp_location[1] = max(location[1], 1)
    tmp_location[1] = min(location[1], map_gridY)
    return tmp_location

def  testdback( text, gyou=1):
    mozi = pygame.font.Font(None,40)
    mozimozi = mozi.render(text, True,(0,0,0))
    screen.blit(mozimozi,[20,50*gyou])

def puzzle_select():
    # 後でちゃんと書いてね
    stage_bangou = 1
    return stage_bangou

object_player = sprite_player_class()
object_player.find_start_mapchip()
object_player.location = object_player.player_start_point
object_player.reset_player_in_startPoint()

screen.fill((200, 200, 200))
tiling_chip(stage_num)
pygame.image.save(screen, os.path.join(image_directry,"generated_BG.png") )
stage_BG = pygame.image.load(os.path.join(image_directry,"generated_BG.png"))
#Game Loop
running = True

while running:
     #RGB- Red, Green, Blue
    # screen.fill((200, 200, 200))
    screen.blit(stage_BG,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                puzzle_state = 1 # 適当に書いている
            if event.key == pygame.K_LEFT:
                object_player.player_direction = [0,-1] 
            elif event.key == pygame.K_RIGHT:
                object_player.player_direction = [0,1] 
            elif event.key == pygame.K_UP:          
                object_player.player_direction = [-1,0] 
            elif event.key == pygame.K_DOWN:      
                object_player.player_direction = [1,0] 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                continue
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                continue
    fps = pygame.time.Clock().get_fps()
    time1 = pygame.time.Clock().tick(fps)

    object_player.find_player_destination()
    loc =  object_player.find_player_location(object_player.location)[0]
    
    object_player.pixel_imalocation  = object_player.hamidasanai(loc)
    object_player.grid_imalocation = [0,0]
    object_player.update()
    object_player.draw()
    testdback(str(object_player.location), 1)
    testdback(str(object_player.pixel_imalocation), 2)
         
    pygame.display.update()

surface = pygame.image.load('N.png').convert()

