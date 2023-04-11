import pygame
import PIL
from PIL import Image
import time
import ptext
from tiledef import tiles
from tiledef import sttobj
import math
import random
import copy

class playerobj():
    def __init__(self):
        self.inventory = {"capturedev":1}
    def rm(self,itemn):
        if itemn in self.inventory:
            if self.inventory[itemn] > 1:
                self.inventory[itemn] += -1
            else:
                del(self.inventory[itemn])
    def add(self,itemn):
        if itemn in self.inventory:
            self.inventory[itemn] += 1
        else:
            self.inventory[itemn] = 1
        
def nrl(l1,l2):
    t = 0
    y = True
    for i in l1:
        if abs(l1[t] - l2[t]) > 2:
            y = False
    t = t + 1
    return y 
class memorymap():
    def __init__(self,imgmp,gstate=True,topt=0):
        if gstate:
            self.size = imgmp.size
            self.imgmp = imgmp
            self.mmap = {}
            for y in range(0,self.size[1] - 1):
                for x in range(0,self.size[0] - 1):
                   t = imgmp.getpixel((x, y))
                   output = "none"
                   for i in tiles:
                       if list[i.color] == list[t] :
                           # print("match" + str(i))
                            output = i      
                   if output == "none" and topt==0 :
                       output = tiles[0]
                   self.mmap[str(x) + "o" + str(y)] = output
            
    
    def rmmap(self,l):
        l = list(l)
        l[0] = math.floor(l[0])
        l[1] = math.floor(l[1])
        key = str(l[0]) + "o" + str(l[1])
        if key in self.mmap:
            return self.mmap[key]
        else:
            return tiles[2]
    def smmap(self,l,i):
        l = list(l)
        l[0] = math.floor(l[0])
        l[1] = math.floor(l[1])
        key = str(l[0]) + "o" + str(l[1])
        self.mmap[key] = i
    def getpixel(self,t,st="l"):
       # try:
            if st=="l":
                return self.imgmp.getpixel(t)
            else:
                return self.rmmap(t)
    def call(self,t,function):
            temp = self.rmmap(t)
            u = eval("temp." + str(function))
            self.smmap(t,temp)
            return u

        #except:
            #if st=="l":
            #    return (0,0,0,255)
           # else:
                #return [(0,0,0,255),sttobj(0,0)]
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
    def sett(self,imgmp,x,y,tile):
        try:
            imgmp.smmap((x,y),tile)
            return imgmp
        except:
            return imgmp
    def setmap(self,x,y,i):
        x = x + 8
        y = y + 8
        ctile = i
        tile = self.read(self.heightmap,x ,y)
        tile2= self.read(self.structuremap,x,y,True)
        if  tile2 == "none":
                self.heightmap = self.sett(self.heightmap,x,y,ctile)
        else:
                self.structuremapmap = self.sett(self.structuremap,x,y,ctile)
    def read(self,imgmp,x,y,clear=False,exc="none"):
        if exc == "none":
            size = imgmp.size
            t = imgmp.getpixel((x, y),"m")
        else:
            t = imgmp.call((x, y),exc)
        return t
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
        self.heightmap =  memorymap(self.loadtxt('img/heightmap.png'))
        self.structuremap =  memorymap(self.loadtxt('img/structures.png'),topt=1)
        self.threedeffecthax =  self.loadtxt('img/3doutlinehack.png')
        self.threedoverlay = pygame.image.load('img/3deffect.png')
        self.threedfx = self.loadtxt('img/3dheight.png')

#addtile( tile('grass1',(255,255,255,255),["ground",1,20]))
#addtile(  tile('grass2',(230,230,230,255),["ground",2,10]))
#addtile( tile('grass3',(204,204,204,255),["ground",3,5]))
#addtile(  tile('grass4',(179,179,179,255),["ground",4,3]))
# addtile(  tile('ice',(153,153,153,255),["ground",4,3,["unpassable"]]))
# addtile(  tile('iceblock',(33,233,222,255),["ground",4,3]))
# addtile(  tile('sand',(128,128,128,255),["ground",2,15]))#ground , pokemoon level , attack chance (attributes[1] and attributes[2])
# #addtile(  tile('',(,,,255),["",0,0]))
# addtile(  tile('steppingstones',(10,10,10,255),["ground",0,0]))
# addtile(  tile('path',(0,255,255,255),["ground",0,0]))
# addtile(  tile('cobblestone',(0,20,20,255),["ground",0,0,["unpassable"]]))
# addtile(  tile('cobblestone',(20,20,20,255),["ground",0,0,["unpassable"]]))
# addtile(  tile('wood',(255,0,161,255),["ground",0,0,["unpassable"]]))
# addtile(  tile('woodh',(255,0,0,255),["ground",0,0,["unpassable"]]))
# addtile(  tile('carpet',(0,0,255,255),["ground",0,0]))
# addtile(  tile('tree',(0,96,121,255),["ground",0,0,["unpassable"]]))
# addtile(  tile('safetile',(0,255,0,255),["ground",0,0]))
cmap = gmap(tiles)