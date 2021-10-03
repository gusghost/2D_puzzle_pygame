from numpy.core.records import array
import pygame
import numpy
import stageMap

pygame.init()

#create screen
screen = pygame.display.set_mode((1176,664))

#caption and Icon

pygame.display.set_caption("ZIKKEN")
icon = pygame.image.load("karicon.png")
pygame.display.set_icon(icon)
sc_width = pygame.display.get_window_size()[0]
sc_height = pygame.display.get_window_size()[1]

#Player
stage_num = 4
selected_stage = stageMap.stage_gene(stage_num,sc_width, sc_height)[0]
class map_chip_class():
    def __init__(self, location):
        self.chipimage = ""
        self.chip_location = location
        self.chip_action = "none" # none, jump, drop, stop, turn
        self.arrow_direction = [0,1]
    #BG
    def create_chip_image(self):
        # type = "string"
        chiptype = self.chipimage
        chiptype = chiptype.upper()
        chipimage = pygame.image.load("{}.png".format(chiptype))
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
        self.player_start_point = [2,1] # grid
        self.pixel_imalocacion = [0, 0]
        self.player_direction = [1,0] # Up[0,-1], Down[0,1], Left[-1,0], Right[1,0]
        self.player_status = ""
        self.player_HP = 20

    def player_move(self, x, y):
        # ほぼ描画しかしてない
        location = self.hamidasanai((x, y))
        margin = stage_gene(stage_num)[1]
        screen.blit(self.playerImg,(location[0] + margin[0], location[1] + margin[1]))
        return location

    def find_player_location(self, location) :
        stage = stage_gene(stage_num)[0]
        chipImage = create_chip_image("N")
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

        imalocation = self.pixel_imalocacion
        imalocationX = self.pixel_imalocacion[0]
        imalocationY = self.pixel_imalocacion[1]

        mokuhyou[0] = mokuhyou[0] - imalocation[0]
        imalocationX += numpy.sign(mokuhyou[0]) * min(abs(mokuhyou[0]), speed)
        mokuhyou[1] = mokuhyou[1] - imalocation[1]
        imalocationY += numpy.sign(mokuhyou[1]) * min(abs(mokuhyou[1]), speed)

        return (imalocationX, imalocationY)

    def find_player_destination(self):
        # 現在位置、プレイヤーの向き、マップチップから目標マス座標を決める
        grid_location = []
        stage  =stage_gene(stage_num)[0]
        direction = self.player_direction
        location = self.location
        length = max(len(stage), len(stage[0]))
        for i in range(length):
            location = location + direction 
            chip = stage[location[0]][location[1]]
            

        grid_location = []
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

def puzzle_select():
    # 後でちゃんと書いてね
    stage_bangou = 1
    return stage_bangou

object_player = player_class()
object_player.location = object_player.player_start_point

gene = stageMap.stage_gene(stage_num, sc_width, sc_height)
object_mapchip = gene
map  = gene[0]
margin = gene[1]
gridsizex = len(map[stage_num])
gridsizey = len(map)
t = "O"
for i in range(gridsizex):
    for d in range(gridsizey):
        object_mapchip[d][i] = map_chip_class((d,i))
        loc = object_mapchip[d][i].chip_location
        object_mapchip[d][i].chipimage = (1,1)
        # map[loc[0]][loc[1]]
        chip = object_mapchip[d][i].create_chip_image()
        tile = chip 
        tileX = tile.get_width()
        tileY = tile.get_height()
        screen.blit(tile,(tileX*i, tileY*d))


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
            # if event.key == pygame.K_LEFT:
            #     object_player.location[0] += -1
            # if event.key == pygame.K_RIGHT:
            #     object_player.location[0] += 1
            # if event.key == pygame.K_UP:          
            #     object_player.location[1] += -1
            # if event.key == pygame.K_DOWN:      
            #     object_player.location[1] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                continue
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                continue
                
    
    

    loc =  object_player.find_player_location(object_player.location)
    
    object_player.pixel_imalocacion  = object_player.player_move(loc[0], loc[1])
    pygame.display.update()

surface = pygame.image.load('N.png').convert()

