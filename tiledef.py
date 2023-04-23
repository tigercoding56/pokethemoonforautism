import pygame
import dialogtree
import asyncio
import npcdia
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
    def __init__(self,location,a=1,rescale=1):
        global tile_textures
        if not str(location) in tile_textures:
            a = 1
            preimg = pygame.image.load(str(location)).convert_alpha()
            if rescale:
                tile_textures[str(location)] = pygame.transform.scale(preimg, (40,40))
            else:
                tile_textures[str(location)] = preimg
            del(preimg)
        self.location = str(location)
    def gt(self):
        return tile_textures[self.location]
        
    
tiles = []
quests = {"intro":0}
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
    def lgco(self,attributes,name,color,a=0): # legacy compatibility
        self.name = name
        self.message = self.name
        self.color = color
        if len(attributes) > 3:
            if  "unpassable" in attributes[3]:
                self.walkable = 0
        self.attributes = []
        self.interactable = 0 
        self.texture = ptexture('img/' +self.name+'.png',a)
    def catchtxt(self,name):
        return ptexture('img/' +name+'.png')
    def __init__(self):
        self.color = [0,0,0,0]
        self.walkable = 1
        self.place_last =0
        self.name = '404'
        self.message = ""
        self.hidden = 0
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


#start of a-10 tiles
class a_10nose(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-nose',(69,69,69,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-nose.png')
class a_10cabin(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin',(88,88,88,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-cabin.png')
class a_10cabin2(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(98,98,98,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-cabin2.png')
class a_10tail(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(167,167,167,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-tailb.png')
class a_10section(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(147,147,147,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-section1.png')
        self.texture2 = ptexture('img/a10-section2.png')
    def gt(self):
        if self.pos[0] % 2 == 1:
            return self.texture
        else:
            return self.texture2
class a_10wing(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,10,50,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-winga.png')
        self.texture2 = ptexture('img/a10-wingb.png')
    def gt(self):
        if self.pos[1] % 2 == 1:
            return self.texture
        else:
            return self.texture2
class a_10wingtipa(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,50,10,255))
        self.message = ""
        self.place_last = 1
        self.texture = ptexture('img/a10-wingtipa.png')

class a_10wingtipb(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,100,50,255))
        self.message = ""
        self.place_last = 1
        self.texture = ptexture('img/a10-wingtipb.png')

class a_10turbinea(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,20,50,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-rightturbine.png')

class a_10turbineb(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,50,20,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-leftturbine.png')

class a_10taila(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,200,50,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a-10taila.png')
        
class a_10tailb(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,20,200,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.texture = ptexture('img/a10-tailc.png')





####end of a-10 tiles

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
class npc(tile):
    def lgco(self,name,questn,pos,dialog,a=0,attributes=["ground",1,20,["unpassable"]],squestn=None): # legacy compatibility
        self.name = name
        self.hidden = 0
        self.message = "(interact to speak)"
        self.color = color
        if len(attributes) > 3:
            if  "unpassable" in attributes[3]:
                self.walkable = 0
        self.attributes = attributes
        self.interactable = 1
        self.pos = pos
        self.dialog = dialog
        self.questn = questn
        self.texture = ptexture('img/' +self.name+'.png',a)
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests 
        if not self.questn in quests:
            quests[questn] = 0
        if quests[questn] == 0:
            dialogtree.cnpcdial = dialogtree.nbcdialog(self.dialog)
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not self.questn in quests:
                quests[questn] = 0
                self.hidden = False
                self.walkable = 1
            if quests[self.questn] == 0:
                if not dialogtree.cnpcdial == None:
                    if  dialogtree.cnpcdial.val == "ac":
                        quests[self.questn] = 1
                        self.hidden = True
                        self.walkable = 1
                        return [cmap,cplayer,"",tiles[1]]
            return [cmap,cplayer]
  
        
######
class scriptkiddie1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'scriptkiddie1',(206,177,22,255),1)
        self.message = "(interact to speak)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if quests["intro"] == 0:
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.introdialog)
        elif quests["intro"] == 1:
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.info1dialog)
        elif quests["intro"] ==2:
           t =  cplayer.inventory.invcheck("copper",2)
           if t == 1:
               dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.info2dialoga)
               quests["intro"] = 3
           else:
                dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.info2dialogb)
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            print(quests)
            if quests["intro"] == 0:
                if not dialogtree.cnpcdial == None:
                    if  dialogtree.cnpcdial.val == "mv":
                        quests["intro"] = 1
                        dialogtree.cnpcdial = dialogtree.ddialog()
                        cmap.structuremap.smmap(self.pos,cmap.tiles[1])
                        return [cmap,cplayer,"",tiles[1]]
            elif quests["intro"] == 1:
                if not dialogtree.cnpcdial == None:
                    if  dialogtree.cnpcdial.val == "ac":
                        quests["intro"] = 2
                        dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]


class terminal1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'terminal',(245,34,34,255),1)
        self.message = "(interact to open terminal)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.tdia)
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "ac":
                    cplayer.inventory = cplayer.inventory.invadds("infochip",1)
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]

class radio1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'radio',(111,226,147,255),1)
        self.message = "(interact to use the radio)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if ( not "getradio1" in quests) or ("radiodone" in quests  and (not "rbf2" in quests)): 
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.urdia)
        elif not "rbf2" in quests:
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.rdia)
            quests["reportbackrd"] = 1
            quests["radiodone"] = 1
        elif quests["rbf2"] == 1:
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia2)
            quests["rbf2"] = 2
            quests["GTH"] = 1
        else:
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.urdia)
            
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "ac":
                    quests["reportbackrd"] = 1
                    quests["radiodone"] = 1
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]

class milvet(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'milvet',(216,53,207,255),1)
        self.message = "(interact to speak)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if quests["intro"] > 2:
            if not "seldone" in quests:
                #if ( not "getradio1" in quests)  : 
                    dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia1)
                    
            else:
                if "getradio1" in quests:
                    if not "reportbackrd" in quests:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia_un_a)
                    elif not "rbf2" in quests:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia_f)
                    elif quests["rbf2"] ==1:    
                        dialogtree.cnpcdial = dialogtree.nbcdialog({"1":["just tell the hacker that all the robots \n agree to join him \n over the radio",{"ok":0,"i'll think about it ":0}]})
                    else:
                        dialogtree.cnpcdial = npcdia.gnpcdia()
                    
        else:
                dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.confuseddia)
                
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "hob":
                    quests["getinfo"] = 1
                elif dialogtree.cnpcdial.val == "MPU":
                    quests["getradio1"] =1
                elif dialogtree.cnpcdial.val == "reportback":
                    quests["rbf2"] = 1
        dialogtree.cnpcdial = dialogtree.ddialog()
        return [cmap,cplayer]
                    #cmap.setmap(self.pos[0] ,self.pos[1],tiles[1])
            
    
    
    
    
    
    
    
    
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
        self.interactable = 0
class steppingstones(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"steppingstones",(10, 10, 10, 255),1)
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
        self.lgco(['ground', 0, 0],"grass1",(0, 255, 0, 255))
xtiles = [water(),safetile(),tree(),woodh(),carpet(),wood(),cobblestone(),path(),steppingstones(),sand(),iceblock(),ice(),grass4(),grass3(),grass2(),grass1(),gemstone(),goldstone(),silverstone(),coalore(),copperore(),scriptkiddie1(),a_10cabin(),a_10cabin2(),a_10nose(),a_10section(),a_10tail(),a_10wing(),a_10wingtipa(),a_10wingtipb(),a_10taila(),a_10tailb(),a_10turbinea(),a_10turbineb(),terminal1(),radio1(),milvet()]
tiles = []
for itile in xtiles:
    itile.upd()
    tiles.append(itile)