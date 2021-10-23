import os

import numpy
import pygame

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
player_speed = 2
stage_num = 4
selected_stage = stageMap.stage_gene(stage_num,sc_width, sc_height)[0]
chip_len = 100
chipimage = n
chip_location = [0,0]
chip_action = "none" # none, jump, drop, stop, turn
arrow_direction = [0,1]

def create_chip_image(type):
    # type = "string"
    image = pygame.image.load("{}\\{}.png".format(image_directry, type))
    image = pygame.transform.scale(image,(chip_len,chip_len))
    return image

def tiling_chip(stage_num):
    gene = stageMap.stage_gene(stage_num,sc_width, sc_height)
    map  = gene[0]
    margin = gene[1]
    gridsizex = len(map[0])
    gridsizey = len(map)

    t = "O"
    for x in range(gridsizex):
        for y in range(gridsizey):
            t = map[y][x]
            tile = create_chip_image(t) 
            tileX = tile.get_width()
            tileY = tile.get_height()
            screen.blit(tile,(margin[0]+tileX*x, margin[1] + tileY*y))

class player_class():

    def __init__(self) :
        scale = 12
        self.location = [0,0] # grid zahyou [Y,X]
        self.playerImg = pygame.image.load('chara_black.jpg')
        self.playerImg =  pygame.transform.scale(self.playerImg,(int(self.playerImg.get_width()/scale),
                                                int(self.playerImg.get_height()/scale)))
        self.player_start_point = [6,4] # grid [y,x] ０はじまり
        self.pixel_imalocation = [0, 0]  # [Y, X]
        self.player_direction = [0,1] # LEFT[0,-1], RIGHT[0,1], up[-1,0], down[1,0]
        self.player_status = ""
        self.player_HP = 20 # int
        self.pixel_destination = [0,0] # [Y,X]

    def player_move(self, pixel_XY):
        # ほぼ描画しかしてない
        location = pixel_XY 
        # location = self.hamidasanai((x, y))
        margin = stageMap.stage_gene(stage_num, sc_width, sc_height)[1]
        screen.blit(self.playerImg,(location[0] , location[1] ))  # X,Y
        return location

    def find_PixelDestination(self):
        grid = self.location # Y, X
        stage = selected_stage
        margin = stageMap.stage_gene(stage_num, sc_width, sc_width)[1]
        charaimage = self.playerImg
        image = create_chip_image(n)

        # キャラ画像右下の座標が出る
        X = (image.get_width()*(grid[1]+1)) - (image.get_width()/2)
        Y = (image.get_height()*(grid[0]+1)) - (image.get_height()/3)
        # キャラ画像左上の座標を出す
        X -= charaimage.get_width()/2
        Y -= charaimage.get_height()

        self.pixel_destination = [Y,X]

    def pixelmove_per_frame(self):
        # pixel_destination から勝手に移動位置を決める
        speed = player_speed
        des = self.pixel_destination # [y,X]
        mokuhyoX = des[1]
        mokuhyoY = des[0]
        pixImaX = self.pixel_imalocation[1]
        pixImaY = self.pixel_imalocation[0]
    
        mX = mokuhyoX-pixImaX
        pixImaX += numpy.sign(mX)*min(abs(mX),speed)
        
        mY = mokuhyoY-pixImaY
        pixImaY += numpy.sign(mY)*min(abs(mY),speed)

        return [pixImaX, pixImaY]

    def find_player_location(self, locationYX) :
        stage = selected_stage
        chipImage = pygame.image.load('N.png')
        chipImage = pygame.transform.scale(chipImage,(chip_len, chip_len))
        speed  = 2
        chipW = chipImage.get_width()
        chipH = chipImage.get_height()
        map_gridX = len(stage[0])
        map_gridY = len(stage)
        standingPointX = 0
        standingPointY = 0
        location = [locationYX[0],locationYX[1]]
        location[0] = min(max(location[0], 1), map_gridX)
        location[1] = min(max(location[1], 1), map_gridY)

        standingPointX = location[0]*chipW-(chipW/2)
        standingPointY = location[1]*chipH-(chipH/3)
        standingPointX -= (self.playerImg.get_width()/2)
        standingPointY -= self.playerImg.get_height()
        mokuhyou = [standingPointX,standingPointY]
        ret_mokuhyou = mokuhyou
        imalocation = self.pixel_imalocation
        imalocationY = self.pixel_imalocation[0]
        imalocationX = self.pixel_imalocation[1]
        mokuhyou[0] = mokuhyou[0] - imalocation[0]
        imalocationY += numpy.sign(mokuhyou[0]) * min(abs(mokuhyou[0]), speed)
        mokuhyou[1] = mokuhyou[1] - imalocation[1]
        imalocationX += numpy.sign(mokuhyou[1]) * min(abs(mokuhyou[1]), speed)

        # self.location = (imalocationY,imalocationX)
        return (imalocationX, imalocationY), ret_mokuhyou

    def find_player_destination(self):
        # 現在位置、プレイヤーの向き、マップチップから目標マス座標を決める
        grid_location = []
        stage  = selected_stage
        direction = self.player_direction
        location = self.location
        length = max(len(stage)*numpy.sign(direction[0]), len(stage[0])*numpy.sign(direction[1]))
        chip = n
        for i in range(length):
            # if location[0]+direction[1] >= len(stage):
            #     break
            # elif location[1]+direction[0] >= len(stage[0]):
            #     break
            try:
                chip = stage[location[0]][location[1]]
            except:
                continue
            zokusei = stageMap.chip_effect(chip)
            if zokusei[0] == "turn":
                self.player_direction = zokusei[1]
            elif zokusei[0] == "walk":
                a = 1
            elif zokusei[0]== "stop":
                # breakに入るとループ自体を中断してループを抜ける
                break
            location[0] += direction[0] 
            location[1] += direction[1]         
            
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
        
        return (playerY, playerX)
    
    def reset_player_in_startPoint(self):
        startpixelpoint = self.find_player_location(self.player_start_point)[1]
        self.pixel_imalocation = startpixelpoint

    def find_start_mapchip(self):
        startmap = selected_stage
        gridsizex = len(startmap[0])
        gridsizey = len(startmap)    
        for x in range(gridsizex):
            for y in range(gridsizey):
                if startmap[y][x] == s:
                    self.player_start_point = [y,x]
                    break


def  testdback( text, gyou=1):
    mozi = pygame.font.Font(None,40)
    mozimozi = mozi.render(text, True,(0,0,0))
    screen.blit(mozimozi,[20,50*gyou])

def puzzle_select():
    # 後でちゃんと書いてね
    stage_bangou = 1
    return stage_bangou

object_player = player_class()
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
                object_player.player_direction = [-1,0] 
                object_player.location[0] += -1 
            elif event.key == pygame.K_RIGHT:
                object_player.player_direction  = [1,0] 
                object_player.location[0]  += 1 
            elif event.key == pygame.K_UP:          
                object_player.player_direction  = [0,-1] 
            elif event.key == pygame.K_DOWN:      
                object_player.player_direction  = [0,1] 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                continue
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                continue

    object_player.find_player_location(object_player.location)            
    object_player.find_PixelDestination()
    object_player.pixelmove_per_frame()
    
    object_player.pixel_imalocation  = object_player.player_move(object_player.pixel_destination)

    testdback(str(object_player.location), 1)
    testdback(str(object_player.pixel_imalocation), 2)

    pygame.display.update()

surface = pygame.image.load('N.png').convert()

