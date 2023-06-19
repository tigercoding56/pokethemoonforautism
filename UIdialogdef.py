from planets import drawplanetsurface
from dialogtree import UIdialogbase
from dialogtree import pygame
import time
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
            
