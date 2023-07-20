import ptext
import dialog
import time
import pygame.gfxdraw
import math
from  ptexture import ptexture
import pygame
import numpy
from pygamebutton import PygButton
from slider import SliderSwitch
ccredits = {
    "Curt":" \"Characters Zombies and Weapons Oh my \"- resource pack",
    "GrafxKid":"\Gum Bot sprites\"-used for various robot sprites ",
    "the tuxemon project":"inspiration (and also how i found the music for this game)",
    "Olivia,le":"some drawings which have been used to make background for cat characters \n about-me dialog section",
    "AndHeGames":"\"32x32 pixel art creatures volume 3\"- unused , but could be used later  \n(i am not sure if i will end up using them)",
    "Spring Spring":"\"Peasant kingdom\"-used as music in the wild (under cc-by 3.0)",
    "Yubatake":" \"JRPG collection \"-- JRPG_town_loop used for towns ",
    "isaiah658":"\" isaiah658's Pixel Pack #2 \"-some tiles of it are used",
    "Fleurman":"\"Laser Gate\"-used for laser gates",
    "BizmasterStudios":"\" Gold Coin/Token \" -base for coin texture ",
    "Proxy Games":"\" Wooden Crate Texture\"-texture for sound markers ( basically the game switches sound track \n if you see one of these tiles)",
    "chatgtp":"somewhat helping me optimise my code \n(although it is a pain to get it to do what you want)",
    "attribution notice for cc-by 3.0":"https://creativecommons.org/licenses/by/3.0/"
    
    
}
class UIdialogbase():
    def __init__(self):
        self.active = 1
        self.val = 0
        self.res = [840,640]
        self.buttons = {}
        self.sliders = []
        self.t=pygame.image.load('Resources/MISC_ASSETS/exitbtn.png')
        self.add_btn("exit","exitbtn",(0.05,0.05),text1=self.t,text2=self.t)
        self.initialised = 0
        self.frametime = 0 
    def scale(self,x,y):
        return [int(x*self.res[0]),int(y*self.res[1])]
    def initialise(self):
        self.add_btn("start game","exitbtn",(0,0.9),(1,0.1))
    def add_slider(self,name,pos,items=["ON","OFF"],size=[80,20],default=0):
        self.sliders.append([name,SliderSwitch(pos,size[0],size[1],items,default),(pos[0]-(len(name)*12)-int(size[0]*0.1)),pos[1]-(int(size[1]*0.4))])
    def add_btn(self,text,name,pos,size=(0.1,0.1),text1=None,text2=None,enabled=1):
        pos = self.scale(pos[0],pos[1])
        size=self.scale(size[0],size[1])
        t= PygButton(caption=text,rect=(pos[0],pos[1],size[0],size[1]),normal=text1,down=text1,highlight=text2)
        t.enabled = enabled
        self.buttons[name] = t 
    def renderframe(self):
        global ccredits
        #self.drawsys.screen
        teal = 0.1
        self.frametime = (self.frametime + 1)%((len(ccredits)*70)/4.5)
        #time.sleep(0.05)
        pygame.draw.rect(self.drawsys.screen, (int(245*teal),int(235*teal),int(250*teal)), pygame.Rect((self.scale(0, 0)+self.scale( 1, 1))))
        ptext.draw( "sorry , for the lack of a good storyline  , \n i am bad at writing good dialog ...", (20,20), color="white",fontsize=32)
        ptext.draw( "thank you to ", (60,100), color="white",fontsize=20)
        indexx = 0
        i = [6,4,7,8,4,5]
        icolors = ["blue","red","black","yellow","gold","silver","green"]
        for key in ccredits:
            name = key
            indexx += 1
            work = ccredits[key]
            ptext.draw( name + " for " + work, (20*i[indexx % 5],140+(((indexx*70))+(self.frametime*4.5) )%(len(ccredits)*70)), color=icolors[indexx%6],fontsize=30)
        #ptext.draw( " ", (30,70), shadow=(1.0,1.0), scolor="gold",fontsize=16)
    #def mouseklick(self,x,y):
        #pass
    def btnp(self,name):
        if name == "exitbtn":
            self.active = 0
    def touch(self,event):
        pass
    def keydown(self,key):
        pass
    def slider(self,name,value):
        pass
    def fill(self,x,y,w,h,bg,screen=None):
        if  screen ==  None:
             pygame.draw.rect(self.drawsys.screen, bg, (x, y, w, h))
        else:
             pygame.draw.rect(screen, bg, (x, y, w, h))
    def string(self,stri,x,y,width=0,color="white",size=16):#(string,x,y)
        ptext.draw(str(stri),pos=(x,y),color=color )
    def runUI(self):
        self.renderframe()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                for i in range(0,len(self.sliders)):
                    slider = self.sliders[i][1]
                    self.slider(self.sliders[i][0],slider.handle_event(event))
                    self.sliders[i][1] = slider
                    
                for key,value in self.buttons.items():
                    t= value.handleEvent(event)
                    #print(t)
                    if "down" in t:
                        self.btnp(key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.touch(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.active = 0
                    self.keydown(event.key)
        for key , value in self.buttons.items():
            value.draw(self.drawsys.screen)
        for i in range(0,len(self.sliders)):
            self.sliders[i][1].draw(self.drawsys.screen)
            ptext.draw(str(self.sliders[i][0]),pos=(self.sliders[i][2],self.sliders[i][3]),color="blue" )
        time.sleep(0.05)
dialog = UIdialogbase()
window = pygame.display.set_mode((840, 640))
class xt():
    def __init__(self):
        self.dr = 1
        self.screen =0 
dialog.drawsys = xt()

dialog.drawsys.screen = window
dialog.initialise()
while True:
    dialog.runUI()
    window = dialog.drawsys.screen
    pygame.display.flip()
