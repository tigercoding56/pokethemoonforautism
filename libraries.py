import pygame
import PIL
import gc
from renderbase import svimg
from PIL import Image
import time
import ptext
import pickle
#import maingui as agui
#from maingui import App
import enemies as EM
from xmap import dlgtree
from xmap import *
from inventory import cplayer  , irender
from pygamebutton import PygButton

if __import__("sys").platform == "emscripten":
    from platform import window



ActionQueue =[]
mousepos = [1,0]
transition = [1,"WMP","WMP"]
#transition = [0,"WMP","ARENA"]
AREAS = ["WMP","ARENA","INV"]## these will be implemented later
ACTIVEAREA = "WMP"# WMP = world map , so the default playing area is handled while WMP is active 
X = 840
Y = 640
cmap = gmap(tiles)
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
intbtn = PygButton(caption="interact ",rect=scale(320,300,100,20))
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

player = playerinstance([],characterinstance("player","the player",(226,26)))
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
        self.screen  = pygame.display.set_mode((X, Y))
        self.vbuffer  = pygame.surface.Surface((840, 640))
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
    def renderwmp(self,camera,xgmap,frametime):
        global mousepos,message
        getmessage()
        for x in range(-1,17):
            for y in range(-1,17):
                x = x 
                y = y
                threed = True
                tile = xgmap.read(xgmap.heightmap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True))
                tile2= xgmap.read(xgmap.structuremap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True),True)
                #tile3= xgmap.readraw(xgmap.threedeffecthax,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True))
                tile4= xgmap.readraw(xgmap.threedfx,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True))
                tile5= xgmap.readraw(xgmap.threedfx,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)+1)
                tile6 = xgmap.readraw(xgmap.threedfx,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True)-1)
                img = tile.gtx(frametime).gt()
                self.vbuffer.blit(img,(x*40+self.gets(camera.cx),y*40+self.gets(camera.cy)))
                if not tile2 == "none":
                    if tile2.name == "steppingstones":
                       threed = False
                    img2 = xgmap.read(xgmap.structuremap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True),exc="gt()").gt()
                    self.vbuffer.blit(img2,(x*40+self.gets(camera.cx),y*40+self.gets(camera.cy)))
                if threed == True:
                  if not (tile5 == (0,255,255,255) or tile5 == "none" or tile5 == (255,0,0,255) ):
                      if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                           if (tile4[0]) > (tile5[0]):
                               self.vbuffer.blit(xgmap.threedoverlay,(x*40+self.gets(camera.cx),y*40+self.gets(camera.cy)))
                  if not (tile6 == (0,255,255,255) or tile6 == "none" or tile6 == (255,0,0,255) ):
                      if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                           if (tile4[0]) > (tile6[0]):
                               self.vbuffer.blit(xgmap.threedoverlay2,(x*40+self.gets(camera.cx),y*40+self.gets(camera.cy)))
                           
                           
                           
                self.vbuffer.blit(self.playerpreimg,(159*2,159*2))
                blitpos = [0,0]
                if list(mousepos) == [-1,0]:
                    blitpos = ((140*2) + self.gets(camera.cx),(160*2) )
                elif list(mousepos) == [1,0] :
                    blitpos = ((200*2) + self.gets(camera.cx),(160*2) )
                elif list(mousepos) == [0,1]:
                    blitpos = ((160*2) ,(200*2) + self.gets(camera.cy))
                elif list(mousepos) == [0,-1] :
                    blitpos = ((160*2) ,(140*2) + self.gets(camera.cy))
                self.vbuffer.blit(self.highlight,blitpos)
                t = self.vbuffer
                blitpos = list(blitpos)
                blitpos[0] = blitpos[0]*2
                blitpos[1] = blitpos[1]*2
                self.screen.blit(t,(0,0))
                ptext.draw( str(message), (blitpos[0],blitpos[1]+20), shadow=(1.0,1.0), scolor="blue",fontsize=16)
                    

        
        

##initialise stuff
drawsys = render()
mycam = camera()
mycam.tp(218,40)
mycam.tp(226,26)
cplayer.pos[0] = 218
cplayer.pos[1] = 21
frametime = 0
drawsys.screen =  pygame.display.set_mode((X,Y))
def interact(rlpos=None):
    global cmap,cplayer,mousepos,message,ActionQueue
    if rlpos == None:
        rlpos = mousepos
        t = cmap.gettile(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],1)
        t.pos = [cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1]]
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
    global message,cplayer,mousepos
    rlpos = mousepos
    try:
        message = cmap.gettile(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],1).message
    except:
        print(cmap.gettile(cplayer.pos[0]+rlpos[0] ,cplayer.pos[1]+rlpos[1],1))
            
        
    
    
###helper function
isinvo = False
def main():
    start_time = time.time()
    global isinvo,mycam,drawsys,frametime,cmap,ACTIVEAREA,AREAS,transition, mousepos,pactare,ActionQueue,dlgtree
    mycam.move(cplayer.pos[0],cplayer.pos[1])
    frametime = frametime + 1 % 20
    mycam.run()
       # except:
           # ActionQueue = []
           # print("ActionQueue failed")
            
    if not (isinvo or  dlgtree.cnpcdial.active)  :
        if len(ActionQueue) > 0:
            interact(ActionQueue[0])
            del(ActionQueue[0])
        if ACTIVEAREA == "WMP":
            drawsys.renderwmp(mycam,cmap,frametime)
            ptext.draw( "" +str(cplayer.pos[0]) +","+ str(cplayer.pos[1]), (10, 0), shadow=(1.0,1.0), scolor="blue",fontsize=16)

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
    if not (isinvo or  dlgtree.cnpcdial.active)  : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if 'click' in intbtn.handleEvent(event):
                    interact()
            if 'click' in invbtn.handleEvent(event):
                isinvo = True
            if event.type == pygame.KEYDOWN and ACTIVEAREA == "WMP" and not isinvo:
                
                keyeventlist = [0,0,0,0]
                camerax = cplayer.pos[0]
                cameray = cplayer.pos[1]
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
                nexttile = 0
                if keyeventlist == [1,0,0,0] and ACTIVEAREA == "WMP":
                    if cmap.gettile(cplayer.pos[0] -1,cplayer.pos[1],4) == 1:
                        nexttile = cmap.gettile(cplayer.pos[0] -1,cplayer.pos[1],1)
                        camerax = camerax - 1
                        
                elif keyeventlist == [0,0,1,0]:
                    if cmap.gettile(cplayer.pos[0],cplayer.pos[1]-1,4) == 1:
                        nexttile = cmap.gettile(cplayer.pos[0],cplayer.pos[1]-1,1)
                        cameray = cameray - 1
                        
                elif keyeventlist == [0,0,0,1]:
                    if cmap.gettile(cplayer.pos[0],cplayer.pos[1]+1,4) == 1:
                        nexttile = cmap.gettile(cplayer.pos[0],cplayer.pos[1]+1,1)
                        cameray = cameray + 1
                        
                elif keyeventlist == [0,1,0,0]:
                    if cmap.gettile(cplayer.pos[0] +1,cplayer.pos[1],4) == 1:
                        nexttile =  cmap.gettile(cplayer.pos[0] +1,cplayer.pos[1],1)
                        camerax = camerax + 1
                if  nexttile != 0 and len(nexttile.attributes) > 1:
                    print(nexttile)
                    if nexttile.attributes[1] > 0:
                        pokeinteraction = nexttile.attributes[1]
                        pokelevel = nexttile.attributes[2]
                cplayer.pos[0] = camerax
                cplayer.pos[1] = cameray
            
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
    if  dlgtree.cnpcdial.active:
        dlgtree.cnpcdial = dlgtree.rnbcdialog(dlgtree.cnpcdial)
    if not (isinvo or  dlgtree.cnpcdial.active)  :
        pygame.draw.rect(drawsys.screen, (245,235,250), pygame.Rect(scale(320, 0, 420, 320)))
        if ACTIVEAREA == "WMP":
            invbtn.draw(drawsys.screen)
            intbtn.draw(drawsys.screen)
            ####other world related GUI is to be drawn here###
            #                                                #
            #                                                #
            ##################################################
            
    if frametime % 11== 10:    
        print("Frametime ",  (time.time() - start_time)) # FPS = 1 / time to process loop
  

if __name__ == "__main__":
    #svimg(cmap) #--generates map image (only uncomment if changing map and need preview to prevent to many disk writes
    import main
    mycam.tp( 52,13)
    cplayer.pos = [52,13]
