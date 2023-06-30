#import pygame
import copy
#import PIL
import base64
#from PIL import Image
import time
import ptext
import tiledef
from tiledef import tiles
from tiledef import sttobj,pygame
from tiledef import dialogtree as dlgtree
from dialogtree import cplayer ,irender 
import math
import random
import copy
import terrainmask2
import numpy as np
import numpy
import pickle
terrainlist  = []
def vec_add(y,t):
    r = []
    if len(y) == len(t):
        for i in range(0,len(y)-1):
            r.append(y[i]+t[i])
        return r
    else:
        return y
    
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
        if abs(l1[t] - l2[t]) > 1:
            y = False
    t = t + 1
    return y 
class memorymap():
    def __init__(self,imgmp,gstate=True,topt=0):
        if gstate:
            self.size = imgmp.get_size()
            self.imgmp = imgmp
            self.mmap = {}
            self.dgmap = {}
            lookup = {}
            for i in tiles:
                lookup[str(list[i.color])] = i
            for y in range(self.size[1] - 1):
                for x in range(self.size[0] - 1):
                    xil = list(imgmp.get_at((x, y)))
                    #xil[3] = 255
                    t = 'list' + str(xil)
                    output = "none"
                    if t in lookup:
                        output = lookup[t]
                    #else:
                        #print("__")
                        #print(t)
                        #print(lookup)
                    if output == "none" and topt == 0:
                        output = tiles[0]
                    if output != "none":
                        output.pos = [x, y]
                        try:
                            output.initmp()
                        except:
                            io = 0
                    self.mmap[str(x) + "o" + str(y)] = output
            self.dgmap = self.mmap
    def getdiff(self):
       difftab = [] 
       for y in range(0,self.size[1] - 1):
                for x in range(0,self.size[0] - 1):
                    original = self.dgmap[str(x) + "o" + str(y)]
                    checkitem =self.mmap[str(x) + "o" + str(y)]
                    if not original == checkitem:
                        difftab.append([str(x) + "o" + str(y),checkitem])
       return difftab
    def applydiff(self,difftab):
       for i in difftab:
           #print(i)
           self.mmap[i[0]] = i[1]
                     
                    
    
#     def rmmap(self,l):
#         l = list(l)
#         l[0] = math.floor(l[0])
#         l[1] = math.floor(l[1])
#         key = str(l[0]) + "o" + str(l[1])
#         if key in self.mmap:
#             return self.mmap[key]
#         else:
#             return tiles[0]
    def rmmap(self, l,clear=0):
        l = list(map(math.floor, l))
        key = f"{l[0]}o{l[1]}"
        if clear == 0:
            if key in self.mmap:
                return self.mmap[key]
            else:
                result = tiles[0]
                #self.mmap[key] = copy.deepcopy(result)
                return result
        else:
            if key in self.mmap:
                return self.mmap[key]
            else:
                #result = tiles[0]
                #self.mmap[key] = copy.deepcopy(result)
                return "none"  

    def smmap(self,l,i,dg=0):
        l = list(l)
        l[0] = math.floor(l[0])
        l[1] = math.floor(l[1])
        key = str(l[0]) + "o" + str(l[1])
        if not i == "none":
            i.pos = [l[0],l[1]]
        self.mmap[key] = copy.deepcopy(i)
        if dg:
            self.dgmap[key] = copy.deepcopy(i)
    def getpixel(self,t,st="l",clear=0):
       # try:
            if st=="l":
                return self.imgmp.getpixel(t)
            else:
                return self.rmmap(t,clear)
    def call(self,t,function):
            temp = self.rmmap(t)
            u = eval("temp." + str(function))
            self.smmap(t,temp)
            return u



class gmap():
    def add_pt(color=[255,255,255],size=2,lifetime=30,position=[0,0],velocity=[0,0]):
        particle = {}
        particle["lifetime"] =lifetime
        particle["position"] = position
        particle["velocity"] = velocity
        particle["color"] = color
        particle["size"] = size
        self.particles.append(particle)
        
    def run_pt():
        for i in range(0,len(self.particles)-1):
            particle = self.particles[i]
            try:
                if particle["lifetime"] <1 :
                    del(self.particles[i])
                else:
                    particle["lifetime"] += -1
                    particle["position"] = vec_add(particle["velocity"] , particle["position"])
                    self.particles[i] = particle
            except:
                del(self.particles[i])
    def loadtxt(self,name):
        try:
            return pygame.image.load(name)
        except:
            return pygame.image.load(name)
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
        elif idx == -1:
            return tile
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
                self.structuremap = self.sett(self.structuremap,x,y,ctile)
    def read(self,imgmp,x,y,clear=False,exc="none"):
        if exc == "none":
            size = imgmp.size
            t = imgmp.getpixel((x, y),"m",clear)
        else:
            t = imgmp.call((x, y),exc)
        return t
    def getheight(self,x,y):
        t = self.heightmap.rmmap((x, y))
        x = self.structuremap.rmmap((x, y))
        try:
            if x == "none":
                return  t.height
            else:
                return x.height + t.height
        except:
            return 0
    def readraw(self,imgmp,x,y):
        size = imgmp.size
        output = "none"
        if x > 0 and x < 480:
            if y > 0 and y < 240:
                t = imgmp.getpixel((x, y))
                output = t
        return output
    def __init__(self,tiles):
        global terrainlist
        self.tiles = tiles
        x = 1
        self.heightmap =  memorymap(self.loadtxt('img/heightmap.png'))
        self.structuremap =  memorymap(self.loadtxt('img/structures.png'),topt=1)
        self.threedeffecthax =  self.loadtxt('img/3doutlinehack.png')
        self.threedoverlay = pygame.transform.scale(pygame.image.load('img/3deffect.png'),(40,40))
        self.threedoverlay2 = pygame.transform.scale(pygame.image.load('img/3deffect2.png'),(40,40))
        self.threedfx = self.loadtxt('img/3dheight.png')
        self.particles = []
        if x:
            tile_lookup = {xi.name + xi.__class__.__name__: xi for xi in self.tiles}

            for i in terrainmask2.mask1:
                t = tile_lookup.get(i[1])

                if t is not None:
                    t.initmp()
                    layer = i[2] if len(i) > 2 else 1

                    if layer == 1:
                        self.structuremap.smmap(i[0], t, dg=1)
                    else:
                        self.heightmap.smmap(i[0], t, dg=1)

            self.structuremap.dgmap = self.structuremap.mmap
            self.heightmap.dgmap = self.heightmap.mmap











# print(terrainlist)
        #base64.b64encode(pickle.dumps(sd)).decode('ascii')

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
#cmap = gmap(tiles)