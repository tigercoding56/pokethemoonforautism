import pygame
import PIL
from PIL import Image
import time
import ptext
class tile():
    def __init__(self,name,color,attributes,anim=0):
        self.color = color
        self.walkable = 1
        if len(attributes) > 3:
            if  "unpassable" in attributes[3]:
                self.walkable = 0
        self.name = name
        self.texture = pygame.image.load('img/'+str(name)+'.png')
        self.textures = []
        if not anim == 0:
            for i in range(1,anim):
                self.textures.append(pygame.image.load('img/'+str(name) + str(i)+'.png'))
        
        self.attributes = attributes ## sample ["detail"[group, if not set is assumed to be ground ],1 [enemy level to spawn 1 is basic enemies , 10 is challenging enemies],10 [chance of spawning (1 in #)],['unpassable','id32'] [list of attributes that can be used elsewhere in code , unpassable means player cannot walk through,"trader" [npc to spawn]]
tiles = []
def addtile(tile):
    global tiles
    tiles.append(tile)
    
class gmap():
    def loadtxt(self,name):
        try:
            return Image.open(name).convert("RBG")
        except:
            return Image.open(name)
    def gettile(self,x,y,idx=0):
        x = x + 8
        y = y + 8
        ctile = 0
        tile = self.read(self.heightmap,x ,y)
        tile2= self.read(self.structuremap,x,y,True)
        if idx == 0:
           if  tile2 == "none":
                return tile.name
           else:
                return tile2.name
        elif idx == 1:
            if  tile2 == "none":
                return tile
            else:
                return tile2
        else:
            if  tile2 == "none":
                return tile.walkable
            else:
                return tile2.walkable
    def read(self,imgmp,x,y,clear=False):
        size = imgmp.size
        output = "none"
        if x > 0 and x < 240:
            if y > 0 and y < 240:
                t = imgmp.getpixel((x, y))
                #print(t)
                for i in self.tiles:
                    if i.color == t :
                        output = i
                        
        if output == "none" and clear == False:
            output = self.tiles[0]
        return output
    def readraw(self,imgmp,x,y):
        size = imgmp.size
        output = "none"
        if x > 0 and x < 240:
            if y > 0 and y < 240:
                t = imgmp.getpixel((x, y))
                output = t
        return output
    def __init__(self,tiles):
        self.tiles = tiles
        self.heightmap =  self.loadtxt('img/heightmap.png')
        self.structuremap =  self.loadtxt('img/structures.png')
        self.threedeffecthax =  self.loadtxt('img/3doutlinehack.png')
        self.threedoverlay = pygame.image.load('img/3deffect.png')
addtile(  tile('water',(0,0,0,255,255),["ground",0,0,["unpassable"]],3))
addtile( tile('grass1',(255,255,255,255),["ground",1,20]))
addtile(  tile('grass2',(230,230,230,255),["ground",2,10]))
addtile( tile('grass3',(204,204,204,255),["ground",3,5]))
addtile(  tile('grass4',(179,179,179,255),["ground",4,3]))
addtile(  tile('ice',(153,153,153,255),["ground",4,3,["unpassable"]]))
addtile(  tile('iceblock',(33,233,222,255),["ground",4,3]))
addtile(  tile('sand',(128,128,128,255),["ground",2,15]))
#addtile(  tile('',(,,,255),["",0,0]))
addtile(  tile('steppingstones',(10,10,10,255),["ground",0,0]))
addtile(  tile('path',(0,255,255,255),["ground",0,0]))
addtile(  tile('cobblestone',(0,20,20,255),["ground",0,0,["unpassable"]]))
addtile(  tile('cobblestone',(20,20,20,255),["ground",0,0,["unpassable"]]))
addtile(  tile('wood',(255,0,161,255),["ground",0,0,["unpassable"]]))
addtile(  tile('woodh',(255,0,0,255),["ground",0,0,["unpassable"]]))
addtile(  tile('carpet',(0,0,255,255),["ground",0,0]))
addtile(  tile('tree',(0,96,121,255),["ground",0,0,["unpassable"]]))
addtile(  tile('safetile',(0,255,0,255),["ground",0,0]))
cmap = gmap(tiles)