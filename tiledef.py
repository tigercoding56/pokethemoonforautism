import pygame
import dialogtree
import asyncio
def IO():
    pass # to get around asyncio.stop() make it so that interact() looks at if tile has a dialog property and handles it in main event loop  (in main.py  just switch off the main function of libraries.py altogether)
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
tile_textures = {}#optimisation to not need a rtx 4090 XYT
class ptexture(): # a texture pointer class
    def __init__(self,location):
        global tile_textures
        if not str(location) in tile_textures:
            tile_textures[str(location)] = pygame.image.load(str(location))
        self.location = str(location)
    def gt(self):
        return tile_textures[self.location]
        
    
tiles = []
class tile():
    def interact(self,cplayer,cmap,message="found \n nothing"):
        return [cplayer,cmap,message]#usefull for modifying the worldmap  , or teleporting the player the last argument is a message 
    
    def gtx(self,fn):
        return self.gt()
    def gt(self):
        return self.texture
    def callback(self,cmap=0,cplayer=0,test=0):
        if test == 1:
            return 0
        else:
            return [cmap,cplayer]
    def lgco(self,attributes,name,color): # legacy compatibility
        self.name = name
        self.message = self.name
        self.color = color
        if len(attributes) > 3:
            if  "unpassable" in attributes[3]:
                self.walkable = 0
        self.attributes = []
        self.interactable = 0 
        self.texture = ptexture('img/' +self.name+'.png')
    def catchtxt(self,name):
        return ptexture('img/' +name+'.png')
    def __init__(self):
        self.color = [0,0,0,0]
        self.walkable = 1
        self.name = '404'
        self.message = ""
        #self.texture = ptexture('img/'+str(name)+'.png')
        self.texture = ptexture('img/404.png')
        self.textures = []
        self.pos = [0,0]
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

class gemstone(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'gemstone',(77,77,157,255))
        self.message = "(interact to mine gem)"
        self.interactable = True
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("gem",1)
        return [cplayer,cmap,message]


class goldstone(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'goldore',(196,189,62,255))
        self.message = "(interact to mine gold)"
        self.interactable = True
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("gold",1)
        return [cplayer,cmap,message]
class silverstone(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'silverstone',(235,235,235,255))
        self.message = "(interact to mine silver)"
        self.interactable = True
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("silver",1)
        return [cplayer,cmap,message]
class coalore(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'coalore',(69,20,20,255))
        self.message = "(interact to mine coal)"
        self.interactable = True
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("coal",1)
        return [cplayer,cmap,message]

class copperore(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'copperore',(80,80,80,255))
        self.message = "(interact to mine copper)"
        self.interactable = True
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("copper",1)
        return [cplayer,cmap,message]
    
class grass2(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'grass2',(230,230,230,255))
###npc classes
class scriptkiddie1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'scriptkiddie1',(206,177,22,255))
        self.message = "(interact to speak)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.introdialog)
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                print(dialogtree.cnpcdial.val)
                if  dialogtree.cnpcdial.val == "mv":
                    cmap.structuremap.smmap(self.pos,cmap.tiles[1])
                    cmap.setmap(self.pos[0] ,self.pos[1],tiles[1])
            return [cmap,cplayer]
    
    
    
    
    
    
    
    
####npc classes
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
        self.interactable = 1
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
xtiles = [water(),safetile(),tree(),woodh(),carpet(),wood(),cobblestone(),path(),steppingstones(),sand(),iceblock(),ice(),grass4(),grass3(),grass2(),grass1(),gemstone(),goldstone(),silverstone(),coalore(),copperore(),scriptkiddie1()]
tiles = []
for itile in xtiles:
    itile.upd()
    tiles.append(itile)