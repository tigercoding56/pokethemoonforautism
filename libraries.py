import pygame
import PIL
import gc
from renderbase import svimg
from PIL import Image
import time
import ptext
import pickle
import maingui as agui
from maingui import App
import enemies as EM
from xmap import *
from inventory import cplayer  , irender
from pygamebutton import PygButton
mousepos = [1,0]
transition = [1,"WMP","WMP"]
#transition = [0,"WMP","ARENA"]
AREAS = ["WMP","ARENA","INV"]## these will be implemented later
ACTIVEAREA = "WMP"# WMP = world map , so the default playing area is handled while WMP is active 
X = 420
Y = 320
cmap = gmap(tiles)
######################
#player initial setup#
######################


######################




######################
#GUI setup           #
######################
invbtn = PygButton(caption="inventory",rect=(320,280,100,20))
intbtn = PygButton(caption="interact ",rect=(320,300,100,20))
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
        self.playerpreimg =  pygame.image.load("img/player.png")
        self.highlight =  pygame.image.load("img/hilight.png")
        self.arenaimg =  pygame.image.load("img/battlearena.png")
    def gets(self,value,t="False"):
        if t == True:
            return value #- (value % 10)
        else:
            return ((value-8) % 1)*-20
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
                self.screen.blit(img,(x*20+self.gets(camera.cx),y*20+self.gets(camera.cy)))
                if not tile2 == "none":
                    if tile2.name == "steppingstones":
                       threed = False
                    img2 = xgmap.read(xgmap.structuremap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True),exc="gt()").gt()
                    self.screen.blit(img2,(x*20+self.gets(camera.cx),y*20+self.gets(camera.cy)))
                if threed == True:
                  if not (tile5 == (0,255,255,255) or tile5 == "none" or tile5 == (255,0,0,255) ):
                      if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                           if (tile4[0]) > (tile5[0]):
                               self.screen.blit(xgmap.threedoverlay,(x*20+self.gets(camera.cx),y*20+self.gets(camera.cy)))
                  if not (tile6 == (0,255,255,255) or tile6 == "none" or tile6 == (255,0,0,255) ):
                      if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                           if (tile4[0]) > (tile6[0]):
                               self.screen.blit(xgmap.threedoverlay2,(x*20+self.gets(camera.cx),y*20+self.gets(camera.cy)))
                           
                           
                           
                self.screen.blit(self.playerpreimg,(159,159))
                blitpos = [0,0]
                if list(mousepos) == [-1,0]:
                    blitpos = (140 + self.gets(camera.cx),160 )
                elif list(mousepos) == [1,0] :
                    blitpos = (200 + self.gets(camera.cx),160 )
                elif list(mousepos) == [0,1]:
                    blitpos = (160 ,200 + self.gets(camera.cy))
                elif list(mousepos) == [0,-1] :
                    blitpos = (160 ,140 + self.gets(camera.cy))
                self.screen.blit(self.highlight,blitpos)
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
def interact():
    global cmap,cplayer,mousepos,message
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
    global isinvo,mycam,drawsys,frametime,cmap,ACTIVEAREA,AREAS,transition, mousepos,pactare
    mycam.move(cplayer.pos[0],cplayer.pos[1])
    frametime = frametime + 1 % 20
    mycam.run()
    if not isinvo:
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
    if not isinvo:
        if  not  agui.elementriev == "":
            if agui.elementriev == ['mn1', [0, 1, 0]]:
                if transition[0] > 0.9 and transition[2] == "WMP":
                    transition =  [0,"WMP","ARENA"]
                if transition[0] > 0.9 and transition[2] == "ARENA":
                    transition =  [0,"ARENA","WMP"]
            if agui.elementriev == ['mn1', [1, 0, 0]]:
               isinvo = True
                #openinv()
               print(agui.elementriev)
            agui.elementriev =""
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
    if not isinvo:
        pygame.draw.rect(drawsys.screen, (245,235,250), pygame.Rect(320, 0, 420, 320))
        if ACTIVEAREA == "WMP":
            invbtn.draw(drawsys.screen)
            intbtn.draw(drawsys.screen)
            ####other world related GUI is to be drawn here###
            #                                                #
            #                                                #
            ##################################################
            
        
    gc.collect(2)
  

if __name__ == "__main__":
    #svimg(cmap) #--generates map image (only uncomment if changing map and need preview to prevent to many disk writes
    import main
    mycam.tp( 52,13)
    cplayer.pos = [52,13]
