import pygame
import PIL
import UIdialogdef
#import noise
import standartUIdialogref
import waterFX
import gc
from copy import deepcopy 
import renderbase
from renderbase import svimg
from PIL import Image
import time
import ptext
import pickle
import base64
from commands import ccmd 
from commands import gprt 
#import maingui as agui
#from maingui import App
import enemies as EM
import xmap
from xmap import dlgtree
from xmap import gmap
from xmap import *
from pygamebutton import PygButton
from pygame.locals import DOUBLEBUF
onweb = 0
pos1 = [0,0]
pos2 = [0,0]
markp=0
sound_intr = -1
selectedt = 0


            
muted = 1
pygame.mixer.init()
outsoundtrack = pygame.mixer.Sound('audio/peasant kingdom.ogg')
insoundtrack = pygame.mixer.Sound('audio/JRPG_town_loop.ogg')
#outsoundtrack.play(-1)
#insoundtrack.play(-1)
def intsound(x):
    global sound_intr,outsoundtrack,insoundtrack,muted
    if muted == 0:
        if x == 1:
            if not sound_intr == 1:
                outsoundtrack.fadeout(2000)
                insoundtrack.play(-1,fade_ms=2000)
        if x == 0:
            if not sound_intr == 0:
                insoundtrack.fadeout(2000)
                outsoundtrack.play(-1,fade_ms=2000)
        sound_intr = x
        outsoundtrack.set_volume(1-sound_intr)
        insoundtrack.set_volume(sound_intr)
ptextures = {}#optimisation to not need a rtx 4090 XYT
class xtexture(): # a texture pointer class
    def __init__(self,location,a=1,rescale=1):
        global tile_textures
        if not str(location) in ptextures:
            a = 1
            preimg = pygame.image.load(str(location)).convert_alpha()
            ptextures[str(location)] = preimg
            del(preimg)
        self.location = str(location)
    def gt(self):
        global ptextures
        return ptextures[self.location]
if __import__("sys").platform == "emscripten":
    from platform import window
    onweb = 1
    window.fs_loaded = False
else:
    import os
    



ActionQueue =[]
mousepos = [1,0]
transition = [1,"WMP","WMP"]
#transition = [0,"WMP","ARENA"]
AREAS = ["WMP","ARENA","INV"]## these will be implemented later
ACTIVEAREA = "WMP"# WMP = world map , so the default playing area is handled while WMP is active 
X = 840
Y = 640
cmap = gmap(tiles)
def save(slot):
    global cmap,onweb,xmap,cplayer
    if onweb :
        sd = ["0.2",cplayer,cmap.structuremap.getdiff(),cmap.heightmap.getdiff(),xmap.tiledef.quests]
        window.localStorage.setItem(str(slot),str(base64.b64encode(pickle.dumps(sd)).decode('ascii')))
    else:
        sd = ["0.2",cplayer,cmap.structuremap.getdiff(),cmap.heightmap.getdiff(),xmap.tiledef.quests]
        #os.path.exists() ## if this gives error , make sure you only use ptexture classes in tiledef py as opposed to pygame.textures
        #print(str(base64.b64encode(pickle.dumps(sd)).decode('ascii')))
        with open("savegame"+slot+".dat","wb") as svg:
            pickle.dump(sd, svg)

def load(slot):
    global cmap , onweb,xmap,cplayer
    if onweb :
        if not window.localStorage.getItem(str(slot)) == None:
            temp = window.localStorage.getItem(str(slot))
            sd = pickle.loads(base64.b64decode(temp))
            if sd[0] == "0.2":##current save version
                    cplayer = sd[1]
                    cmap.structuremap.applydiff(sd[2])
                    cmap.heightmap.applydiff(sd[3])
                    xmap.tiledef.quests = sd[4]
    else:
        if os.path.exists("savegame"+slot+".dat"):
            with open("savegame"+slot+".dat","rb") as svg:
                sd = pickle.load(svg)
                if sd[0] == "0.2":##current save version
                    cplayer = sd[1]
                    cmap.structuremap.applydiff(sd[2])
                    cmap.heightmap.applydiff(sd[3])
                    xmap.tiledef.quests = sd[4]
                    xmap.tiledef.quests = {'intro': 3, 'HOFF': 0, 'getradio1': 1, 'seldone': 1, 'reportbackrd': 1, 'radiodone': 1, 'ART': 1, 'rbf2': 2, 'GTH': 1}

######################
#player initial setup#
######################


######################




######################
#GUI setup           #
######################
def scale(x,y,x1,y1):
    return (x*2,y*2,x1*2,y1*2)
invbtn = PygButton(caption="inventory",rect=scale(320,280,100,20))
svbtn = PygButton(caption="save game",rect=scale(320,260,100,20))
lvbtn = PygButton(caption="load game",rect=scale(320,240,100,20))
intbtn = PygButton(caption="interact ",rect=scale(320,300,100,20))
dbbtn = PygButton(caption="costumise tile",rect=scale(320,220,100,20))
#intbtn = PygButton(caption="scavenge",rect=(320,260,100,20))


######################
defaultpk = EM.pokemons[0].pclone()
pygame.key.set_repeat(250)

def getattacks():
     global defaultpk
     return defaultpk
     




class text():
    def __init__():
        pass
class characterinstance():
    def __init__(self,name,desc,pos):
        self.name = name
        self.desc = desc
        self.pos = pos

class playerinstance():
    def __init__(self,inv,basechar):
        self.inv = inv
        self.pos = basechar.pos
        self.name = basechar.name
        self.desc = basechar.desc

class camera():
    def __init__(self):
        self.cx = 0
        self.cy = 0
        self.targetx = 0
        self.targety = 0
        self.percentage = 1
        self.lx =0
        self.ly = 0
        self.steps = 1
    def lerp(self,v1,v2,percentage):
        return (v1 + ((v2-v1)*percentage))
    def move(self,tx,ty,steps=10):
        self.targetx = tx
        self.targety = ty
        self.lx = self.cx
        self.ly = self.cy
        self.steps = steps
        self.percentage = 0
    def tp(self,tx,ty):
        self.steps = 0
        self.percentage = 0
        self.lx = tx
        self.ly = ty
        self.targetx = tx
        self.targety = ty
        self.cx = tx
        self.cy = ty
    def run(self):
        if (self.percentage < self.steps):
            self.percentage = self.percentage +1
            self.cx = self.lerp(self.lx,self.targetx,1/((self.steps - self.percentage)+0.000001))
            self.cy = self.lerp(self.ly,self.targety,1/((self.steps - self.percentage)+0.000001))
        if self.percentage >= self.steps :
            self.cx = self.targetx
            self.cy = self.targety
message = ["",0]
class render():
    def __init__(self):
        global X,Y
        self.optbuffer = {}
        self.tilebuffer = {} ##this serves as a buffer for
        self.skytexture = xtexture("img/sky.png").gt()
        self.wateroffsetext = waterFX.generate_texture(pygame.time.get_ticks()/2000,40,40)
        self.screen  = pygame.display.set_mode((X, Y))
        self.vbuffer  = pygame.surface.Surface((840, 840)).convert()
        self.wrfb = pygame.surface.Surface((40,4)).convert()
        self.wrfb2 = pygame.surface.Surface((40,8)).convert()
        self.playerpreimg =  pygame.transform.scale( pygame.image.load("img/player.png"),(40,40))
        self.highlight =  pygame.transform.scale( pygame.image.load("img/hilight.png"),(40,40))
        self.arenaimg =  pygame.image.load("img/battlearena.png")
    def gets(self,value,t="False"):
        if t == True:
            return value #- (value % 10)
        else:
            return ((value-8) % 1)*-40
    def shaderz(self):
        for x in range(1,320):
            for y in range(1,320):
                color = self.screen.get_at((x, y))
    def renderarena(self):
        self.screen.blit(self.arenaimg,(0,0))
    def hash_tile(self,tile1,tile2,tile4,tile5,tile6):
        if tile2 == "none":
            return hash(str(type(tile1).__name__)+str(tile4)+str(tile5)+str(tile6))
        else:
            return hash(type(tile1).__name__ + type(tile2).__name__+str(tile4)+str(tile5)+str(tile6))
    def renderwmp(self,camera,xgmap,frametime):
        global mousepos,message,onweb,selectedt
        performance = 0
        #watertxt = waterFX.apply_ripple(,wateroffsetext,3,2)
        getmessage()
        wvb = []
        vb1 =[]
        vb2 = []
        vb3 = []
        vb4 = []
        vb5 = []
        csound=0
        wimg = ""
        wimgb = ""
        for xtt in range(-1,17):
            for ytt in range(0,18):
                x = xtt 
                y = ytt
                threed = True
                tile = xgmap.heightmap.rmmap((x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)))
                tile2= xgmap.structuremap.rmmap((x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)),True)
                #tile3= xgmap.readraw(xgmap.threedeffecthax,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True))
                tile4= xgmap.getheight(x + self.gets(camera.cx,True),y + self.gets(camera.cy,True))
                tile5=xgmap.getheight(x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)+1)
                tile6 = xgmap.getheight(x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)-1)
                img = tile.gtx(frametime).gt()
                if tile2 == "none":
                    txa = 0
                else:
                    if tile2.name == "townmarker":
                        csound = 1
                    try:
                        txa = tile2.animated
                    except:
                         tile2.animated = 0
                         txa = 0
                stile = 0        
                
                t = self.hash_tile(tile,tile2,tile4,tile5,tile6)
                xtu =str(x) +","+str( y)
                if xtu in self.optbuffer:
                    if self.optbuffer[xtu] == t:
                        stile = 1
                    else:
                        self.optbuffer[xtu] = t
                else:
                    self.optbuffer[xtu] = t
                if not ( tile.animated == 0 and txa ==0):
                    stile = 0
                    self.optbuffer[xtu] = t
                if tile.name == "water":
                    stile = 0
                if stile == 0:        
                    if not tile.name == "water":
                        ximg = img.copy()
                        if hasattr(tile,"reflectivity"):
                                xti = ""
                                xti = waterFX.get_texture_slice(self.skytexture,(xtt*40)+self.gets(camera.cx),(ytt*40)+self.gets(camera.cy))
                                xti.set_alpha(tile.reflectivity)
                                
                                ximg.blit(xti,(0,0))
                        vb1.append((ximg,(x*40,y*40)))
                    else:
                        if wimg == "":
                            if (frametime % 4 ) == 1:
                                self.wateroffsetext = waterFX.generate_texture(pygame.time.get_ticks()/2000,40,40)
                            wimg = waterFX.apply_ripple(img,self.wateroffsetext,3,2)
                        xti = ""
                        xti = waterFX.get_texture_slice(self.skytexture,(xtt*40)+self.gets(camera.cx),(ytt*40)+self.gets(camera.cy))
                        #xti = waterFX.apply_ripple(xti,self.wateroffsetext,3,2)
                        xti.set_alpha(50)
                        wimgx = wimg.copy()
                        wimgx.blit(xti,(0,0))
                        
                            #wimg = img
                            #wimg = wateroffsetext
                        wvb.append((wimgx,(x*40,y*40)))
                        if performance == 0:
                            if tile.name == "water" and tile2 == "none":
                                wtile = xgmap.read(xgmap.heightmap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)+1)
                                wtile2 = xgmap.read(xgmap.structuremap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)+1,True)
                                if not wtile.name == "water":
                                    self.wrfb.blit(pygame.transform.scale(pygame.transform.flip(wtile.gt().gt(), False, False), (40, 4)),[0,0])
                                    if not wtile2 == "none":
                                        if not wtile2.name ==  "steppingstones":
                                             self.wrfb.blit(pygame.transform.scale(pygame.transform.flip(wtile2.gt().gt(), False, False), (40, 4)),[0,0])
                                    #self.wrfb.set_alpha(125)
                                    self.wrfb = waterFX.apply_ripple(self.wrfb,self.wateroffsetext,3,2)
                                    self.wrfb.set_alpha(100)
                                    vb5.append((self.wrfb,(x*40,y*40+36)))
                                wtile = xgmap.read(xgmap.heightmap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)-1)
                                wtile2 = xgmap.read(xgmap.structuremap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)-1,True)
                                if not wtile.name == "water":
                                    self.wrfb2.blit(pygame.transform.scale(pygame.transform.flip(wtile.gt().gt(), False, True), (40, 8)),[0,0])
                                    if not wtile2 == "none":
                                        if not wtile2.name ==  "steppingstones":
                                            self.wrfb2.blit(pygame.transform.scale(pygame.transform.flip(wtile2.gt().gt(), False, True), (40, 8)),[0,0])
                                    self.wrfb = waterFX.apply_ripple(self.wrfb,self.wateroffsetext,3,2)
                                    self.wrfb.set_alpha(100)
                                    vb5.append((self.wrfb,(x*40,y*40)))
                                    
                    if not (tile2 == "none"):
                        if tile2.name == "steppingstones":
                           threed = False
                        img2 = xgmap.read(xgmap.structuremap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True),exc="gt()").gt()
                        if tile2.name =="wheat":
                            if wimgb == "":
                                wimgb = waterFX.apply_waving_effect(img2,tile2.wavetxt.gt(),5,120,5,frametime)
                            img2 = wimgb
                        if not tile2.hidden:
                            ximg2 = img2.copy()
                            if hasattr(tile2,'reflectivity'):
                                xti = ""
                                xti = waterFX.get_texture_slice(self.skytexture,(xtt*40)+self.gets(camera.cx),(ytt*40)+self.gets(camera.cy))
                                xti.set_alpha(tile2.reflectivity)
                                ximg2.blit(xti,(0,0))
                            if  tile2.place_last: 
                                vb2.append((ximg2,(x*40,y*40)))
                            else:
                                vb3.append((ximg2,(x*40,y*40)))
                    if threed == True:
                      if not (tile5 == (0,255,255,255) or tile5 == "none" or tile5 == (255,0,0,255) ):
                          if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                               if (tile4) > (tile5):
                                   vb3.append((xgmap.threedoverlay,(x*40,y*40)))
                      if not (tile6 == (0,255,255,255) or tile6 == "none" or tile6 == (255,0,0,255) ):
                          if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                               if (tile4) > (tile6):
                                   vb4.append((xgmap.threedoverlay2,(x*40,y*40)))
                       
        if len(wvb)>0:
            #wvb = waterFX.apply_ripple_to_blits(wvb,wateroffsetext,3,2)
            self.vbuffer.blits(wvb)           
        self.vbuffer.blits(vb1)
        if len(vb2)>0:
            self.vbuffer.blits(vb2)
        if len(vb3) > 0:
            self.vbuffer.blits(vb3)
        if len(vb4) > 0:
            self.vbuffer.blits(vb4)
        if len(vb5) > 0:
            self.vbuffer.blits(vb5)
        
            
        
        blitpos = [0,0]
        if list(mousepos) == [-1,0]:
            blitpos = ((140*2) +self.gets(camera.cx),(160*2) )
        elif list(mousepos) == [1,0] :
            blitpos = ((200*2)+self.gets(camera.cx) ,(160*2) )
        elif list(mousepos) == [0,1]:
            blitpos = ((160*2) ,(200*2)+self.gets(camera.cy) )
        elif list(mousepos) == [0,-1] :
            blitpos = ((160*2) ,(140*2) +self.gets(camera.cy)) 
        t=self.vbuffer
        #t = waterFX.apply_color_curves(t, 1, 1.0, 1.0)
        #t = waterFX.apply_bloom(t,3,245,2)
        #t=self.vbuffer
        #t = waterFX.apply_color_curves(t, 0.8, 0.9, 0.7)
        
        blitpos = list(blitpos)
        #blitpos[0] = blitpos[0]*2
        #blitpos[1] = blitpos[1]*2
        intsound(csound) 
        self.screen.blit(t,(self.gets(camera.cx),self.gets(camera.cy)))
        self.screen.blit(self.playerpreimg,(159*2,159*2))
        self.screen.blit(self.highlight,blitpos)
        return blitpos

        
        

##initialise stuff
drawsys = render()
mycam = camera()
mycam.tp(218,40)
#mycam.tp(226,26)
#mycam.tp(480,240)
cplayer.pos[0] = 218
cplayer.pos[1] = 21
#cplayer.pos[0] = 405#uncomment to tp to oilrig
#cplayer.pos[1] = 33
frametime = 0
drawsys.screen =  pygame.display.set_mode((X,Y))
def gtcpos(t=False):
    global cplayer,mousepos
    rlpos = mousepos
    if not t:
        return [cplayer.pos[0] + rlpos[0],cplayer.pos[1] + rlpos[1]]
    else:
        return [cplayer.pos[0]  +8+ rlpos[0],cplayer.pos[1] +8+ rlpos[1]]
def interact(rlpos=None):
    global ccmd,cmap,cplayer,mousepos,message,ActionQueue
    if rlpos == None:
        rlpos = mousepos
        t = cmap.gettile(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],1)
        #t.pos = [cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1]]
        if t.name == "vendingmachine":
            dlgtree.cnpcdial = UIdialogdef.vendingmachinedia(xmap.tiledef.testlist,cplayer.inventory.getcount("coin"))
        if t.interactable :
            res = t.interact(cplayer,cmap)
            if len(res) > 0:
                cplayer = res[0]
            if len(res) > 1:
                cmap = res[1]
            if len(res)>3:
                t = res[3]
                cmap.setmap(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],t)
            if t.callback(test=1):
                ActionQueue.append([cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1]])
                
            
    else:
        t = cmap.gettile(rlpos[0] ,rlpos[1],1)
        t.pos = rlpos
        if t.interactable :
            res = t.callback(cmap,cplayer,test=0)
            if len(res) > 0:
                cmap = res[0]
            if len(res) > 1:
                cplayer = res[1]
            if len(res)>3:
                t = res[3]
                cmap.setmap(rlpos[0] ,rlpos[1],t)


def getmessage():
    global message,cplayer,mousepos,dbbtn
    rlpos = mousepos
    mg = cmap.gettile(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],1)
    mg2 = cmap.gettile(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],-1)
    try:
        message = mg.message
    except:
        #print(cmap.gettile(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],1))
          io=0
    #try:
    if hasattr(mg2,'PBA'):
        if mg2.PBA ==1:
            dbbtn.enabled = 1
        else:
            dbbtn.enabled = 0
    else:
        dbbtn.enabled = 0
    #except:
        io = 0
        
    
    
###helper function
isinvo = False
endtime = 0
for i in range(1,100):
    cplayer.inventory.invadds("coin")
    cplayer.inventory.invadds("tile_tree")
dlgtree.cnpcdial = dlgtree.UIdialogbase()
#dlgtree.cnpcdial = UIdialogdef.vendingmachinedia(xmap.tiledef.testlist,1)
#
dlgtree.cnpcdial.active = 1
clock = pygame.time.Clock()
def main():
    global clock,cplayer, ccmd,markp, pos1,pos2, selectedt, endtime, isinvo,mycam,drawsys,frametime,cmap,ACTIVEAREA,AREAS,transition, mousepos,pactare,ActionQueue,dlgtree,message
    start_time = time.time()
    dt = clock.tick(50)
    #time.sleep(1/31)
    mycam.move(cplayer.pos[0],cplayer.pos[1])
    frametime = frametime + 1 % 120
    tiledef.npcdia.quests = tiledef.quests
    mycam.run()
       # except:
           # ActionQueue = []
           # print("ActionQueue failed")
            
    if not (isinvo or  dlgtree.cnpcdial.active)  :
        if len(ActionQueue) > 0:
            interact(ActionQueue[0])
            del(ActionQueue[0])
        if ACTIVEAREA == "WMP":
            start_time = time.time()
            blitpos = drawsys.renderwmp(mycam,cmap,frametime)
            ptext.draw( str(message), (blitpos[0],blitpos[1]+20), shadow=(1.0,1.0), scolor="blue",fontsize=16)
            ptext.draw( "" +str(cplayer.pos[0]) +","+ str(cplayer.pos[1]) + " fps:" + str((1000/dt)), (10, 0), shadow=(1.0,1.0), scolor="blue",fontsize=16)

        elif ACTIVEAREA == "ARENA":
            drawsys.renderarena()
    if isinvo :
        temp = irender(cplayer.inventory.inv)
        cplayer.inventory.inv = temp[1]
        if temp[0] == 1 :
            isinvo = False

    
    #pygame.display.update()
    pokeinteraction = 0
    pokelevel = 0
   # print(dt)
    if not (isinvo or  dlgtree.cnpcdial.active)  : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if 'click' in intbtn.handleEvent(event):
                    interact()
            if 'click' in invbtn.handleEvent(event):
                isinvo = True
            if 'click' in svbtn.handleEvent(event):
                save("default")
            if 'click' in lvbtn.handleEvent(event):
                load("default")
            if 'click' in dbbtn.handleEvent(event):
                s = gtcpos(True)
                seltile = cmap.heightmap.rmmap(s)
                if hasattr(seltile,'PBA'):
                    if seltile.PBA ==1 :
                        dlgtree.cnpcdial = UIdialogdef.invdia(s[0],s[1])
                
            if event.type == pygame.KEYDOWN and ACTIVEAREA == "WMP" and not isinvo:
                
                keyeventlist = [0,0,0,0]
                cplayer.pos[0] = cplayer.pos[0]
                cplayer.pos[1] = cplayer.pos[1]
                if event.key == pygame.K_RIGHT:
                    keyeventlist[1] = 1
                    mousepos = [1,0]
                elif event.key == pygame.K_LEFT:
                    keyeventlist[0] = 1
                    mousepos = [-1,0]
                elif event.key == pygame.K_UP:
                    keyeventlist[2] = 1
                    mousepos = [0,-1]
                elif event.key == pygame.K_DOWN:
                    keyeventlist[3] = 1
                    mousepos = [0,1]
                elif event.key == pygame.K_SPACE:
                    interact()
                elif event.key == pygame.K_q:
                    pass#(str(cplayer.pos[1]) + "'" + str(cplayer.pos[0]))
                elif event.key == pygame.K_w:
                    keyeventlist[2] = 1
                    mousepos = [0,-1]
                elif event.key == pygame.K_a:
                    keyeventlist[0] = 1
                    mousepos = [-1,0]
                elif event.key == pygame.K_s:
                    keyeventlist[3] = 1
                    mousepos = [0,1]
                elif event.key == pygame.K_d:
                    keyeventlist[1] = 1
                    mousepos = [1,0]
                elif event.key == pygame.K_PAGEDOWN:
                    selectedt += 1
                    selectedt = selectedt % len(cmap.tiles)
                elif event.key == pygame.K_PAGEUP:
                    selectedt +=-1
                    selectedt = selectedt % len(cmap.tiles)
                elif event.key == pygame.K_0 and onweb == 0:
                    print(str([gtcpos(True),cmap.tiles[selectedt].name + cmap.tiles[selectedt].__class__.__name__,1])+",",end='')
                    cmap.structuremap.smmap(gtcpos(True),cmap.tiles[selectedt])
                elif event.key == pygame.K_o and onweb == 0:
                    print(str([gtcpos(True),cmap.tiles[selectedt].name + cmap.tiles[selectedt].__class__.__name__,0])+",",end='')
                    cmap.heightmap.smmap(gtcpos(True),cmap.tiles[selectedt])
                elif event.key == pygame.K_1 and onweb == 0:
                            pos1 = gtcpos(True)
                elif event.key == pygame.K_f and onweb == 0:
                            for tx in gprt(pos1[0],pos2[0]):
                                for ty in gprt(pos1[1],pos2[1]):
                                    print(str([[tx,ty],cmap.tiles[selectedt].name + cmap.tiles[selectedt].__class__.__name__,1])+",",end='')
                                    cmap.structuremap.smmap([tx,ty],cmap.tiles[selectedt])
                elif event.key == pygame.K_2 and onweb == 0:
                    pos2 = gtcpos(True)

                nexttile = 0
                if keyeventlist == [1,0,0,0] and ACTIVEAREA == "WMP":
                    #for i in range(int((1+(1000/max(1,dt))*2))):
                        if cmap.gettile(cplayer.pos[0] -1,cplayer.pos[1],4) == 1:
                            nexttile = cmap.gettile(cplayer.pos[0] -1,cplayer.pos[1],1)
                            cplayer.pos[0] = cplayer.pos[0] - 1
                        
                elif keyeventlist == [0,0,1,0]:
                    #for i in range(int(((1000/max(1,dt))*1))):
                        if cmap.gettile(cplayer.pos[0],cplayer.pos[1]-1,4) == 1:
                            nexttile = cmap.gettile(cplayer.pos[0],cplayer.pos[1]-1,1)
                            cplayer.pos[1] = cplayer.pos[1] - 1
                        
                elif keyeventlist == [0,0,0,1]:
                   # for i in range(int((1000/max(1,dt))*1)):
                        if cmap.gettile(cplayer.pos[0],cplayer.pos[1]+1,4) == 1:
                            nexttile = cmap.gettile(cplayer.pos[0],cplayer.pos[1]+1,1)
                            cplayer.pos[1] = cplayer.pos[1] + 1
                        
                elif keyeventlist == [0,1,0,0]:
                    #for i in range(int((1000/max(1,dt))*1)):
                        if cmap.gettile(cplayer.pos[0] +1,cplayer.pos[1],4) == 1:
                            nexttile =  cmap.gettile(cplayer.pos[0] +1,cplayer.pos[1],1)
                            cplayer.pos[0] = cplayer.pos[0] + 1
                if  nexttile != 0 and len(nexttile.attributes) > 1:
                    #print(nexttile)
                    if nexttile.attributes[1] > 0:
                        pokeinteraction = nexttile.attributes[1]
                        pokelevel = nexttile.attributes[2]
                cplayer.pos[0] = cplayer.pos[0]
                cplayer.pos[1] = cplayer.pos[1]
            
    if transition[0] < 0.5:
            transition[0] = transition[0] + 0.01
            EM.transition(drawsys.screen,transition[0] )
            EM.transition(drawsys.screen,transition[0] )
            
            ACTIVEAREA = transition[1]
    elif transition[0] < 1:
            transition[0] = transition[0] + 0.01
            EM.transition(drawsys.screen,(1-transition[0] * 2) )
            EM.transition(drawsys.screen,(1-transition[0] * 2) )
            if not ACTIVEAREA in ["inventory"]:
                ACTIVEAREA = transition[2]
    else:
        if not ACTIVEAREA in ["inventory"]:
            ACTIVEAREA = transition[2]
   # try:
    if 0==0:
         if  dlgtree.cnpcdial.active:
             if not hasattr(dlgtree.cnpcdial,'runUI'):
                dlgtree.cnpcdial = dlgtree.rnbcdialog(dlgtree.cnpcdial)
             else:
                dlgtree.cnpcdial.cmap = cmap
                dlgtree.cnpcdial.drawsys = drawsys
                dlgtree.cnpcdial.cplayer = cplayer
                if dlgtree.cnpcdial.initialised == 0:
                    dlgtree.cnpcdial.initialise()
                dlgtree.cnpcdial.runUI()
                cmap = dlgtree.cnpcdial.cmap
                drawsys = dlgtree.cnpcdial.drawsys
                cplayer = dlgtree.cnpcdial.cplayer
                if dlgtree.cnpcdial.active == 0 and hasattr(dlgtree.cnpcdial,"returndialog"):
                    try:
                        dlgtree.cnpcdial = standartUIdialogref.SR[dlgtree.cnpcdial.returndialog]
                    except:
                        io = 0
                    
                
   # except Exception as ex23:
        #print(ex23)
        #print(dlgtree.cnpcdial)
        #dlgtree.cnpcdial = dlgtree.ddialog()
        
    if not (isinvo or  dlgtree.cnpcdial.active)  :
        pygame.draw.rect(drawsys.screen, (245,235,250), pygame.Rect(scale(320, 0, 420, 320)))
        teal = 0.8
        tealx = 0.7
        pygame.draw.rect(drawsys.screen, (int(245*teal),int(235*teal),int(250*teal)), pygame.Rect(scale(322, 2, 418, 98)))
        pygame.draw.rect(drawsys.screen, (int(25*tealx),int(235*tealx),int(29*tealx)), pygame.Rect(scale(322 + (cplayer.pos[0]*0.2), 2+(cplayer.pos[1]*0.2), 2, 2)))
        if ACTIVEAREA == "WMP":
            invbtn.draw(drawsys.screen)
            intbtn.draw(drawsys.screen)
            svbtn.draw(drawsys.screen)
            lvbtn.draw(drawsys.screen)
            dbbtn.draw(drawsys.screen)
            if onweb == 0:
                drawsys.screen.blit(cmap.tiles[selectedt].gt().gt(),(650,200))
            ####other world related GUI is to be drawn here###
            #                                                #
            #                                                #
            ##################################################
            
     # FPS = 1 / time to process loop
    endtime = time.time()
    #pygame.time.wait(10)
    
    #time.sleep(1/43)
    

if __name__ == "__main__":
    #svimg(cmap) #--generates map image (only uncomment if changing map and need preview to prevent to many disk writes
    import main
    mycam.tp( 52,13)
    cplayer.pos = [52,13]
