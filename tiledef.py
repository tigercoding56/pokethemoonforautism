import pygame
import dialogtree
import UIDIA
import asyncio
import random
import npcdia
import math
import copy
import npcnames as npcproperties
import UIdialogdef
import waterFX
import UIDIA
import psprite
companion = "none"
disptm = 0
printatall = 1
# xprint = print
# helpmsg = ""
# def zprint(x,**kwargs):
#     global printatall,xprint
#     if printatall == 1:
#         xprint(x,**kwargs)
# print = zprint
def IO():
    pass # to get around asyncio.stop() make it so that interact() looks at if tile has a dialog property and handles it in main event loop  (in main.py  just switch off the main function of libraries.py altogether)
class sttobj():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = {"x":x , "y": y}
    def sets(key,value):# index and value to place at index
        self.state[key] = value
    def gets(key,default): # index  , and value to return if index does not have a value
        if key in self.state:
            return self.state[key]
        else:
            return default
tile_textures = {}#optimisation to not need a rtx 4090 XYT
class ptexture(): # a texture pointer class
    def __init__(self,location,a=1,rescale=1):
        global tile_textures
        if not str(location) in tile_textures:
            #print("intitialising_ptexture")
            a = 1
            preimg = pygame.image.load(str(location)).convert_alpha()
            if rescale:
                tile_textures[str(location)] = pygame.transform.scale(preimg, (40,40))
            else:
                tile_textures[str(location)] = preimg
            del(preimg)
        self.location = str(location)
    def gt(self):
        return tile_textures[self.location]
    
class fptexture(): # a texture pointer class
    def __init__(self,image):
        global tile_textures
        imgstr = hash(pygame.image.tostring(image, 'RGBA'))
        if not str(imgstr) in tile_textures:
            #print("intitialising_ptexture")
                tile_textures[str(imgstr)] = image

        self.location = str(imgstr)
    def gt(self):
        return tile_textures[self.location]


quests = {"CHEST_INV":{},"bgtrailcolor":'black',"intro":0,"HOFF":0,"gather_members":0,"helpmessage":"interact (interact button) with the robot \n at the front door \n WASD / arrows to move \n i do not assume that you are stupid olivia \n and i know you probably do not need \n this help message \n but  some playtesters cannot understand  \n what the game wants them todo "}

def color_name_to_rgb(color_name, frametime=None):
    color_map = {
        'black': (0, 0, 0,14),
        'white': (255, 255, 255,14),
        'red': (255, 0, 0,14),
        'green': (0, 128, 0,14),
        'blue': (0, 0, 255,14),
        'purple': (128, 0, 128,14),
        'pink': (255, 192, 203,14),
        'yellow':(255,255,0,14),
        'orange':(255,165,0,14)
        ,'ethereal': (255, 192, 203,14)
        #'None':
    }

    if color_name == 'rainbow':
        if frametime is None:
            raise ValueError("Rainbow color requires a 'frametime' argument.")

        period = 100  # Adjust the period to change the speed of the rainbow cycle
        frequency = 2 * math.pi / period
        r = int(127 * math.sin(frequency * frametime + 0) + 128)
        g = int(127 * math.sin(frequency * frametime + 2 * math.pi / 3) + 128)
        b = int(127 * math.sin(frequency * frametime + 4 * math.pi / 3) + 128)
        return (r, g, b,14)

    if color_name == 'ethereal':
        if frametime is None:
            raise ValueError("Ethereal color requires a 'frametime' argument.")

        period = 250  # Adjust the period to change the speed of the ethereal color cycle
        frequency = 2 * math.pi / period
        r = int(127 * math.sin(frequency * frametime + 0) + 128)
        g = int(127 * math.sin(frequency * frametime + math.pi / 2) + 128)
        b = int(127 * math.sin(frequency * frametime + math.pi) + 128)
        return (r, g, b,14)

    return color_map.get(color_name, None)
def draw_circle(surface, color, center, radius):
    circle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(circle_surface, color[:3], (radius, radius), radius)
    alpha = color[3] if len(color) >= 4 else 255
    circle_surface.set_alpha(alpha)
    surface.blit(circle_surface, (center[0] - radius, center[1] - radius))
    return surface

class entity():
    def __init__(self,x,y):
        self.pos = [x,y]
        self.delme = 0
        self.dt = 20
        self.frametime = 0
        self.swm =0 #save  with map
        self.texture = ptexture('img/footstep.png')
    def draw(self,x,y,screen):
        global quests
        if "bgtrailcolor" in quests:
            color = list(color_name_to_rgb(quests["bgtrailcolor"],self.frametime))
        else:
            quests["bgtrailcolor"] = "black"
            color = list(color_name_to_rgb(quests["bgtrailcolor"],self.frametime))
        color[3] =  100
        self.frametime += 10
        self.frametime = self.frametime % 100
        try:
            #screen.blit(pygame.transform.scale(self.texture.gt(),(self.dt,self.dt)),(int(x-(self.dt*0.5)),int(y-int(self.dt*0.5))))
            screen = draw_circle(screen, color, (x, y), int(self.dt*0.5))
        except:
            self.delme = 1
        return screen
    def run(self,tiles,cmap):
        self.dt = self.dt - 1
        if self.dt < 2:
            self.delme = 1
        return self
    def rm(self):
        self.delme = 1
class shadowentframeent():
    def __init__(self,x,y):
        self.pos = [x,y]
        self.delme = 0
        #self.dt = 3
        self.frametime = 2
        self.swm =0 #save  with map
        self.texture = ptexture('img/footstep.png')
    def draw(self,x,y,screen):
        #print((x,y))
        screen.blit(self.texture.gt(),(int(x),int(y)))
        #self.delme = 1
        #self.delme=1
            #screen = draw_circle(screen, color, (x, y), int(self.dt*0.5))

        return screen
    def run(self,tiles,cmap):
        #if self.dt < 2:
            #self.delme = 1
        #self.dt = self.dt - 1
        return self
    def rm(self):
        self.delme = 1
def extract_sprite_from_32x_cat_spritesheet(spritesheet, orientation, frame):
    sprite_width = 32
    sprite_height = 32
    num_columns = 4
    
    row_offset = 0
    if orientation == 'left':
        row_offset = 1
    elif orientation == 'right':
        row_offset = 2
    elif orientation == 'up':
        row_offset = 3
    elif orientation == 'down':
        row_offset = 0
    elif orientation == 'standright':
        row_offset = 4
    elif orientation == 'standleft':
        row_offset = 5
        
    # Calculate the position in the spritesheet
    column = (frame ) % num_columns
    row = row_offset
    
    # Calculate the position in pixels
    x = column * sprite_width
    y = row * sprite_height
    
    # Extract the sprite from the spritesheet
    #print(pygame.Rect(x, y, sprite_width, sprite_height))
    #print((spritesheet.get_width(),spritesheet.get_height()))
    sprite = spritesheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
    
    return sprite
def determine_direction(start, end):
    start_x, start_y = start
    end_x, end_y = end
    
    if start_x < end_x:
        return 'right'
    elif start_x > end_x:
        return 'left'
    elif start_y < end_y:
        return 'down'
    elif start_y > end_y:
        return 'up'
    else:
        return 'right'  # Default direction if the coordinates are the same
def determine_dir2(start, end):
    start_x, start_y = start
    end_x, end_y = end
    
    if start_x < end_x:
        return 'standleft'
    elif start_x > end_x:
        return 'standright'
    elif start_y < end_y:
        return 'standright'
    elif start_y > end_y:
        return 'standleft'
    else:
        return 'right'  # Default direction if the coordinates are the same
class entit2y():
    def __init__(self,x,y):
        self.pos = [x,y]
        self.delme = 0
        self.dt = 10
        self.animation = 0
        self.stage = 1
        self.progress = 10
        self.previouspos = self.pos
        self.nextpos = self.pos
        self.swm =0 #save  with map
        self.texture = ptexture('img/followcat.png',rescale=0)
        self.path = []
    def draw(self,x,y,screen):
        texture =  self.texture.gt()
        if self.previouspos.__class__.__name__ == 'int' or self.nextpos.__class__.__name__ == 'int':
            return screen
        self.dt = 40
        if len(self.path) == 1:
            self.animation = (self.animation + 0.2) % 4
            texture = extract_sprite_from_32x_cat_spritesheet(texture,determine_dir2(self.previouspos,self.nextpos),int(self.animation )% 4)
        else:
            texture = extract_sprite_from_32x_cat_spritesheet(texture,determine_direction(self.previouspos,self.nextpos),int(self.progress )% 4)
        try:
            screen.blit(pygame.transform.scale(texture,(self.dt,self.dt)),(int((x+20)-(self.dt*0.5)),int((y+20)-int(self.dt*0.5))))
        except Exception as iex:
            self.delme = 1
            print(iex)
            
        return screen
    def int(self,x,y,i):
        return ((y-x)*i)+x
    def run(self,tiles,cmap):
        try:
            if self.stage > (len(self.path)-2):
                prepath = cmap.path(self.pos,cmap.playerpos)
                if not (prepath == None or prepath == []):
                    self.path = prepath
                    self.previouspos = [math.floor(xu) for xu in self.pos]
                    #if len(prepatb)
                    self.nextpos = self.path[0]
                    self.stage = 0
                    #print(prepath)
            else:
                if not self.path == []:
                    if self.progress < 10:
                        self.pos = list(self.pos)
                        self.progress = self.progress +1
                        self.pos[0] = self.int(self.previouspos[0],self.nextpos[0],self.progress*0.1)
                        self.pos[1] = self.int(self.previouspos[1],self.nextpos[1],self.progress*0.1)
                    else:
                        self.progress = 0
                        self.previouspos = self.path[self.stage]
                        self.stage = self.stage + 1
                        self.nextpos = self.path[self.stage]
                else:
                    self.stage = 2
                    
        except:
            self.pos = cmap.playerpos
            self.progress = 9999999
                
            
        #self.dt = self.dt - 1
         
        #if self.dt < 2:
            #self.delme = 1
        return self
    def rm(self):
        self.delme = 1
        

class RandomWalkEntity:
    def __init__(self, x, y):
        self.start_pos = [x, y]
        self.tout= 0
        self.pos = None
        self.itl = 0
        self.delme = 0
        self.lvp = [0,0]
        self.dt = 20
        self.swm = 0 #save with map
        self.texture = ptexture('img/cat.png')
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.walkable = True
        
    def run(self, tiles,cmap):
        if (tiles[4].__class__.__name__ == 'str' or tiles[4].walkable) and (tiles[5].__class__.__name__ == 'str' or tiles[5].walkable) :
            self.lvp = [math.floor(x)+0.5 for x in self.pos]
        else:
            self.pos = self.lvp
        #if self.itl == 0:
            #self.itl=1
            #self.pos = [round(self.pos[0])+0.5, round(self.pos[1])+0.5]
        if self.walkable:
            dx, dy = self.direction
            if self.tout > 0:
                self.tout = self.tout -1
            if self._is_on_center_of_tile() or self.itl==0:
                    self.itl == 1
                    
                    self.direction = self._get_new_direction(tiles)
                    #print(dx)
                    #print(dy)
                    new_x, new_y = self.pos[0] + dx * 0.1, self.pos[1] + dy * 0.1
                    self.pos[0], self.pos[1] = new_x, new_y
                    #print(new_x)
            new_x, new_y = self.pos[0] + dx * 0.1, self.pos[1] + dy * 0.1
            if  tiles[self._get_tile_index(new_x, new_y)].__class__.__name__ == "str" or tiles[self._get_tile_index(new_x, new_y)].walkable:
                
                #if self._is_valid_position(new_x, new_y):
                    self.pos[0], self.pos[1] = new_x, new_y
                #else:
                    #self.direction = list(self.direction)
                    #self.direction[0] = 0 - self.direction[0]
                    #self.direction[1] = 0 - self.direction[1]
                    #self.direction = self._get_new_direction(tiles)
                    #self.pos[0] = math.floor(self.pos[0])+0.5
                    #self.pos[1] = math.floor(self.pos[1])+0.5
            else:
                #if self.tout == 0:
                    #dirlist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    self.direction = list(self.direction)
                    if not self.direction[0] == 0:
                        self.direction[0] = 0 - self.direction[0]
                    if not self.direction[1] == 0:
                        self.direction[1] = 0 - self.direction[1]
                    #else:
                        #pdir = [(0)]
                        #for i in range(0,4):
                            #tiles[self._get_tile_index(pnew_x, pnew_y)].__class__.__name__ == "str" or tiles[self._get_tile_index(pnew_x, pnew_y)].walkable:
                        
                    #self.tout = 10
                
                #self.direction = tuple(x + random.uniform(-0.1, 0.1) for x in self.direction)

                #self.pos[0] = math.floor(self.pos[0])
               # self.pos[1] = math.floor(self.pos[1])
                #self.pos = self.lvp
                    #self.direction = self._get_new_direction(tiles,xt=0)

        return self
    def _get_tile_index(self, x, y):
        # Calculate the index of the tile that the entity would move into based on its position and direction of movement
        #print(self.direction)
        dx, dy = self.direction
        if dx > 0:
            return 2 if y >= self.pos[1] else 1
        elif dx < 0:
            return 0 if y >= self.pos[1] else 1
        elif dy > 0:
            return 3 if x >= self.pos[0] else 1
        else:
            return 1 if x >= self.pos[0] else 0

    def draw(self, x, y, screen):
       # try:
        screen.blit(pygame.transform.scale(self.texture.gt(), (self.dt, self.dt)), (int(x - (self.dt * 0.5)), int(y - int(self.dt * 0.5))))
        #except:
           # self.delme = 1
        return screen



    def rm(self):
        self.delme = 1

    def _is_valid_position(self, x, y, dx=0.1):
        if x % 1 > (0.5 - dx) or x % 1 < (0.5 + dx):
            if y % 1 > (0.5 - dx) or y % 1 < (0.5 + dx):
                return True
        return False

    def _get_new_direction(self, tiles,xt=0):
        possible_directions = []
        dirlist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        t = enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)])
        for i, direction in t:
            dx, dy = direction
            #if xt == 0:
            new_x, new_y = math.floor(self.pos[0]) + dx , math.floor(self.pos[1]) + dy 
            #else:
               # new_x, new_y = self.pos[0] + dx * 0.1, self.pos[1] + dy * 0.1
            #if self._is_valid_position(new_x, new_y):
            tile = tiles[i]
                #print(tile)
            tiles[self._get_tile_index(new_x, new_y)].__class__.__name__ == "str" or tiles[self._get_tile_index(new_x, new_y)].walkable
                    #print("xD")
            if direction != (0-self.direction[0], 0-self.direction[1]):
                        possible_directions.append(direction)
            else:
                tl = [0-x for x in direction ]
                ix = dirlist.index(tuple(tl))
                new_x3 = tl[0]
                new_y3 = tl[1]
                if tiles[self._get_tile_index(new_x3, new_y3)].__class__.__name__ == "str" or tiles[self._get_tile_index(new_x3, new_y3)].walkable:
                    possible_directions.append(tuple(tl))
                    possible_directions.append(tuple(tl))
                
        if not possible_directions:
            return self.direction
        return random.choice(possible_directions)

    def _is_on_center_of_tile(self):
        if self.pos[0] % 1 == 0.5 and self.pos[1] % 1 == 0.5:
            return True

        return False       
        

entities = [entity(0,0),RandomWalkEntity(0,0),entit2y(0,0),shadowentframeent(0,0)]        
tiles = []
class tile():
    def init(self):
        pass
    def updtmp(self,cmap):
        return cmap
    def initmp(self):
        pass
    def interact(self,cplayer,cmap,message="found \n nothing"):
        return [cplayer,cmap,message]#usefull for modifying the worldmap  , or teleporting the player the last argument is a message 
    
    def gtx(self,fn):
        return self.gt()
        
    def powerevent(self,cmap):
        return cmap
    def gt(self):
        return self.texture
    def callback(self,cmap=0,cplayer=0,test=0):
        if test == 1:
            return 0
        else:
            return [cmap,cplayer]
    def lgco(self,attributes,name,color,a=0): # legacy compatibility
        self.name = name
        self.rstate = [0,0,0,0]
        self.message = self.name
        self.color = color
        if len(attributes) > 3:
            if  "unpassable" in attributes[3]:
                self.walkable = 0
        self.attributes = []
        self.interactable = 0 
        self.texture = ptexture('img/' +self.name+'.png',a)
    def catchtxt(self,name):
        return ptexture('img/' +name+'.png')
    def wirephandle(self):
        pass
    def __init__(self):
        self.color = [0,0,0,0]
        self.walkable = 1
        self.rstate = [0,0,0,0]
        self.tst = [ptexture('mesecons/S0O.png'),ptexture('mesecons/S1O.png'),ptexture('mesecons/OO.png'),ptexture('mesecons/S3O.png')]
        self.mp_item = None
        self.animated = 0
        self.height = 0
        self.price = 0
        self.PBA = 0
        self.place_last =0
        self.name = '404'
        self.message = ""
        self.hidden = 0
        self.on = 0
        self.conductor = 0
        self.state = 0
        self.x = 0
        self.y = 0
        #self.texture = ptexture('img/'+str(name)+'.png')
        self.texture = ptexture('img/404.png')
        self.textures = []
        self.pos = [0,0]
        self.attributes = ["ground",0,0,[]] ## sample ["detail"[group, if not set is assumed to be ground ],1 [enemy level to spawn 1 is basic enemies , 10 is challenging enemies],10 [chance of spawning (1 in #)],['unpassable','id32'] [list of attributes that can be used elsewhere in code , unpassable means player cannot walk through,"trader" [npc to spawn]]
    def update_state(self,cmap,state,s=""):
        global rstates
        nxt = [(-1,0),(0,1),(1,0),(0,-1)]
        lt = [2,3,0,1]
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.on = state
        self.wirephandle()
        if not s=="":
            dntupd = lt[s]
        else:
            dntupd = ""
        for i in nxt:
            tilex= cmap.read(cmap.structuremap,self.x+i[0],self.y+i[1],True)
            if not tilex == "none":
                if tilex.conductor == 1:
                    if not tilex.on == state:
                        try:
                            #if not x == dntupd:
                                cmap = tilex.update_state(cmap,state)#,s=x)
                                cmap.structuremap = cmap.sett(cmap.structuremap,self.x+i[0],self.y+i[1],tilex)
                        except Exception as e:
                            print("NONCONDUCTING TILE HAS update_state function ")
                            print(e)
            
                else:
                    try:
                        tilex.rstate[lt[nxt.index(i)]] = state
                        cmap = tilex.powerevent(cmap)
                        cmap.structuremap = cmap.sett(cmap.structuremap,self.x+i[0],self.y+i[1],tilex)
                    except Exception as e:
                        print(e)
                        
        
        return cmap

#### definitions start here
rstates = {}

class lever(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'lever',(255,255,999,255))
        self.interactable = True
        self.state = 0
    def interact(self,cplayer,cmap,message="found \n nothing"):
        self.state = (self.state + 1) %2
        self.x = self.pos[0]
        self.y = self.pos[1]
        nxt = [(-1,0),(0,1),(1,0),(0,-1)]
        opnxt = [2,3,0,1]
        for x in range(0,4):
            i = nxt[x]
            tile2= cmap.read(cmap.structuremap,self.x+i[0],self.y+i[1],True)
            if not tile2 == "none":
               # print(tile2)
                if tile2.conductor == 1:
                    try:
                            cmap = tile2.update_state(cmap,self.state)
                            cmap.structuremap =cmap.sett(cmap.structuremap,self.x+i[0],self.y+i[1],tile2)
                    except Exception as e:
                        print("exception in lever class interact function")
                        print(e)
                
        return [cplayer,cmap,message]


class conductor(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",0,0,[]],'wire0',(0,0,999,255))
        self.txtoff = self.catchtxt('wire0')
        self.txton = self.catchtxt('wire1')
        self.on =0
        self.conductor = 1
        self.animated = 1

    def gt(self):
        if self.on == 1:
            return self.txton
        else:
            return self.txtoff
side1txt = []
side2txt = []
class gate(tile):
    def intr(self):
        if self.on:
            self.closed = self.closed - 0.5
        else:
            self.closed = self.closed + 0.5
        if self.closed < 0:
            self.closed = 0
        if self.closed > 7.9:
            self.closed = 7.9
    def upd(self): #gets run after init to set defaults to water
        global side1txt,side2txt
        self.lgco(["ground",0,0,[]],'wire0',(0,0,999,255))
        self.txtoff = self.catchtxt('wire0')
        self.txton = self.catchtxt('wire1')
        self.side1txt = []
        self.side2txt = []
        gatetext = ptexture('img/LaserGate1.png',rescale=0)
        for i in range(0,4):
            side1txt.append( waterFX.get_texture_slice(gatetext.gt(),0,((4-i)*40)))
            side2txt.append( waterFX.get_texture_slice(gatetext.gt(),40,(4-i)*40))
        self.on =0
        self.walkable = 0
        self.conductor = 1
        self.animated = 1
        self.closed = 8

    def gt(self):
        global side1txt,side2txt
        self.intr()
        index = max(min(int((self.closed * 2 )/4),3),0)
        if self.pos[0] % 2 == 1:
            return fptexture(side1txt[index])
        else:
            return fptexture(side2txt[index])
    def wirephandle(self):
        if self.on == 1:
            self.walkable = 1
        else:
            self.walkable = 0
# class conductor(tile):
#     def upd(self):
#         self.txtoff = self.catchtxt('wire0')
#         self.txton = self.catchtxt('wire1')
#         self.on = 0
# 
#     def update_state(self, cmap, state):
#        # if self.on != state:  # If the state is changing
#             self.on = state
#             self.texture = self.txton if self.on else self.txtoff
# 
#             nxt = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#             for dx, dy in nxt:
#                 tile = cmap.read(cmap.structuremap, self.x + dx, self.y + dy, True)
#                 if isinstance(tile, conductor):
#                         cmap = tile.update_state(cmap, state)
#                         cmap.structuremap = cmap.sett(cmap.structuremap, tile.x, tile.y, tile)
# 
#             return cmap
# 
#     def gt(self):
#         if self.on == 1:
#             return self.txton
#         else:
#             return self.txtoff




#############
watertxturessides = [ptexture('img/waterw'+str(i)+'.png') for i in range(1,5)]
class water(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",0,0,["unpassable"]],'water',(0,0,0,255))
        self.txt1 = self.catchtxt('water2')
        self.txt2 = self.catchtxt('water3')
        self.ft =0
        self.height = 0
       # self.states = [0,0,0,0]
        #self.needs_upd_after_init = 1
        #self.animated = 0
    def gt(self):
        return fptexture(self.gtx(1).gt())
    #def initmp(self,cmap):
        #self.states = [1,1,1,1]
       # nxt = [(-1,0),(0,1),(1,0),(0,-1)]
       # for i in nxt:
          #  tilex= cmap.read(cmap.heightmap,self.x+i[0],self.y+i[1],True)
          #  if not tilex == "none":
             #   if tilex.name == "water":
                  #  self.states[nxt.index(i)] = 0
                
        
        return cmap
    def gtx(self,fn):
        fn = fn % 30
        if fn < 11:
            bt =  self.texture
        elif fn < 21:
            bt= self.txt1
        else:
            bt= self.txt2
        #for i in range(0,4):
           # if self.states[i]:
              #  bt.blit(watertxturessides[i].gt(),(0,0))
        return bt #fptexture(bt)
class infpedestal(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",0,0,["unpassable"]],'pedestal',(0,0,430,255))
        self.txt1 = self.catchtxt('pedestal')
        self.orb = [self.catchtxt("orb"+str(i)) for i in range(0,4)]
        self.ft =0
        self.message = "(interact to view helpmessage)"
        self.animated = 1
        self.height = 0
        self.interactable = 1
       # self.states = [0,0,0,0]
        #self.needs_upd_after_init = 1
        #self.animated = 0
    def gt(self):
        return fptexture(self.gtx(1).gt())
    #def initmp(self,cmap):
        #self.states = [1,1,1,1]
       # nxt = [(-1,0),(0,1),(1,0),(0,-1)]
       # for i in nxt:
          #  tilex= cmap.read(cmap.heightmap,self.x+i[0],self.y+i[1],True)
          #  if not tilex == "none":
             #   if tilex.name == "water":
                  #  self.states[nxt.index(i)] = 0
                
        
        return cmap
    def gtx(self,fn):
        fn = int((fn*0.1))%4
        #print(fn)
        bt = pygame.surface.Surface((40,40)).convert_alpha()
        bt.fill([0,0,0,0])
        bt.blit(self.txt1.gt(),(0,0))
        bt.blit(self.orb[fn].gt(),(0,0))
        #for i in range(0,4):
           # if self.states[i]:
              #  bt.blit(watertxturessides[i].gt(),(0,0))
        return fptexture(bt)
    def interact(self,cplayer,cmap,message="found \n nothing"):
            global quests
            nspq = "you do not have a quest assigned by a NPC this time"
            mqh = quests["helpmessage"]
            if not npcproperties.activequest == None:
                try:
                    nspq =npcproperties.activequest.desc
                except:
                    nspq = "idk if you have a quest assigned by a NPC this time \n you may have one but the following line of code \n errored out  \n   nspq =npcproperties.activequest.desc  "
            dialogtree.cnpcdial = dialogtree.nbcdialog({"1":["which helpmessage do you want to see ?",{"the one for main storyline ":"ms","the once for the npc specific quest":"nspq","exit dialog":0}],"ms":[mqh,{"exit ":"0","back":"1"}],"nspq":[nspq,{"exit ":"0","back":"1"}]})
            
            
        ####
        
            return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]
class TESTGATE(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'grass1',(255,255,2505,255))
        self.height = 0
        self.name = "DEBUG_GATE"
        self.animated = 1
        self.ft = 1
        self.texture = ptexture('mesecons/DEBUG_GATE.png')
        self.tst = [ptexture('mesecons/S0O.png'),ptexture('mesecons/S3O.png'),ptexture('mesecons/OO.png'),ptexture('mesecons/S1O.png')]
    def gt(self):
        t = self.texture.gt()
        it = t.copy()
        for i in range(0,4):
            x = self.rstate[i]
            if x == 1:
                it.blit(self.tst[i].gt(),(0,0))
        return fptexture(it)
    def powerevent(self,cmap):
        #print(self.rstate)
        return cmap
class NOTGATE(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'grass1',(255,255,2505,255))
        self.height = 0
        self.name = "DEBUG_GATE_NOT"
        self.animated = 1
        self.ft = 1
        self.rxo = 0
        self.needs_upd_after_init = 1
        self.texture = ptexture('mesecons/jeija_gate_not.png')
        self.tst = [ptexture('mesecons/S0O.png'),ptexture('mesecons/S3O.png'),ptexture('mesecons/OO.png'),ptexture('mesecons/S1O.png')]
    def gt(self):
        t = self.texture.gt()
        it = t.copy()
        if self.rxo == 1:
            it.blit(self.tst[2].gt(),(0,0))
       # for i in range(0,4):
           #x = self.rstate[i]
           # if x == 1:
                #it.blit(self.tst[i].gt(),(0,0))
        return fptexture(it)
    def updtmp(self,cmap):
        cmap = self.powerevent(cmap)
        return cmap
    def powerevent(self,cmap):
        print(self.rstate)
        self.rxo = int(not(self.rstate[0]))
        self.x = self.pos[0]
        self.y = self.pos[1]
        i = [1,0]
        tilex= cmap.read(cmap.structuremap,self.x+i[0],self.y+i[1],True)
        if not tilex == "none":
                if tilex.conductor == 1:
                    if not tilex.on == self.rxo:
                        try:
                            #if not x == dntupd:
                                cmap = tilex.update_state(cmap,self.rxo)#,s=x)
                                cmap.structuremap = cmap.sett(cmap.structuremap,self.x+i[0],self.y+i[1],tilex)
                        except Exception as e:
                            print("NONCONDUCTING TILE HAS update_state function ")
                            print(e)

 
        return cmap
class ORGATE(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'grass1',(255,255,2505,255))
        self.height = 0
        self.name = "DEBUG_GATE_OR"
        self.animated = 1
        self.ft = 1
        self.texture = ptexture('mesecons/jeija_gate_or.png')
        self.tst = [ptexture('mesecons/S0O.png'),ptexture('mesecons/S3O.png'),ptexture('mesecons/OO.png'),ptexture('mesecons/S1O.png')]
    def gt(self):
        t = self.texture.gt()
        it = t.copy()
        for i in range(0,4):
            x = self.rstate[i]
            if x == 1:
                it.blit(self.tst[i].gt(),(0,0))
        return fptexture(it)
    def powerevent(self,cmap):
        #print(self.rstate)
        state = 0
        self.x = self.pos[0]
        self.y = self.pos[1]
        if self.rstate[1]==1 or self.rstate[3] ==1:
            state =1
        self.rstate[2] = state 
        tilex= cmap.read(cmap.structuremap,self.x+1,self.y,True)
        if not tilex == "none":
                print(tilex)
                if tilex.conductor == 1:
                    if not tilex.on == state:
                        try:
                            #if not x == dntupd:
                                cmap = tilex.update_state(cmap,state)#,s=x)
                                cmap.structuremap = cmap.sett(cmap.structuremap,self.x+1,self.y+0,tilex)
                        except Exception as e:
                            print("NONCONDUCTING TILE HAS update_state function ")
                            print(e)
            
                else:
                    try:
                        tilex.rstate[0] = state
                        cmap = tilex.powerevent(cmap)
                        cmap.structuremap = cmap.sett(cmap.structuremap,self.x+1,self.y+0,tilex)
                    except Exception as e:
                        print(e)
        return cmap

class ANDGATE(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'grass1',(255,255,2505,255))
        self.height = 0
        self.name = "DEBUG_GATE_AND"
        self.animated = 1
        self.ft = 1
        self.texture = ptexture('mesecons/jeija_gate_and.png')
        self.tst = [ptexture('mesecons/S0O.png'),ptexture('mesecons/S3O.png'),ptexture('mesecons/OO.png'),ptexture('mesecons/S1O.png')]
    def gt(self):
        t = self.texture.gt()
        it = t.copy()
        for i in range(0,4):
            x = self.rstate[i]
            if x == 1:
                it.blit(self.tst[i].gt(),(0,0))
        return fptexture(it)
    def powerevent(self,cmap):
        #print(self.rstate)
        state = 0
        self.x = self.pos[0]
        self.y = self.pos[1]
        if self.rstate[1]==1 and self.rstate[3] ==1:
            state =1
        self.rstate[2] = state 
        tilex= cmap.read(cmap.structuremap,self.x+1,self.y,True)
        if not tilex == "none":
                print(tilex)
                if tilex.conductor == 1:
                    if not tilex.on == state:
                        try:
                            #if not x == dntupd:
                                cmap = tilex.update_state(cmap,state)#,s=x)
                                cmap.structuremap = cmap.sett(cmap.structuremap,self.x+1,self.y+0,tilex)
                        except Exception as e:
                            print("NONCONDUCTING TILE HAS update_state function ")
                            print(e)
            
                else:
                    try:
                        tilex.rstate[0] = state
                        cmap = tilex.powerevent(cmap)
                        cmap.structuremap = cmap.sett(cmap.structuremap,self.x+1,self.y+0,tilex)
                    except Exception as e:
                        print(e)
        return cmap

    
class NANDGATE(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'grass1',(255,255,2505,255))
        self.height = 0
        self.name = "DEBUG_GATE_NAND"
        self.animated = 1
        self.ft = 1
        self.texture = ptexture('mesecons/jeija_gate_nand.png')
        self.tst = [ptexture('mesecons/S0O.png'),ptexture('mesecons/S3O.png'),ptexture('mesecons/OO.png'),ptexture('mesecons/S1O.png')]
    def gt(self):
        t = self.texture.gt()
        it = t.copy()
        for i in range(0,4):
            x = self.rstate[i]
            if x == 1:
                it.blit(self.tst[i].gt(),(0,0))
        return fptexture(it)
    def powerevent(self,cmap):
        #print(self.rstate)
        state = 0
        self.x = self.pos[0]
        self.y = self.pos[1]
        if not(self.rstate[1]==1 and self.rstate[3] ==1):
            state =1
        self.rstate[2] = state 
        tilex= cmap.read(cmap.structuremap,self.x+1,self.y,True)
        if not tilex == "none":
                print(tilex)
                if tilex.conductor == 1:
                    if not tilex.on == state:
                        try:
                            #if not x == dntupd:
                                cmap = tilex.update_state(cmap,state)#,s=x)
                                cmap.structuremap = cmap.sett(cmap.structuremap,self.x+1,self.y+0,tilex)
                        except Exception as e:
                            print("NONCONDUCTING TILE HAS update_state function ")
                            print(e)
            
                else:
                    try:
                        tilex.rstate[0] = state
                        cmap = tilex.powerevent(cmap)
                        cmap.structuremap = cmap.sett(cmap.structuremap,self.x+1,self.y+0,tilex)
                    except Exception as e:
                        print(e)
        return cmap      



class vegetationcover(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'grass1',(2,4,8,255))
        #self.height = 1
        #self.animated = 1
        self.UAM = 1
        self.name =  "vge" 
        #self.st = -1
       # self.needpos = 1
    #def initmp(self):
        #self.st = hash(str(self.pos)) % 23
    def gt(self):
        #if self.st == -1:
        self.st = hash(str(self.pos)) % 23
        return ptexture("img/sc_obj" + str(self.st)+".png")
class grass1(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'grass1',(255,255,255,255))
        self.height = 1
        self.reflectivity = 2
class housetile(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'place',(255,255,2585,255))
        self.height = 0
        self.name = "housetile"
        self.message = ""
        self.PBA = 1
        
class pipe1(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'pipe1',(255,25235,255,255))
        self.height = 0
        self.cost = 1
        
class pipe2(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'pipe2',(255,25235,255,255))
        self.height = 0
        self.cost = 1
class pipe3(tile):
    def upd(self): 
        self.lgco(["ground",1,20],'pipe3',(255,25235,255,255))
        self.texture = ptexture('img/pipe2')
        self.height = 0
        self.cost = 1
        
        
        
        
class town_marker(tile):  
    def upd(self):
        self.lgco(["ground",1,20],'townmarker',(25215,255,23155,255))
        self.height = 0
        self.hiddentxt = ptexture("img/townmarkerhidden.png")
    def gt(self):
        global disptm
        if disptm == 1:
            return self.texture
        else:
            return self.hiddentxt


#start of a-10 tiles
class a_10nose(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-nose',(69,69,69,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.name = "a10-nose"
        self.animated = 1
        self.texture = ptexture('img/a10-nose.png')
        self.shineimage = ptexture('img/a10-nose_normal.png')
        self.name = "a-10,126"
class a_10cabin(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin',(88,88,88,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.animated = 1
        self.name = "a-10,125"
        self.texture = ptexture('img/a10-cabin.png')
        self.shineimage = ptexture('img/a10-cabin_normal.png')
class a_10cabin2(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(98,98,98,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.animated = 1
        self.name = "a-10,123"
        self.texture = ptexture('img/a10-cabin2.png')
        self.shineimage = ptexture('img/a10-cabin2_normal.png')
class a_10tail(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(167,167,167,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.animated = 1
        self.name = "a-10,353"
        self.texture = ptexture('img/a10-tailb.png')
        self.shineimage = ptexture('img/a10-tailb_normal.png')
class a_10section(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(147,147,147,255))
        self.message = ""
        self.place_last = 1
        self.name = "a-10,23"
        self.walkable = 0
        self.animated = 1
        self.texture = ptexture('img/a10-section1.png')
        self.texture2 = ptexture('img/a10-section2.png')
        self.shineimage = ptexture('img/a10-section2_normal.png')
        
    def gt(self):
        if self.pos[0] % 2 == 1:
            return self.texture
            
        else:
            return self.texture2
class a_10wing(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,10,50,255))
        self.message = ""
        self.place_last = 1
        self.walkable = 0
        self.animated = 1
        self.name = "a-10,43"
        self.texture = ptexture('img/a10-winga.png')
        self.texture2 = ptexture('img/a10-wingb.png')
        self.shineimage = ptexture('img/a10-wingb_normal.png')
    def gt(self):
        if self.pos[1] % 2 == 1:
            return self.texture
           
        else:
            return self.texture2
class a_10wingtipa(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,50,10,255))
        self.message = ""
        self.name = "a-10,132344"
        self.place_last = 1
        self.animated = 1
        self.texture = ptexture('img/a10-wingtipa.png')
        self.shineimage = ptexture('img/a10-wingtipa_normal.png')

class a_10wingtipb(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,100,50,255))
        self.message = ""
        self.name = "a-10,353"
        self.place_last = 1
        self.animated = 1
        self.texture = ptexture('img/a10-wingtipb.png')
        self.shineimage = ptexture('img/a10-wingtipb_normal.png')

class a_10turbinea(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,20,50,255))
        self.message = ""
        self.name = "a-10,13423"
        self.place_last = 1
        self.walkable = 0
        self.animated = 1
        self.texture = ptexture('img/a10-rightturbine.png')
        self.shineimage = ptexture('img/a10-rightturbine_normal.png')

class a_10turbineb(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,50,20,255))
        self.message = ""
        self.name = "a-10,433"
        self.place_last = 1
        self.walkable = 0
        self.animated = 1
        self.texture = ptexture('img/a10-leftturbine.png')
        self.shineimage = ptexture('img/a10-leftturbine_normal.png')

class a_10taila(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,200,50,255))
        self.message = ""
        self.name = "a-10,343"
        self.place_last = 1
        self.walkable = 0
        self.animated = 1
        self.texture = ptexture('img/a-10taila.png')
        self.shineimage = ptexture('img/a-10taila_normal.png')
        
class a_10tailb(tile):
    def upd(self):
        self.lgco(["ground",1,20],'a10-cabin2',(0,20,200,255))
        self.message = ""
        self.name = "a-10,23122"
        self.place_last = 1
        self.walkable = 1
        self.animated = 1
        self.texture = ptexture('img/a10-tailc.png')
        self.shineimage = ptexture('img/a10-tailb_normal.png')





####end of a-10 tiles
#SPINKITTY 

class gemstone(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'gemstone',(77,77,157,255))
        self.message = "(interact to mine gem)"
        self.interactable = True
        self.height = 1
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("gem",1)
        return [cplayer,cmap,message]


class goldstone(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'goldore',(196,189,62,255))
        self.message = "(interact to mine gold)"
        self.interactable = True
        self.height = 1
        self.walkable = 0
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("gold",1)
        return [cplayer,cmap,message]
class silverstone(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'silverstone',(235,235,235,255))
        self.message = "(interact to mine silver)"
        self.interactable = True
        self.height = 1
        self.walkable = 0
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("silver",1)
        return [cplayer,cmap,message]
class coalore(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'coalore',(69,20,20,255))
        self.message = "(interact to mine coal)"
        self.interactable = True
        self.height = 1
        self.walkable = 0
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("coal",1)
        return [cplayer,cmap,message]

class sand_message(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'sand_message',(0,0,7,255))
        self.message = "(interact to scavenge)"
        self.interactable = True
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("message_in_bottle",1)
        self = sand()
        return [cplayer,cmap,message]



class copperore(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20],'copperore',(80,80,80,255))
        self.message = "(interact to mine copper)"
        self.interactable = True
        self.height = 1
        self.walkable = 0
    def interact(self,cplayer,cmap,message="found \n nothing"):
        cplayer.inventory = cplayer.inventory.invadds("copper",1)
        return [cplayer,cmap,message]
    
class grass2(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'grass2',(230,230,230,255))
        self.height = 2
class oliviale(tile):
    def upd(self):
        self.lgco(["ground",2,10],'o.le',(22349,30,2042,255))
        self.animated = 1
class steel(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'steel',(29,30,20,255))
        self.height = 2
        self.metalshading = 1
        self.reflectivity = 20
        self.walkable =0
        self.animated = 1
        #self.
        
class plant1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'plant1',(230,230,230,2515))
        self.height = 0
        self.price = 1
        
class table1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'table',(230,230,230,2515))
        self.height = 0
        self.price = 1
        
class table2(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'table2',(230,230,230,2155))
        self.height = 0
        self.price = 1
class table3(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'table3',(230,230,230,2155))
        self.height = 0
        self.price = 1
class drawer(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'drawer',(230,230,230,2155))
        self.height = 0
        self.price = 1
        
class chair(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",2,10],'chair',(230,230,230,1255))
        self.height = 0
        self.price = 1
###npc classes
class npc(tile):
    def lgco(self,name,questn,pos,dialog,a=0,attributes=["ground",1,20,["unpassable"]],squestn=None): # legacy compatibility
        self.name = name
        self.hidden = 0
        self.message = "(interact to speak)"
        self.color = color
        if len(attributes) > 3:
            if  "unpassable" in attributes[3]:
                self.walkable = 0
        self.attributes = attributes
        self.interactable = 1
        self.pos = pos
        self.dialog = dialog
        self.questn = questn
        self.texture = ptexture('img/' +self.name+'.png',a)
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests 
        if not self.questn in quests:
            quests[questn] = 0
        if quests[questn] == 0:
            dialogtree.cnpcdial = dialogtree.nbcdialog(self.dialog)
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not self.questn in quests:
                quests[questn] = 0
                self.hidden = False
                self.walkable = 1
            if quests[self.questn] == 0:
                if not dialogtree.cnpcdial == None:
                    if  dialogtree.cnpcdial.val == "ac":
                        quests[self.questn] = 1
                        self.hidden = True
                        self.walkable = 1
                        return [cmap,cplayer,"",tiles[1]]
            return [cmap,cplayer]
#### 
# reading through 
#r/awfulleverything
# makes me realise just how messed up things have become 
#and all i can do is sit here and complain 
#
######
class scriptkiddie1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'scriptkiddie1',(206,177,22,255),1)
        self.message = "(interact to speak)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if quests["intro"] == 0:
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.introdialog)
            quests["helpmessage"] =  "go to the center of the small village you started at \n and speak to the green robot "
        elif quests["intro"] == 1:
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.info1dialog)
            quests["helpmessage"] = "get some copper , should be near 170,42 ,\n then go back to the green robot \n in the village at the start of the game  "
        elif quests["intro"] ==2:
           t =  cplayer.inventory.invcheck("copper",2)
           if t == 1:
               dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.info2dialoga)
               quests["intro"] = 3
               quests["helpmessage"] = "go talk to the robot near 210,16"
           else:
                dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.info2dialogb)
                quests["helpmessage"] ="copper is at 170,42"
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            print(quests)
            if quests["intro"] == 0:
                if not dialogtree.cnpcdial == None:
                    if  dialogtree.cnpcdial.val == "mv":
                        quests["intro"] = 1
                        dialogtree.cnpcdial = dialogtree.ddialog()
                        cmap.structuremap.smmap(self.pos,cmap.tiles[1])
                        return [cmap,cplayer,"",tiles[1]]
            elif quests["intro"] == 1:
                if not dialogtree.cnpcdial == None:
                    if  dialogtree.cnpcdial.val == "ac":
                        quests["intro"] = 2
                        dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]

class teleporter(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'teleportationdev',(78,94,186,255),1)
        self.message = "(interact to travel)"
        self.interactable = True
        self.teleport_pos = [(412,41),(200,160),(27 ,47 ),(35 ,196 ),(218 ,36 )]
    
    def gt(self):
        global quests
        if "GTH" in quests or "TPA" in quests:
            self.hidden = 0
            self.message = "(interact to travel)"
            self.interactable = True
            self.walkable =0
        else:
            self.hidden = 1
            self.message = ""
            self.interactable = False
            self.walkable = 1
        return self.texture
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.tpdia)
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "st":
                    cplayer.pos[0] = 218 - 8
                    cplayer.pos[1] = 36 -8
                    
                if  dialogtree.cnpcdial.val == "sm":
                    cplayer.pos[0] = 35 - 8
                    cplayer.pos[1] = 196 - 8
                    
                if  dialogtree.cnpcdial.val == "md":
                    cplayer.pos[0] = 27 - 8
                    cplayer.pos[1] = 47 - 8
                if  dialogtree.cnpcdial.val == "lg":
                    cplayer.pos[0] = 199-8
                    cplayer.pos[1] = 160-8
                    
                if  dialogtree.cnpcdial.val == "or":
                    cplayer.pos[0] = 412-8
                    cplayer.pos[1] = 41-8
                    
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]

class coloriser(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'coloriser',(78,94,134886,255),1)
        self.message = "(colorise trail)"
        self.interactable = True
        self.price = 1
        #self.teleport_pos = [(464 ,127),[445,180]]

    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.trailcolordia)

        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            color = (0,0,0)
            #print()
            if  dialogtree.cnpcdial.val.__class__.__name__ == 'str':
                quests["bgtrailcolor"] = dialogtree.cnpcdial.val

            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]


class fei(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'fei2',(78,94,134886,255),1)
        self.message = "(interact to travel)"
        self.interactable = True
        self.teleport_pos = [(464 ,127),[445,180]]

    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if cplayer.pos[1] >150 :
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.FIDLdialog)
        else:
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.FRTTdialog)
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "idl":
                    if cplayer.pos[1] >150:
                        cplayer.pos[0] = 464 -8
                        cplayer.pos[1] = 127 -8
                    else:
                        cplayer.pos = [445-8,180-8]
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]


class wendy(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'wendy2',(78,94,13486,255),1)
        self.message = "(interact to travel)"
        self.interactable = True
        self.teleport_pos = [[179,234],[427 ,218 ]]

    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if cplayer.pos[0] < 300:
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.WIDLdialog)
        else:
            dialogtree.cnpcdial = dialogtree.nbcdialog(dialogtree.WRTTdialog)
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "idl":
                    if cplayer.pos[0] < 300:
                        cplayer.pos[0] = 427 -8
                        cplayer.pos[1] = 218 -8
                    else:
                        cplayer.pos = [179-8,234-8]
                #if  dialogtree.cnpcdial.val == "sm":
                    #cplayer.pos[0] = 35 - 8
                    #cplayer.pos[1] = 196 - 8
               # if  dialogtree.cnpcdial.val == "md":
                   # cplayer.pos[0] = 27 - 8
                    #cplayer.pos[1] = 47 - 8
                #if  dialogtree.cnpcdial.val == "lg":
                   # cplayer.pos[0] = 200-8
                    #cplayer.pos[1] = 160-8
                #if  dialogtree.cnpcdial.val == "or":
                   # cplayer.pos[0] = 412-8
                    #cplayer.pos[1] = 41-8
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]


####
class test(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'scriptkiddie2',(245,159,159,255),1)
        self.message = "(interact to speak )"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia())
        if not ("GTH" in quests or "TPA" in quests):
                if not "GRM" in quests:
                    dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia(npcdia.cgqd1))
                else:
                    ichk = 1
                    if cplayer.inventory.invcheck("gem",rm=1,tm=0) and cplayer.inventory.invcheck("copper",rm=1,tm=0):
                        cplayer.inventory.invcheck("gem",rm=1,tm=1)
                        cplayer.inventory.invcheck("copper",rm=1,tm=1)
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.cgqd2)
                        quests["TPA"] = 1
                    else:
                        print("#")
                        print(cplayer.inventory.inv)
                        print("#")
                        print("gem" + str(cplayer.inventory.invcheck("gem",rm=1,tm=0)) )
                        print("copper" + str(cplayer.inventory.invcheck("copper",rm=1,tm=0)) )
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.cgqd3)
                        
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if  dialogtree.cnpcdial.val == "ac1":
                quests["GRM"] = 1
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]









class questobjective(tile):
    def initmp(self):
        npcproperties.npc_pos[self.cname] = self.pos
    def ssc(self,charnum):
        charnum = charnum % len(npcproperties.npc_inf) 
        character = npcproperties.npc_inf[charnum]
        self.species = character[2]
        
        
        self.assignquest = npcproperties.genquest()
        self.about = character[1]
        self.cname = character[0]
        self.lgco(["ground",1,20,["unpassable"]],self.species,(52,96,1111,255),1)
        if not "tile_" in self.species:
            self.ex_shadow = True
            self.shadowtxt = fptexture(waterFX.add_shadow(self.texture.gt(),"reflected"))
            self.animated = 1
        else:
            if self.species in ["tile_birdfeeder","tile_mailbox"]:
                self.ex_shadow = True
                self.shadowtxt = fptexture(waterFX.add_shadow(self.texture.gt(),"reflected"))
                self.animated = 1
        self.message = "( " + self.cname + " )"
        return self
    def upd(self): #gets run after init to set defaults to water
        #self.lgco(["ground",1,20,[]],'cat',(52,96,1111,255),1)
        #self.message = "(interact to speak )"
        self.interactable = True
        self.message = "( " + self.cname + " )"
    def intx(self,cplayer,cmap):
        return [cplayer,cmap]
    def interact(self,cplayer,cmap,message="found \n nothing"):
        if not npcproperties.activequest == None :
            x = npcproperties.activequest.check(cplayer,self.cname,1)
            if not x[1] == "":
                dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[x[1],{"ok":0}]})
            else:
                 dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[self.wdia,{"ok":0}]})
            if npcproperties.activequest.done == 1:
                npcproperties.activequest = None
        else:
           dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[self.wdia,{"ok":0}]})
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        if test == 1:
            return 1
        else:
            io = 0
        return [cmap,cplayer]





human_characters = []
for key in range(0,len(npcproperties.npc_inf)):
    value = npcproperties.npc_inf[key]
    if "human" in value[2]:
        human_characters.append(key)
        
assigned_characters = []
xted = random
def assign_human_character(i):
    global assigned_characters,xted
    xted.seed(str(i))
    available_characters = [character for character in human_characters if character not in assigned_characters]

    if not available_characters:
        available_characters = human_characters
        assigned_characters.clear()

    assigned_character = xted.choice(available_characters)
    assigned_characters.append(assigned_character)

    return assigned_character

class character(tile):
    def initmp(self):
        if not npcproperties.npc_pos.__class__.__name__ == "dict":
          npcproperties.npc_pos = {}  
        npcproperties.npc_pos[self.cname] = self.pos
        if "human" in self.species:
            t = assign_human_character(self.pos)
            self.ssc(t)
    def ssc(self,charnum):
        charnum = charnum % len(npcproperties.npc_inf) 
        character = npcproperties.npc_inf[charnum]
        self.species = character[2]
        
        self.about = character[1]
        self.cname = character[0]
        self.name = character[0]
        self.istile = 0
        if "tile_" in self.species:
            self.istile = 1
        self.name = self.cname
        self.assignquest = ""
        self.lgco(["ground",1,20,["unpassable"]],self.species,(52,96,1111,255),1)
        if not "tile_" in self.species:
            self.ex_shadow = True
            try:
                if self.species == "human_m":
                    self.shadowtxt = fptexture(waterFX.add_shadow(psprite.Sprite(self.cname,"Guy").sprites[3],"reflected"))
                    
                elif self.species == "human_f":
                    self.shadowtxt = fptexture(waterFX.add_shadow(psprite.Sprite(self.cname,"Girl").sprites[3],"reflected"))
                else:
                    self.shadowtxt = fptexture(waterFX.add_shadow(self.texture.gt(),"reflected"))
            except Exception as issue:
                print(issue)
            self.animated = 1
        else:
            if self.species in ["tile_birdfeeder","tile_mailbox"]:
                self.ex_shadow = True
                self.shadowtxt = fptexture(waterFX.add_shadow(self.texture.gt(),"reflected"))
                self.animated = 1
        self.message = "( " + self.cname + " )"
        return self
    def upd(self): #gets run after init to set defaults to water
        #self.lgco(["ground",1,20,[]],'cat',(52,96,1111,255),1)
        #self.message = "(interact to speak )"
        self.interactable = True
        self.message = "( " + self.cname + " )"
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        if self.istile == 0:
            if not npcproperties.activequest == None :
                x = npcproperties.activequest.check(cplayer,self.cname)
                if not x[1] == "":
                    dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[x[1],{"exit dialog":0}]})
                else:
                     dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia(do=self.about,dialog=[" sorry it seems you already have a active quest\n (" +npcproperties.activequest.desc + ")",{"exit":0},{"cancel quest":"questrm"}],npcn=self.cname))
                if npcproperties.activequest.done == 1:
                    npcproperties.activequest = None
            else:
                self.assignquest = npcproperties.quest(npcproperties.genquest(cplayer,self.cname))
                dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia(do=self.about,dialog=["do you want to  " + self.assignquest.desc + " ?" ,{"no , thank you for the offer though":0,"yes":"questac"}],npcn=self.cname))
        else:
            if not npcproperties.activequest == None :
                x = npcproperties.activequest.check(cplayer,self.cname)
                if not x[1] == "":
                    dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[x[1],{"exit dialog":0}]})
                else:
                     dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[self.about,{"exit dialog":0}]})
                if npcproperties.activequest.done == 1:
                    npcproperties.activequest = None
            else:
                dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[self.about,{"exit dialog":0}]})





        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "questac":
                    npcproperties.activequest = self.assignquest
                if  dialogtree.cnpcdial.val == "questrm":
                    npcproperties.activequest = None
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]




class OVXcharacter(tile):
    def initmp(self):
        if not npcproperties.npc_pos.__class__.__name__ == "dict":
          npcproperties.npc_pos = {}  
        npcproperties.npc_pos[self.cname] = self.pos
    def ssc(self,charnum):
        charnum = charnum % len(npcproperties.npc_inf) 
        character = npcproperties.npc_inf[charnum]
        self.species = character[2]
        
        self.about = character[1]
        self.cname = character[0]
        self.name = character[0]
        self.istile = 0
        if "tile_" in self.species:
            self.istile = 1
        self.name = self.cname
        self.assignquest = ""
        self.lgco(["ground",1,20,["unpassable"]],self.species,(52,96,1111,255),1)
        self.message = "( " + self.cname + " )"
        return self
    def upd(self): #gets run after init to set defaults to water
        #self.lgco(["ground",1,20,[]],'cat',(52,96,1111,255),1)
        #self.message = "(interact to speak )"
        self.interactable = True
        self.message = "( " + self.cname + " )"
    def gcd(self):
        return 0#return 0 or a custom dialog
    def HGCD(self):
        return 0
    def interact(self,cplayer,cmap,message="found \n nothing"):
        if self.istile == 0:
            if self.gcd() == 0 :
                if not npcproperties.activequest == None :
                    x = npcproperties.activequest.check(cplayer,self.cname)
                    if not x[1] == "":
                        dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[x[1],{"exit dialog":0}]})
                    else:
                         dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia(do=self.about,dialog=[" sorry it seems you already have a active quest\n (" +npcproperties.activequest.desc + ")",{"exit":0},{"cancel quest":"questrm"}],npcn=self.cname))
                    if npcproperties.activequest.done == 1:
                        npcproperties.activequest = None
                else:
                    self.assignquest = npcproperties.quest(npcproperties.genquest(cplayer,self.cname))
                    dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia(do=self.about,dialog=["do you want to  " + self.assignquest.desc + " ?" ,{"no , thank you for the offer though":0,"yes":"questac"}],npcn=self.cname))
            else:
                dialogtree.cnpcdial = self.gcd()
                self.HGCD()
        else:
            if not npcproperties.activequest == None :
                x = npcproperties.activequest.check(cplayer,self.cname)
                if not x[1] == "":
                    dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[x[1],{"exit dialog":0}]})
                else:
                     dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[self.about,{"exit dialog":0}]})
                if npcproperties.activequest.done == 1:
                    npcproperties.activequest = None
            else:
                dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[self.about,{"exit dialog":0}]})





        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "questac":
                    npcproperties.activequest = self.assignquest
                if  dialogtree.cnpcdial.val == "questrm":
                    npcproperties.activequest = None
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]



















class frnm(tile):
    def initmp(self):
        if not npcproperties.npc_pos.__class__.__name__ == "dict":
          npcproperties.npc_pos = {}  
        npcproperties.npc_pos[self.cname] = self.pos
    def ssc(self,charnum):
        charnum = charnum % len(npcproperties.npc_inf) 
        character = npcproperties.npc_inf[charnum]
        self.species = character[2]
        
        self.about = character[1][0]
        self.about2 = character[1][1]
        self.cname = character[0]
        self.name = character[0]
        self.istile = 0
        if "tile_" in self.species:
            self.istile = 1
        self.name = self.cname
        self.assignquest = ""
        self.lgco(["ground",1,20,["unpassable"]],self.species,(52,96,1111,255),1)
        self.message = "( " + self.cname + " )"
        return self
    def upd(self): #gets run after init to set defaults to water
        #self.lgco(["ground",1,20,[]],'cat',(52,96,1111,255),1)
        #self.message = "(interact to speak )"
        self.interactable = True
        self.message = "( " + self.cname + " )"
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        x = 1
        if not self.cname in quests:
            if "hx1" in quests:
                if quests["hx1"] < 4:
                    quests[self.cname] = 1
                    quests["hx1"] = quests["hx1"] + 1
                    dialogtree.cnpcdial = dialogtree.nbcdialog({"1":["you tell " + self.cname + " the news of \n the fire nation reassembling  \n  ",{"exit dialog":0}]})
                    return [cplayer,cmap,message]
        if self.cname in quests:
            about = self.about2
        else:
            about = self.about
        if self.istile == 0:
            if not npcproperties.activequest == None :
                x = npcproperties.activequest.check(cplayer,self.cname)
                if not x[1] == "":
                    dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[x[1],{"exit dialog":0}]})
                else:
                     dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia(do=about,dialog=[" sorry it seems you already have a active quest\n (" +npcproperties.activequest.desc + ")",{"exit":0},{"cancel quest":"questrm"}],npcn=self.cname))
                if npcproperties.activequest.done == 1:
                    npcproperties.activequest = None
            else:
                self.assignquest = npcproperties.quest(npcproperties.genquest(cplayer,self.cname))
                dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gtqdia(do=about,dialog=["do you want to  " + self.assignquest.desc + " ?" ,{"no , thank you for the offer though":0,"yes":"questac"}],npcn=self.cname))
        else:
            if not npcproperties.activequest == None :
                x = npcproperties.activequest.check(cplayer,self.cname)
                if not x[1] == "":
                    dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[x[1],{"exit dialog":0}]})
                else:
                     dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[about,{"exit dialog":0}]})
                if npcproperties.activequest.done == 1:
                    npcproperties.activequest = None
            else:
                dialogtree.cnpcdial = dialogtree.nbcdialog({"1":[about,{"exit dialog":0}]})





        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "questac":
                    npcproperties.activequest = self.assignquest
                if  dialogtree.cnpcdial.val == "questrm":
                    npcproperties.activequest = None
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]

class hacker(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'hacker',(52,96,157,255),1)
        self.message = "(interact to speak )"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if "end_game" in quests:
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia4)
            return [cplayer,cmap,message]
            
        
        if not "hx1" in quests:
            
            if not "hob" in quests:
                quests["hx1"] = 0
                dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia)
            else:
                dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia_a)
        else:
            if quests["hx1"] < 4:
                dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia2s)
            else:
                if not "hx2" in quests:
                    dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia3)
                    quests["hx2"] = 1
                else:
                    dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia4)
            
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not "hx1" in quests:
                if "hob" in quests:
                    if dialogtree.cnpcdial.val == "gt":
                        quests["hx1"] = 0
                    else:
                        quests["end_game"] = 1
                    
                
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]

class terminal1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'terminal',(245,34,34,255),1)
        self.message = "(interact to open terminal)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.tdia)
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "ac":
                    cplayer.inventory = cplayer.inventory.invadds("infochip",1)
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]





class radio1(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'radio',(111,226,147,255),1)
        self.message = "(interact to use the radio)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if ( not "getradio1" in quests) or "radion" in quests: 
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.urdia)
        elif not "rbf2" in quests:
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.rdia)
            quests["reportbackrd"] = 1
            
            quests["radiodone"] = 1
            quests["radion"] = 1
            quests["ART"] = 1
            quests["helpmessage"] = "back to robot"
        elif quests["rbf2"] == 1:
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.hackerdia2)
            quests["rbf2"] = 2
            quests["GTH"] = 1
            quests["ART"] = 1
            quests["helpmessage"] = "nearest city --> white \n teleporter machine --> oil rig \n speak to person on it"
        else:
            dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.urdia)
            
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "ac":
                    quests["reportbackrd"] = 1
                    quests["radiodone"] = 1
            dialogtree.cnpcdial = dialogtree.ddialog()
            return [cmap,cplayer]

class milvet(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'milvet',(216,53,207,255),1)
        self.message = "(interact to speak)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        if quests["intro"] > 2:
            if not "seldone" in quests:
                #if ( not "getradio1" in quests)  : 
                    dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia1)
                    quests["helpmessage"] = "go to either radio near plane wreck (129,50) , or \n terminal in large village (188,154) \n depending on your choice"
                    
            else:
                if "getradio1" in quests:
                    if "radion" in quests:
                        del(quests["radion"])
                    if not "reportbackrd" in quests:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia_un_a)
                        quests["helpmessage"] = "back to radio(129,50) "
                    elif not "rbf2" in quests:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia_f)
                        quests["helpmessage"] = "back to radio(129,50) "
                    elif quests["rbf2"] ==1:    
                        dialogtree.cnpcdial = dialogtree.nbcdialog({"1":["just tell the hacker that all the robots \n agree to join him \n over the radio",{"ok":0,"i'll think about it ":0}]})
                        quests["helpmessage"] = "back to radio(129,50) "
                    else:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gnpcdia())
                elif "hob" in quests :
                    if cplayer.inventory.invcheck("infochip",1) and quests["hob"] == 1:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia_fh)
                        quests["hob"] = 2
                        quests["ART"] = 1
                        quests["helpmessage"] = "take teleporter to oil-rig "
                        quests["GTH"] = 1
                    elif quests["hob"] ==1:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.milvetdia_un_b)
                        
                    else:
                        dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.gnpcdia())
                    
                        
                    
                    
                    
        else:
                dialogtree.cnpcdial = dialogtree.nbcdialog(npcdia.confuseddia)
                
        ####
        
        return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "hob":
                    quests["getinfo"] = 1
                    quests["seldone"] = 1
                    quests["hob"] = 1
                elif dialogtree.cnpcdial.val == "MPU":
                    quests["getradio1"] =1
                    quests["seldone"] = 1
                elif dialogtree.cnpcdial.val == "reportback":
                    quests["rbf2"] = 1
        dialogtree.cnpcdial = dialogtree.ddialog()
        return [cmap,cplayer]
                    #cmap.setmap(self.pos[0] ,self.pos[1],tiles[1])
            
    
    
    
    
    
    
    
    
####npc classes
class grass3(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",3,5],'grass3',(204,204,204,255))
        self.height = 3
        
class grass4(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",4,3],'grass4',(179,179,179,255))
        self.height = 4
        
class wheat(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",4,3],'wheat',(1709,1079,1709,2505))
        self.height = 0
        self.wavetxt = ptexture('img/plantwave.png')
        self.animated = 1

class ice(tile):
    def upd(self):
        self.lgco(['ground', 4, 3, ['unpassable']],"ice",(153, 153, 153, 255))
        self.height = 1
        #self.reflectivity = 50
class iceblock(tile):
    def upd(self):
        self.lgco(['ground', 4, 3],"iceblock",(33, 233, 222, 255))
        self.height = 0
        self.reflectivity = 25
        #self.animated = 1
class sand(tile):
    def upd(self):
        self.lgco(['ground', 2, 15],"sand",(128, 128, 128, 255))
        self.interactable = 0
        self.height = 1
class steppingstones(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"steppingstones",(10, 10, 10, 255),1)
####oil rig tiles
        
class oilrigplatform(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"metalgrate",(138, 14, 161, 255),1)
        self.message =""
        
class oilrigplatformwood(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"woodplatform",(79, 14, 161, 255),1)
        self.message =""
class oilrigplatformsupport1(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"oilplatformsupport1",(138, 54, 161, 255),1)
        self.message =""
        self.walkable = 0
class oilrigplatformsupport2(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"oilplatformsupport2",(18, 54, 161, 255),1)
        self.message =""
        self.walkable = 0
class oilrigpillar(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"pillar",(138, 54, 11, 255),1)
        self.message =""
        self.walkable = 0
class oilrigdrill1(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"oildrill1",(180, 54, 11, 255),1)
        self.message =""
        self.walkable = 0
class oilrigdrill2(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"oildrill2",(180, 154, 11, 255),1)
        self.message =""
        self.walkable = 0
class oilrigdrill3(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"oildrill4",(10, 154, 11, 255),1)
        self.message =""
        self.walkable = 0
class oilrigdrill4(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"oildrill5",(10, 154, 110, 255),1)
        self.message =""
        self.walkable = 0
        self.price = 1
        
        
##end of oil rig tiles
class path(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"path",(0, 255, 255, 255))
        self.wcost = 0
class cobblestone(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"cobblestone",(0, 20, 20, 255))
        self.height = 2
class cobblestone(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"cobblestone",(20, 20, 20, 255))
        self.height = 2
class wood(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"wood",(255, 0, 161, 255))
        self.height = 1
class woodh(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"woodh",(255, 0, 0, 255))
        self.height = 1
        self.price = 3
class carpet(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"carpet",(0, 0, 255, 255))
class tree(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"tree",(0, 96, 121, 255))
        self.height = 1
        self.price = 2
class vendingmachine(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, ['unpassable']],"vendingmachine",(0, 96, 1281, 32255))
class chest(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, []],"chest",(0, 96, 121, 32255))
        self.interactable = 1
        self.message = "(interact with chest)"
        self.price = 1
        self.inventory = {}
    def interact(self,cplayer,cmap,message="found \n nothing"):
        global quests
        #gameSwitcher()
        self.inventory = copy.deepcopy(quests['CHEST_INV'])
            #self.inventory = {}
        dialogtree.cnpcdial = UIdialogdef.inv2dia(self.inventory)
        #return [,cmap,message]
        return []
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        self.inventory = dialogtree.cnpcdial.inv
        quests["CHEST_INV"] = self.inventory
        #return [cplayer,cmap]
        return []
class console(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, []],"console",(0, 96, 121, 32255))
        self.interactable = 1
        self.price = 1
    def interact(self,cplayer,cmap,message="found \n nothing"):
        dialogtree.cnpcdial = UIdialogdef.gameSwitcher()
        #return [,cmap,message]
        return []
    def callback(self,cmap=0,cplayer=0,test=0):
        #dialogtree.cnpcdial =  dialogtree.ddialog()
        #return [cplayer,cmap]
        return []
class flightsim(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, []],"flightsim",(0, 96, 121, 32255))
        self.interactable = 1
        self.price = 1
    def interact(self,cplayer,cmap,message="found \n nothing"):
        dialogtree.cnpcdial = UIDIA.flightsim()
        #return [,cmap,message]
        return []
    def callback(self,cmap=0,cplayer=0,test=0):
        #dialogtree.cnpcdial =  dialogtree.ddialog()
        #return [cplayer,cmap]
        return []
class telescope(tile):
    def upd(self):
        self.lgco(['ground', 0, 0, []],"telescope",(0, 96, 121, 32255))
        self.interactable = 1
        self.price = 1
    def interact(self,cplayer,cmap,message="found \n nothing"):
        dialogtree.cnpcdial = UIdialogdef.spaceobserverdia()
        #return [,cmap,message]
        return []
    def callback(self,cmap=0,cplayer=0,test=0):
        #dialogtree.cnpcdial =  dialogtree.ddialog()
        #return [cplayer,cmap]
        return []
class safetile(tile):
    def upd(self):
        self.lgco(['ground', 0, 0],"grass1",(0, 255, 0, 255))
        
class buyhouse(tile):
    def upd(self): #gets run after init to set defaults to water
        self.lgco(["ground",1,20,["unpassable"]],'bhouse',(111,226,147,2585),1)
        self.message = "(interact to inspect house sale)"
        self.interactable = True
    
    def interact(self,cplayer,cmap,message="found \n nothing"):
            self.price = 20
            if cplayer.inventory.getcount("coin") >=  self.price:
                dialogtree.cnpcdial = dialogtree.nbcdialog({"1":["you have enough coins to buy this house ,\n do you want to buy this house for "+str(self.price) + " coins ?",{"yes":"bh","no":0}]})
            else:
                dialogtree.cnpcdial = dialogtree.nbcdialog({"1":["you don't have  enough coins to buy this house ,\n this house costs  "+str(self.price) + " coins to unlock ",{"exit dialog":0}]})
            
        ####
        
            return [cplayer,cmap,message]
    def callback(self,cmap=0,cplayer=0,test=0):
        global quests
        if test == 1:
            return 1
        else:
            if not dialogtree.cnpcdial == None:
                if  dialogtree.cnpcdial.val == "bh":
                    cplayer.inventory.rmitem("coin",self.price)
                    #cmap.structuremap.smmap(self.pos,cmap.tiles[1])
                    return [cmap,cplayer,"",carpet()]
                    
            dialogtree.cnpcdial = dialogtree.ddialog()
            
            return [cmap,cplayer]

xtiles = [water(),safetile(),test(),tree(),woodh(),carpet(),wood(),cobblestone(),path(),steppingstones(),sand(),iceblock(),ice(),grass4(),grass3(),grass2(),grass1(),gemstone(),goldstone(),silverstone(),coalore(),copperore(),scriptkiddie1(),a_10cabin(),a_10cabin2(),a_10nose(),a_10section(),a_10tail(),a_10wing(),a_10wingtipa(),a_10wingtipb(),a_10taila(),a_10tailb(),a_10turbinea(),a_10turbineb(),terminal1(),radio1(),milvet(),oilrigdrill1(),oilrigdrill2(),oilrigdrill3(),oilrigdrill4(),oilrigpillar(),oilrigplatform(),oilrigplatformsupport1(),oilrigplatformsupport2(),teleporter(),oilrigplatformwood(),hacker(),sand_message(),wheat(),town_marker()]
tiles = []
for i in range(0,len(npcproperties.npc_inf)):
    try:
        if not "tile" in  npcproperties.npc_inf[i][2]:
            if npcproperties.npc_inf[i][1].__class__.__name__ =='list':
                xtiles.append(frnm().ssc(i))
                print(npc_inf[i][1])
            else:
                xtiles.append(character().ssc(i))
    except Exception as EX:
        print(npcproperties.npc_inf[i][0])
        print(EX)
xtiles = xtiles + [housetile(),wendy(),fei(),chair(),vegetationcover(),steel(),oliviale(),coloriser(),infpedestal(),table1(),chest(),table2(),flightsim(),table3(),plant1(),console(),vendingmachine(),drawer(),buyhouse(),telescope(),lever(),conductor(),NOTGATE(),ORGATE(),ANDGATE(),NANDGATE(),TESTGATE(),gate()]
testlist = []
for i in range(0,len(npcproperties.npc_inf)):
        if  "tile" in  npcproperties.npc_inf[i][2]:
            tne = character()
            tne = copy.deepcopy(tne)
            xtiles.append(tne.ssc(i))
            print(tne.ssc(i).cname)


for itile in xtiles:
    itile.upd()
    if itile.price > 0:
        #testlist.append((itile))
        it = dialogtree.inv_handle.item("tile_" + str(itile.name),"this item allows you to costumise any \n applicable tiles with \n a"+str(itile.name),ptextpath=itile.gt().location,blockid=itile.__class__.__name__)
        dialogtree.inv_handle.possible_items["tile_"+str(itile.name)] = it
        #print("tile_"+str(itile.name))
        itile.mp_item = it
        testlist.append((itile,itile.price))
    tiles.append(itile) 