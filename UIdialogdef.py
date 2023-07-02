from planets import drawplanetsurface
from dialogtree import UIdialogbase
from dialogtree import pygame
import time
import ptext
from inventory import imxrender
import random
import waterFX


class IPXdraw():
    def __init__(self):
        pass
    def fill(x,y,w,h,bg,screen):
         pygame.draw.rect(screen, bg, (x, y, w, h))
class spaceobserverdia(UIdialogbase):
    def initialise(self):
        self.add_btn("exit","exitbtn",(0.9,0.9),(0.1,0.1))
        self.add_btn("left","left",(0.9,0.8),(0.1,0.1))
        self.add_btn("up","_up_",(0.9,0.7),(0.1,0.1))
        self.add_btn("right","right",(0.9,0.6),(0.1,0.1))
        self.add_btn("down","down",(0.9,0.5),(0.1,0.1))
        self.x = 0
        self.y = 0
        self.initialised = 1
    def renderframe(self):
        global ccredits
        #self.x = self.x +100
        #self.drawsys.screen
        #print(self.x)
        teal = 0.1
        teal2 = 0.9
        self.frametime = (self.frametime + 1)%200
        time.sleep(0.05)
        pygame.draw.rect(self.drawsys.screen, (int(245*teal),int(235*teal),int(250*teal)), pygame.Rect((self.scale(0, 0)+self.scale( 1, 1))))
        pygame.draw.rect(self.drawsys.screen, (int(245*teal2),int(235*teal2),int(250*teal2)), pygame.Rect((self.scale(0.9, 0)+self.scale( 1, 1))))
        t = drawplanetsurface(self.x,self.y,self.scale(0.9,1)[0],self.scale(1,1)[1])
        self.drawsys.screen.blit(t,(0,0))
        
        #ptext.draw( " ", (30,70), shadow=(1.0,1.0), scolor="gold",fontsize=16)
    #def mouseklick(self,x,y):
        #pass
    def btnp(self,name):
        if name == "exitbtn":
            self.active = 0
        if name == "right":
            self.x = self.x +250
        if name == "left":
            self.x = self.x -250
        if name == "_up_":
            self.y = self.y +250
        if name == "down":
            self.y = self.y -250
###################pong
            
            
WIDTH, HEIGHT = 840, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [6, 4]
paddle_pos = HEIGHT/2 - PADDLE_HEIGHT/2
game_over = False
class pongdia(UIdialogbase):
    def initialise(self):
        global ball_pos
        ball_pos = [WIDTH/2, HEIGHT/2]
        self.game_over = False
        self.initialised = 1
        self.score = 0
        self.add_btn("exit","exitbtn",(0.9,0.9),(0.1,0.1))
        self.add_btn("restart","re",(0.9,0.8),(0.1,0.1))
    def renderframe(self):
        global ball_pos,paddle_pos
        paddle_pos = pygame.mouse.get_pos()[1]
        #self.active = self.game_over
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
        if ball_pos[0] > 600:
            ball_vel[0] = -ball_vel[0]
            ball_pos[0] = 600
        if ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
            ball_vel[1] = -ball_vel[1]
        if ball_pos[0] < PADDLE_WIDTH and paddle_pos - BALL_RADIUS < ball_pos[1] < paddle_pos + PADDLE_HEIGHT + BALL_RADIUS:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[0] < 0:
            self.game_over = True

        self.drawsys.screen.fill((0, 0, 0))
        pygame.draw.rect(self.drawsys.screen, (255, 255, 255), (WIDTH/2 - 1, 0, 2, HEIGHT))
        pygame.draw.circle(self.drawsys.screen, (255, 255, 255), ball_pos, BALL_RADIUS)
        pygame.draw.rect(self.drawsys.screen, (255, 255, 255), (0, paddle_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        ptext.draw("score ; " + str(self.score) ,pos=(20,20),color="white" )
    def btnp(self,name):
        global ball_pos
        if name == "exitbtn":
            self.active = 0
        if name == "re":
            self.score = 0
            self.active = 1
            ball_pos = [WIDTH/2, HEIGHT/2]
            



class flappybird(UIdialogbase):


    def __init__(self):
        UIdialogbase.__init__(self)
        self.playerx = 120
        self.playery = 140
        self.oly = self.playery
        self.velocity = -10
        self.maxheight =640
        self.maxlenght = 840
        self.input = 0
        self.time = 0
        self.initialised = 1
        self.ttime =0
        self.score = 0
        self.bars = [40,20,60,50,80,60]
        self.height = 240
        self.width = 240
        self.screenb = pygame.surface.Surface((240,240))
        #self.driver = wasp.watch.display
        #self.draw = wasp.watch.drawable
    def initialise(self):
        pass
    def pipe(self,y,t):
        x = ((t +(0-self.playerx)) % self.width)
        xt = (((t+7) +(0-self.playerx)) % self.width)
        if not (x > self.width or x < 10):
                self.fill(x=x-5,y=(self.height - y),w=10,h=y,bg=(0,245,0),screen=self.screenb)
                self.fill(x=x+3,y=(self.height - y),w=2,h=y,bg=(0,252,0),screen=self.screenb)
                self.fill(x=x-5,y=(self.height - y),w=2,h=y,bg=(0,240,0),screen=self.screenb)
        if not (xt > self.width or xt < 6):
                self.fill(x=xt,y=(self.height- y),w=4,h=y,bg=(0,0,255),screen=self.screenb)
        if x > 110 and x < 125:
            if self.playery < y:
                self.playerx = 0
                self.time = 0
                self.score = 0
                self.fill(x=0,y=24,w=240,h=self.height,bg=(0,0,255),screen=self.screenb)
                self.oly = 140
                self.playery = 140
            else:
                self.score = self.score + 0.1
    def gamelogic(self):
        self.playery += self.velocity
        self.velocity = self.velocity - 1
        if self.playery < 10:
            self.playery = 10
        elif self.playery > 140:
            self.playery = 140
        if self.velocity > 20:
            self.velocity = 20
        if self.velocity < -10:
            self.velocity = -10
    def renderframe(self):
        self.gamelogic()
        self.fill(x=0,y=0,w=self.width,h=self.height,bg=(0,0,255),screen=self.screenb)
        self.ttime = (self.ttime + 1) % 20
        self.playerx = (self.playerx + 2)% self.width
        self.fill(x=110,y=(self.height - self.oly),w=10,h=10,bg=(0,0,255),screen=self.screenb)
        self.fill(x=5,y=120,w=2,h=120,bg=(0,0,255))
        self.fill(x=110,y=(self.height - self.playery),w=10,h=10,bg=(31*8,53*4,8*8),screen=self.screenb)
        self.oly = self.playery
        for i in range(0,5):
            self.pipe(self.bars[i], i * 150)
        self.drawsys.screen.blit(pygame.transform.scale(self.screenb,(840,640)),(0,0))
        self.string("(esc key to exit game and return to world) score:" +str(int(self.score)), 0, 0, width=240)
    def touch(self, event):
            if self.velocity < 0:
                self.velocity = self.velocity + 10
            else:
                self.velocity = self.velocity + 5
    def keydown(self, key):
            if self.velocity < 0:
                self.velocity = self.velocity + 10
            else:
                self.velocity = self.velocity + 5


class gameSwitcher(UIdialogbase):
    def initialise(self):
        pong = pygame.image.load("img/pong.png")
        flappy = pygame.image.load("img/flappybox.png")
        self.add_btn("Pong", "pongBtn", (0.5, 0.3), (0.1, 0.1),text1=pong,text2=pong)
        self.add_btn("Flappy Bird", "flappyBtn", (0.5, 0.6), (0.1, 0.1),text1=flappy,text2=flappy)
        self.initialised =1
    def renderframe(self):
        self.drawsys.screen.fill((0, 0, 0))
        self.string("Choose a game:", 0.5, 0.1, width=400, color="white")

    def btnp(self, name):
        if name == "pongBtn":
            self.returndialog = "CPONG"
            self.active = 0
        elif name == "flappyBtn":
            self.returndialog = "CFLAPPY"
            self.active = 0
            
class settingsdia(UIdialogbase):
    def __init__(self,settings):
        UIdialogbase.__init__(self)
        self.settings = settings
        print(settings)
        self.initialised = 0
    def initialise(self):
        self.initialised =1
        #pong = pygame.image.load("img/pong.png")
        #flappy = pygame.image.load("img/flappybox.png")
        self.add_slider("       touch controls ",(300,160),["ON","OFF"],default=(1-self.settings[0]))
        self.add_slider("water Level of detail ",(300,190),["ON","OFF"],default=(1-self.settings[1]))
        self.add_slider("    performance       ",(300,220),["ON","OFF"],default=(1-self.settings[2]))
        self.add_slider("      enable  audio   ",(300,250),["ON","OFF"],default=(1-self.settings[3]))
        self.add_slider("skip credits",(300,280),["ON","OFF"],default=(1-self.settings[4]))
        #self.add_btn("Pong", "pongBtn", (0.5, 0.3), (0.1, 0.1),text1=pong,text2=pong)
        #self.add_btn("Flappy Bird", "flappyBtn", (0.5, 0.6), (0.1, 0.1),text1=flappy,text2=flappy)

    def renderframe(self):
        self.drawsys.screen.fill((200, 180, 187))
        self.string("settings", 300, 10, width=15, color="white")
    def slider(self,name,value):
        if name == "       touch controls ":
            if value == "ON":
                self.settings[0] = 1
            else:
                self.settings[0] = 0
            #print(value)
            #print(value)
        if name == "water Level of detail ":
            if value == "ON":
                self.settings[1] = 1
            else:
                self.settings[1] = 0
        if name == "    performance       ":
            if value == "ON":
                self.settings[2] = 1
            else:
                self.settings[2] = 0
        if name == "      enable  audio   ":
            if value == "ON":
                self.settings[3] = 1
            else:
                self.settings[3] = 0
        if name == "skip credits":
            if value == "ON":
                self.settings[4] = 1
            else:
                self.settings[4] = 0
        self.val = self.settings
        

       

class vendingmachinedia(UIdialogbase):
    def __init__(self,products,coins):
        #(tile,price)
        UIdialogbase.__init__(self)
        
        self.choice = random.sample(products,3)
        self.products = self.choice
        self.coins = coins
        #text4 = pygame.image.load('img/items/shopmenubutton.png')
        #text4_s = pygame.image.load('img/items/shopmenubutton_s.png')
        #rcolor = (0,255,27,255)
        #offset = (3,3)
        self.XI = 0
        text4 = pygame.image.load('img/items/shopmenubutton.png')
        text4_s = pygame.image.load('img/items/shopmenubutton_s.png')
        rcolor = (0,255,27,255)
        offset = (3,3)
        coins = self.coins
        text1 = waterFX.overlay_green_screen(text4, self.choice[0][0].gt().gt(), green_color=rcolor, offset=offset)
        text2 = waterFX.overlay_green_screen(text4, self.choice[1][0].gt().gt(), green_color=rcolor, offset=offset)
        text3 = waterFX.overlay_green_screen(text4, self.choice[2][0].gt().gt(), green_color=rcolor, offset=offset)
        text1_s = waterFX.overlay_green_screen(text4_s, self.choice[0][0].gt().gt(), green_color=rcolor, offset=offset)
        text2_s = waterFX.overlay_green_screen(text4_s, self.choice[1][0].gt().gt(), green_color=rcolor, offset=offset)
        text3_s = waterFX.overlay_green_screen(text4_s, self.choice[2][0].gt().gt(), green_color=rcolor, offset=offset)
        self.add_btn("","1",pos=(0.05,0.1),text1=pygame.transform.scale(text1,(160,160)),text2=pygame.transform.scale(text1_s,(160,160)),enabled=(coins >= self.choice[0][1]))
        self.add_btn("","2",pos=(0.37,0.1),text1=pygame.transform.scale(text2,(160,160)),text2=pygame.transform.scale(text2_s,(160,160)),enabled=(coins >= self.choice[1][1]))
        self.add_btn("","3",pos=(0.7,0.1),text1=pygame.transform.scale(text3,(160,160)),text2=pygame.transform.scale(text3_s,(160,160)),enabled=(coins >= self.choice[2][1]))
        #self.rtdia = self
        #text1 = waterFX.overlay_green_screen(text4, self.choice[0][0].gt().gt(), green_color=rcolor, offset=offset)
        #text2 = waterFX.overlay_green_screen(text4, self.choice[1][0].gt().gt(), green_color=rcolor, offset=offset)
        #text3 = waterFX.overlay_green_screen(text4, self.choice[2][0].gt().gt(), green_color=rcolor, offset=offset)
        #text1_s = waterFX.overlay_green_screen(text4_s, self.choice[0][0].gt().gt(), green_color=rcolor, offset=offset)
        #text2_s = waterFX.overlay_green_screen(text4_s, self.choice[1][0].gt().gt(), green_color=rcolor, offset=offset)
        #text3_s = waterFX.overlay_green_screen(text4_s, self.choice[2][0].gt().gt(), green_color=rcolor, offset=offset)
        
        #self.add_btn("","1",pos=(0.05,0.1),text1=pygame.transform.scale(text1,(160,160)),text2=pygame.transform.scale(text1_s,(160,160)),enabled=(coins >= self.choice[0][1]))
        #self.add_btn("","2",pos=(0.37,0.1),text1=pygame.transform.scale(text2,(160,160)),text2=pygame.transform.scale(text2_s,(160,160)),enabled=(coins >= self.choice[1][1]))
        #self.add_btn("","3",pos=(0.7,0.1),text1=pygame.transform.scale(text3,(160,160)),text2=pygame.transform.scale(text3_s,(160,160)),enabled=(coins >= self.choice[2][1]))
    
    def initialise(self):
        self.initialised = 1
        self.add_btn("exit vending machine","exitbtn",(0,0.9),(1,0.1))
    def btnp(self, name):
        if name == "1":
            self.cplayer.inventory.rmitem("coin",self.choice[0][1])
            self.cplayer.inventory.invadds(self.choice[0][0].mp_item.name)
        if name == "2":
            self.cplayer.inventory.rmitem("coin",self.choice[1][1])
            self.cplayer.inventory.invadds(self.choice[1][0].mp_item.name)
        if name == "3":
            self.cplayer.inventory.rmitem("coin",self.choice[2][1])
            self.cplayer.inventory.invadds(self.choice[2][0].mp_item.name)
        #if name == "exitbtn":
            #self.returndialog = "thisridiculeslylongstringwillmakesureyoucanexit:D"
        self.active = 0
    def autoswitch(self,val,strt=" coin"):
        if val == 1:
            return str(strt)
        else:
            return str(strt) + "s"
    def renderframe(self):

            #coins = self.cplayer.inventory.getcount("coin")
            #self.coins = coins

            
            
        ###
        self.drawsys.screen.fill((0, 0, 0))
        self.string("you have " + str(self.coins) +" coins remaining",20,20)
        self.string(str(self.products[0][0].name) + " for "+ str(self.products[0][1])+self.autoswitch(self.products[0][1]),self.scale(0.05,0.4)[0],self.scale(0.7,0.4)[1])
        self.string(str(self.products[1][0].name) + " for "+ str(self.products[1][1])+self.autoswitch(self.products[1][1]),self.scale(0.35,0.4)[0],self.scale(0.7,0.4)[1])
        self.string(str(self.products[2][0].name) + " for "+ str(self.products[2][1])+self.autoswitch(self.products[2][1]),self.scale(0.7,0.4)[0],self.scale(0.7,0.4)[1])
        #self.active = 0
class invdia(UIdialogbase):#i have not tested this , at least it has a chance of working until tested 
    def __init__(self,x,y):
        UIdialogbase.__init__(self)
        self.cx = x
        self.cy = y
        self.FTIO = 0
    def initialise(self):
        self.active = 1
        self.initialised = 1
        self.inv = {}  # initialize inventory
        self.xi = 0  # initialize xi variable

    def renderframe(self):#####YYYYYYYYYYYYYAAAAAAAAAAAAAAAAYYYYYYYYYYYYYYY it works , i think i know how but just in case leave this alone   
        if self.FTIO == 0:
            self.FTIO == 1
            tl = self.cmap.structuremap.rmmap((self.cx,self.cy),1)
            if not tl == "none":
                if tl.price > 0:
                    self.inv = {}
                    self.inv[tl.mp_item] = 1
                    self.cmap.structuremap.smmap((self.cx,self.cy),"none")
                else:
                    self.cmap.structuremap.smmap((self.cx,self.cy),"none")
                
        self.drawsys.screen.fill((0, 0, 0))
        # render inventory using imvrender function
        xo = imxrender(self.cplayer.inventory.inv, self.inv)
        #print(xo)
        self.cplayer.inv = xo[1]
        self.inv = xo[2]
        time.sleep(0.05)
        if xo[0] ==  1:
            self.active = 0
            print(self.inv)
            if self.inv == {}:
                self.cmap.structuremap.smmap((self.cx,self.cy),"none")
            else:
                nx = next(iter(self.inv.items()))
                tlc = nx[0]
                print(tlc.blockID)
                xi = "none"
                for i in self.cmap.tiles:
                    if i.__class__.__name__ == tlc.blockID:
                        xi = i
                        print("match found ")
                self.cmap.structuremap.smmap((self.cx,self.cy),xi)
                print(str(self.cx) +"+"+str(self.cy))
                
            ##add code that replaces tile just above x/y coords
            #just do it, if it does not work ,you can fix it later


    def btnp(self, name):
        pass  # do nothing on button press

    def runUI(self):
        while self.active:
            self.renderframe()
            #self.handleinputs()
            pygame.display.flip()

    
