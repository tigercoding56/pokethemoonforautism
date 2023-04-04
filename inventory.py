import pygame
import time
import math
import ptext
import pqGUI as agui
from pqGUI import App
from player import messages
from player import player

import random
X = 420
Y = 320
color = (200,220,255)
class item():
    def __init__(self,name="default",desc="description",place="no"):
        self.name = str(name)
        self.tname = tname = str(name).replace(" ","_")
        self.place = place
        
        try:
            texture = pygame.image.load("img/items/" + tname + ".png")
        except:
            texture = pygame.image.load("img/404.png")
            print("item " + str(name) + " needs a texture at img/items" + tname + ".png please ,add one")
        self.image = pygame.transform.scale(texture, (40,40))
        
        print(self.tname)
        ##format
        t = ""
        wc =0
        for i in desc:
            t = t + i
            if i == " ":
                wc = wc + 1
            if wc>4:
                t = t + "\n"
                wc = 0
        ###end of format
        self.desc = t
    def use(self):
        return self
## class message in bottle ##

class messageinbottle(item):
    def use(self):
        return item("letter","the letter reads " + messages[random.randint(0,len(messages)-1)])
item("message in bottle","interact with this to take the letter out of the bottle ")
possible_items = {
"coal":item("coal"," coal ore  "),
"copper":item("copper"," copper ore  "),
"gold":item("gold"," gold ore   "),
"silver":item("silver"," silver ore  "),
"gem":item("gem"," a shiny crystal . probably broke of off a gemstone"),
"capture_device":item("capture device","a device  which captures   one creature .single use item "),
"info":item("infochip"," click on any inventory item to view it and press the exit button to exit the inventory . press the interact button to search the highligthed tile"),
"wood":item("wood","a pile of wood, perfect for creating things "),
"iloveyou":item("easteregg","a reminder of why i bothered making this game , if you ever find it that is "),
"flower":item("flower","a flower  with quite sturdy roots , could it be used as rope"),
"win":item("mysteriousdevice","this device should  tame all animals on this island . just place it down","md"),    
"message_in_bottle":messageinbottle("message in bottle","interact to take out message ")

}

class INVAPP(App):
    def __init__(self,**options):
        super().__init__(**options)
        agui.Scene(id=0)
        self.inv = agui.ListBox([],pos=(250,0),width=170,fontsize=20,cmd="self.sse()",name="mn1")        
        App.scene = App.scenes[0]
t = INVAPP(size=(X,Y))
surface = pygame.display.set_mode((X,Y))

class inventoryc:
    def __init__(self):
        self.inv = {}
    def test(self):
        global possible_items
        for i in possible_items:
            self.inv[possible_items[i]]= 64
            print(self.inv)
temp = inventoryc()
temp.test()
inventory = temp.inv 
def setinv():
    global inventory,t
    u = []
    clist = []
    x = t.scenes[0].nodes[0].i
    for key, value in inventory.items():
        if value > 0:
            u.append(key.name + " "+str(value))
            clist.append(key)
    t.scenes[0].nodes[0].set_list(u)
    t.scenes[0].nodes[0].i = x
    t.scenes[0].nodes[0].select(x)
    return clist[math.floor((t.scenes[0].nodes[0].i% len(u)))] 
    
    
while True:
    for event in pygame.event.get():
        t.scene.do_event(event)
        if event.type == pygame.QUIT:
            pygame.quit()
    invitem = setinv()
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, 250, 320))
    ptext.draw( invitem.desc, (10, 70),  color="black")
    surface.blit(invitem.image,(5,5))
    t.run()
    t.scene.update()
    t.scene.draw()
    pygame.display.flip()
    time.sleep(0.05)
  