import pygame
import PIL
from PIL import Image
import time
import ptext
import enemies
from xmap import *
import pygame_gui
pygame.init()
#manager = pygame_gui.UIManager((320, 320))
X = 320
Y = 320
pygame.key.set_repeat(250)

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
            if self.percentage == self.steps :
                self.cx = self.targetx
                self.cy = self.targety

class render():
    def __init__(self):
        global X,Y
        self.screen  = pygame.display.set_mode((X, Y))
        self.playerpreimg =  pygame.image.load("img/player.png")
    def gets(self,value,t="False"):
        if t == True:
            return value #- (value % 10)
        else:
            return ((value-8) % 1)*-20
    def shaderz(self):
        for x in range(1,320):
            for y in range(1,320):
                color = self.screen.get_at((x, y))
    def render(self,camera,xgmap,frametime):
        for x in range(-1,17):
            for y in range(-1,17):
                x = x 
                y = y 
                tile = xgmap.read(xgmap.heightmap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True))
                tile2= xgmap.read(xgmap.structuremap,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True),True)
                tile3= xgmap.readraw(xgmap.threedeffecthax,x + self.gets(camera.cx,True),y + self.gets(camera.cy,True))
                img = tile.texture
                if not tile.textures == []:
                    img = tile.textures[int(frametime * 0.05) % len(tile.textures)]
                self.screen.blit(img,(x*20+self.gets(camera.cx),y*20+self.gets(camera.cy)))
                if not tile2 == "none":
                    img2 = tile2.texture
                    if not tile2.textures == []:
                        img2 = tile2.textures[int(frametime * 0.05) % len(tile2.textures)]
                    self.screen.blit(img2,(x*20+self.gets(camera.cx),y*20+self.gets(camera.cy)))
                if not (tile3 == (0,0,0,255) or tile3 == "none"):
                    self.screen.blit(xgmap.threedoverlay,(x*20+self.gets(camera.cx),y*20+self.gets(camera.cy)))
                self.screen.blit(self.playerpreimg,(159,159))
                    

        
        


cmap = gmap(tiles)
drawsys = render()
mycam = camera()
mycam.tp(218,40)
camx = 218
camy = 21
frametime = 0

def interact():
    global cmap,camx,camy
    print(cmap.gettile(camx,camy))
def main():
    global mycam,camx,drawsys,camy,frametime,cmap, #manager
    mycam.move(camx,camy)
    frametime = frametime + 1 % 20
    mycam.run()
    time.sleep(0.05)
    drawsys.render(mycam,cmap,frametime)
    ## code for ui can go here:
    
    #manager.draw_ui(window_surface)
    #
    ptext.draw( "" +str(camx) +","+ str(camy), (10, 0), shadow=(1.0,1.0), scolor="blue")
    pygame.display.update()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.quit()
  
        if event.type == pygame.KEYDOWN:
            keyeventlist = [0,0,0,0]
            camerax = camx
            cameray = camy
            if event.key == pygame.K_RIGHT:
                keyeventlist[1] = 1
            elif event.key == pygame.K_LEFT:
                keyeventlist[0] = 1
            elif event.key == pygame.K_UP:
                keyeventlist[2] = 1
            elif event.key == pygame.K_DOWN:
                keyeventlist[3] = 1
            elif event.key == pygame.K_SPACE:
                interact()
            elif event.key == pygame.K_q:
                pass#(str(camy) + "'" + str(camx))
            elif event.key == pygame.K_w:
                keyeventlist[2] = 1
            elif event.key == pygame.K_a:
                keyeventlist[0] = 1
            elif event.key == pygame.K_s:
                keyeventlist[3] = 1
            elif event.key == pygame.K_d:
                keyeventlist[1] = 1

            if keyeventlist == [1,0,0,0]:
                if cmap.gettile(camx -1,camy,4) == 1:
                    camerax = camerax - 1
            elif keyeventlist == [0,0,1,0]:
                if cmap.gettile(camx,camy-1,4) == 1:
                    cameray = cameray - 1
            elif keyeventlist == [0,0,0,1]:
                if cmap.gettile(camx,camy+1,4) == 1:
                    cameray = cameray + 1
            elif keyeventlist == [0,1,0,0]:
                if cmap.gettile(camx +1,camy,4) == 1:
                    camerax = camerax + 1
            camx = camerax
            camy = cameray
            

  


