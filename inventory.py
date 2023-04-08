import pygame
import time
import math
import ptext
import pqGUI as agui
from pqGUI import App
from player import messages
from player import playerobj
from player import player
from pygamebutton import PygButton
import random
X = 420
Y = 320
color = (200,220,255)
wcolor = (255,200,150)
class item():
    def __init__(self,name="default",desc="description",place="no",uda=False):
        self.name = str(name)
        self.tname = tname = str(name).replace(" ","_")
        self.place = place
        self.uda = uda
        
        try:
            texture = pygame.image.load("img/items/" + tname + ".png")
        except:
            texture = pygame.image.load("img/404.png")
            print("item " + str(name) + " needs a texture at img/items" + tname + ".png please ,add one")
        self.image = pygame.transform.scale(texture, (40,40))
        ##format
        t = ""
        ct = 0
        wc =0
        for i in desc:
            t = t + i
            ct = ct + 1
            if ct == 0 and i == " ":
                break
            if i == " ":
                wc = wc + 1
            if wc>4:
                t = t + "\n"
                wc = 0
        ###end of format
        self.desc = t
    def use(self,test=0):
        if test:
            return 1
        else:
            return self
## class message in bottle ##

class messageinbottle(item):
    def use(self,test=0):
        if test:
            return 1
        else:
            return item("letter","the letter reads " + messages[random.randint(0,len(messages)-1)])

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
def computestringdiff(actuall,inputst):
    return len(list(inputst.replace(actuall,"")))

        
        
class INVAPP(App):
    def __init__(self,**options):
        super().__init__(**options)
        agui.Scene(id=0)
        self.inv = agui.ListBox([],pos=(250,0),width=170,m=18,fontsize=20,cmd="self.sse()",name="mn1")        
        App.scene = App.scenes[0]
    
    
invs = INVAPP(size=(X,Y))
surface = pygame.display.set_mode((X,Y))
exitbtn = PygButton(caption="exit inventory",rect=(250,280,170,20))
delbtn = PygButton(caption="throw away ",rect=(250,300,170,20))
intbtn = PygButton(caption=" interact  ",rect=(250,260,170,20))
class inventoryc:
    def __init__(self):
        self.inv = {}
    def test(self):
        global possible_items
        for i in possible_items:
            self.inv[possible_items[i]]= 64
    def invadds(self,ist,amount=1):
        global possible_items
        t = possible_items["coal"]
        if ist in possible_items:
            temp = inventory[ist]
            if temp in self.inv:
                self.inv[temp] =  inv[temp] + amount
                if self.inv[inv[temp]] < 0:
                    self.inv[temp] = 0
        else:
            print("there does not exist a item of name" + str(ist))
temp = inventoryc()
temp.test()
tempinventory = temp.inv 
def setinv(inventory):
    global invs
    x = invs.scenes[0].nodes[0].i
    u = []
    clist = []
    for key, value in inventory.items():
        if value > 0:
            u.append(key.name + " "+str(value))
            clist.append(key)
    u.append(" ")
    clist.append(item("infochip"," this entry is here to prevent crashing if all inventory items are deleted ",uda=True))
    invs.scenes[0].nodes[0].set_list(u)
    invs.scenes[0].nodes[0].i = x
    invs.scenes[0].nodes[0].select(x)
    invs.scenes[0].nodes[0].render()
    return clist[math.floor((invs.scenes[0].nodes[0].i% len(u)))] 

def irender(player):
    exitinv = 0
    inventory = player
    invitem = setinv(inventory)
    if  invitem.use(test=1) == 1  and  invitem in inventory and inventory[invitem]  > 0 and invitem.uda == False:
        intbtn.enabled = True
    else:
        intbtn.enabled = False
    for event in pygame.event.get():
        invs.scene.do_event(event)
        if 'click' in delbtn.handleEvent(event) :
            if invitem.uda == False :
                inventory[invitem] = 0
        if 'click' in exitbtn.handleEvent(event):
            exitinv = 1
        if 'click' in intbtn.handleEvent(event):
                try:
                    if invitem.use(test=1) == 1 and inventory[invitem] > 0 and invitem.uda == False : 
                        inventory[invitem] = inventory[invitem] - 1
                        j = invitem.use()
                        #print(j)
                        if j in inventory:
                            inventory[j]= inventory[j]+1
                        else:
                            inventory[j] = 1
                except:
                    iot = 0
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, 250, 320))
    ptext.draw( invitem.desc, (10, 70),  color="black")
    surface.blit(invitem.image,(5,5))
    invs.run()
    invs.scene.update()
    invs.scene.draw()
    exitbtn.draw(surface)
    delbtn.draw(surface)
    intbtn.draw(surface)
    pygame.display.flip()
    return [exitinv,inventory] ## 0 means not finished yet ,1 means to exit

player.inventory = inventoryc()

cplayer = player
if __name__ == '__main__':
    t = playerobj()
    t.inventory = tempinventory
    while True :
        t.inventory = irender(t)[1]
        time.sleep(0.05)