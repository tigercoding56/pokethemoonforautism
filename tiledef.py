import pygame

class sttobj():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = {"x":x , "y": y}
    def sets(key,value):# index and value to place at index
        self.state[key] = value
    def gets(key,default): # index  , and value to return if index does not have a value
        if key in self.state:
            return self.state[key]
        else:
            return default
tiles = []
class tile():
    def interact(self):
        return 0
    
    def gtx(self,fn):
        return self.gt()
    def gt(self):
        return self.texture
    def lgco(self,attributes,name,color): # legacy compatibility
        self.name = name
        self.color = color
        if len(attributes) > 3:
            if  "unpassable" in attributes[3]:
                self.walkable = 0
        self.attributes = []
        self.texture = pygame.image.load('img/' +self.name+'.png')
    def catchtxt(self,name):
        return pygame.image.load('img/' +name+'.png')
    def __init__(self):
        self.color = [0,0,0,0]
        self.walkable = 1
        self.name = '404'
        #self.texture = pygame.image.load('img/'+str(name)+'.png')
        self.texture = pygame.image.load('img/404.png')
        self.textures = []
        self.attributes = ["ground",0,0,[]] ## sample ["detail"[group, if not set is assumed to be ground ],1 [enemy level to spawn 1 is basic enemies , 10 is challenging enemies],10 [chance of spawning (1 in #)],['unpassable','id32'] [list of attributes that can be used elsewhere in code , unpassable means player cannot walk through,"trader" [npc to spawn]]
#### definitions start here

class water(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",0,0,["unpassable"]],'water',(0,0,0,255))
        self.txt1 = self.catchtxt('water2')
        self.txt2 = self.catchtxt('water3')
        self.ft =0
    def gt(self):
        return self.gtx(1)
    def gtx(self,fn):
        fn = fn % 30
        if fn < 11:
            return self.texture
        elif fn < 21:
            return self.txt1
        else:
            return self.txt2
        

class grass1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'grass1',(255,255,255,255))
        
class grass2(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'grass2',(230,230,230,255))
        
class grass3(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",3,5],'grass3',(204,204,204,255))
        
class grass4(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",4,3],'grass4',(179,179,179,255))

class ice(tile):
    def upd(self):
        self.lgco(['ground', 4, 3, ['unpassable']],"ice",(153, 153, 153, 255))
class iceblock(tile):
    def upd(self):
        self.lgco(['ground', 4, 3],"iceblock",(33, 233, 222, 255))
class sand(tile):
    def upd(self):
        self.lgco(['ground', 2, 15],"sand",(128, 128, 128, 255))
class steppingstones(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"steppingstones",(10, 10, 10, 255))
class path(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"path",(0, 255, 255, 255))
class cobblestone(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"cobblestone",(0, 20, 20, 255))
class cobblestone(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"cobblestone",(20, 20, 20, 255))
class wood(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"wood",(255, 0, 161, 255))
class woodh(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"woodh",(255, 0, 0, 255))
class carpet(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"carpet",(0, 0, 255, 255))
class tree(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"tree",(0, 96, 121, 255))
class safetile(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"safetile",(0, 255, 0, 255))
xtiles = [water(),safetile(),tree(),woodh(),carpet(),wood(),cobblestone(),path(),steppingstones(),sand(),iceblock(),ice(),grass4(),grass3(),grass2(),grass1()]
tiles = []
for itile in xtiles:
    itile.upd()
    tiles.append(itile)