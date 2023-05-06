import pygame
import time
import math
import ptext
#import pqGUI as agui
#from pqGUI import App
from player import messages
from player import playerobj
from player import player
from pygamebutton import PygButton
from listbox import ListBox
import random
X = 840
Y = 640
color = (200,220,255)
wcolor = (255,200,150)
item_textures = {}#optimisation to not need a rtx 4090 XYT
class ptexture(): # a texture pointer class
    def __init__(self,location,a=1,rescale=1):
        global item_textures
        if not str(location) in item_textures:
            a = 1
            preimg = pygame.image.load(str(location)).convert_alpha()
            if rescale:
                item_textures[str(location)] = pygame.transform.scale(preimg, (80,80))
            else:
                item_textures[str(location)] = preimg
            del(preimg)
        self.location = str(location)
    def gt(self):
        return item_textures[self.location]
def scale(x,y,x1,y1):
    return (x*2,y*2,x1*2,y1*2)
class item():
    def __init__(self,name="default",desc="description",place="no",uda=False):
        self.name = str(name)
        self.tname = tname = str(name).replace(" ","_")
        self.place = place
        self.uda = uda
        self.hash = hash(str(name) + str(desc))
        
        try:
            texture = ptexture("img/items/" + tname + ".png")
        except:
            texture = ptexture("img/404.png")
            print("item " + str(name) + " needs a texture at img/items" + tname + ".png please ,add one")
        self.image = texture
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
"message_in_bottle":messageinbottle("message in bottle","interact to take out message "),
"infochip":item("infochip"," this infochip contains a large amount of data"),


}
def computestringdiff(actuall,inputst):
    return len(list(inputst.replace(actuall,"")))

        

    

list_box = ListBox(500, 0, 340, 840, ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6'])
surface = pygame.display.set_mode((X,Y))
exitbtn = PygButton(caption="exit inventory",rect=scale(250,280,170,20))
delbtn = PygButton(caption="throw away ",rect=scale(250,300,170,20))
intbtn = PygButton(caption=" interact  ",rect=scale(250,260,170,20))
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
            temp = possible_items[ist]
            if temp in self.inv:
                self.inv[temp] =  self.inv[temp] + amount
            else:
                self.inv[temp] = amount
            if self.inv[temp] < 0:
                    self.inv[temp] = 0
        else:
            print("there does not exist a item of name" + str(ist))
        return self
    def hashin(self,itemhash):
        for i in self.inv:
                if  hasattr(i, 'hash'):
                    if i.hash == itemhash:
                        return 1
                else:
                    i.hash = hash(str(i.name) + str(i.desc))
                    if i.hash == itemhash:
                        return 1
                    
        return 0
    def convhashintoitem(self,itemhash,it):
        for i in self.inv:
            if i.hash == itemhash:
                return i
        else:
            return it
    def invcheck(self,ist,rm=0,tm=1):#rm removes item # if greater than 0
        global possible_items
       # t = possible_items["coal"]
        if ist in possible_items:
            temp = possible_items[ist]
            if self.hashin(temp.hash) :
                temp = self.convhashintoitem(temp.hash,temp)
                if self.inv[temp] > rm:
                    if tm ==1:
                        self.inv[temp] =  self.inv[temp] - rm
                    return 1
                elif self.inv[temp] == rm:
                    if tm ==1:
                        del(self.inv[temp])
                    return 1
        return 0
                    
temp = inventoryc()
temp.test()
tempinventory = temp.inv 
def setinv(inventory):
    global list_box,surface
    u = []
    clist = []
    for key, value in inventory.items():
        if value > 0:
            u.append(key.name + " "+str(value))
            clist.append(key)
    list_box.setl(u)
    list_box.draw(surface)
    if list_box.selected_item ==None:
        return  item("infochip"," this entry is here to prevent crashing if all inventory items are deleted ",uda=True)
    return clist[math.floor((list_box.selected_item % len(u)))] 

def irender(player):
    exitinv = 0
    inventory = player
    invitem = setinv(inventory)
    if  invitem.use(test=1) == 1  and  invitem in inventory and inventory[invitem]  > 0 and invitem.uda == False:
        intbtn.enabled = True
    else:
        intbtn.enabled = False
    for event in pygame.event.get():
        list_box.handle_event(event)
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
    
    pygame.draw.rect(surface, color, pygame.Rect(scale(0, 0, 250, 320)))
    ptext.draw( invitem.desc, (20, 140),  color="black")
    surface.blit(invitem.image.gt(),(5,5))
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