import pygame as pg
import pygame
import random
import pygame.gfxdraw
import time
from  ptexture import ptexture
import math
import numpy
tile_textures = {}#optimisation to not need a rtx  XYT
particles = []
pp = [0,0,0]


def find_peaks_in_range(start, end, pp):
    # Compute the values of i where the peaks repeat
    k_start = int(math.floor((start + pp[1])/69 - math.asin(1)/math.pi))
    k_end = int(math.ceil((end + pp[1])/120 - math.asin(1)/math.pi))
    ks = range(k_start, k_end+685)

    # Compute the values of i where the peaks occur
    peak_locations = []
    for k in ks:
        i = 400 * (math.asin(1)/math.pi + k) - pp[1]
        if i >= start and i <= end:
            peak_locations.append(i)
    return peak_locations
class particle():
    def __init__(self,x,y,velx,vely):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.lifetime = 50
def drawcloud(x,y,z,surface):
    z = min(max(z,0),1)
    #print(z)
    cloud = ptexture('img/cloud.png').gt()
    #pygame.gfxdraw.filled_circle(surface,int(x),int(y),int(z*30),(250,250,250))
    surface.blit(pygame.transform.scale_by(cloud,z),(int(x)-(cloud.get_height()/2),int(y)-(cloud.get_width()/2)))
def clears(surface):
    global pp
    for i in range(0,640):
        t = max(min(int(math.sin((i+pp[1])/400)*255),255),40)
        pygame.gfxdraw.hline(surface, 0, 840, i, (40,40,(t/255)*100+150))
    for xt in find_peaks_in_range(-300,1000,pp):
        for i in range(1,20):
            
            ikey = hash(str(i))%3000
            #print()
            z = int(((pp[2]+ikey)%300))/300
            x = (int((pp[0]+(i*45))%900)-25)
            drawcloud(x,int(xt)+(z*50),z,surface)
    #print(pp[0])
def updpt():
    global particles
    for i in range(0,len(particles)):
        try:
            if particles[i].lifetime < 1:
                if len(particles) <2:
                    particles = []
                else:
                    del(particles[i])
                
                
            else:
                particles[i].lifetime += -1
                particles[i].x += particles[i].velx
                particles[i].y += particles[i].vely
        except:
            particles = []
def drawpt(surface):
    global particles
    for i in particles:
        pygame.draw.line(surface, (169,54,45), (i.x,i.y), (i.x + i.velx,i.y+i.vely),2)
        
class ptexture(): # a texture pointer class
    def __init__(self,location,a=1,rescale=0):
        global tile_textures
        if not str(location) in tile_textures:
            a = 1
            preimg = pygame.image.load(str(location)).convert_alpha()
            if rescale:
                tile_textures[str(location)] = pygame.transform.scale(preimg,(40,40))
            else:
                tile_textures[str(location)] = preimg
            del(preimg)
        self.location = str(location)
    def gt(self):
        return tile_textures[self.location]
# Initialize Pygame
pg.init()
def c3t2(c):
    return (c[0]*(1+(0.02*c[2])))+420,320+(c[1]*(1+(0.02*c[2])))
# Set up the display window
window = pg.display.set_mode((840, 640))

# Load the font
font = pg.font.Font(None, 24)
imagelist = []
for i in range(1,5):
    imagelist.append(ptexture('img/a10l'+str(i)+'.png'))
    imagelist.append(ptexture('img/a10l'+str(i)+'.png'))
    imagelist.append(ptexture('img/a10l'+str(i)+'.png'))
    imagelist.append(ptexture('img/a10l'+str(i)+'.png'))

# Define colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (56,76,255)
def constrain(val, min_val, max_val):
    if abs(val) < 1:
        if random.randint(1,2) == 1:
            val = 1
        else:
            val = -1
        
    return min(max_val, max(min_val, val))
# Create an empty queue for events

x =0
y = 0

# Main game loop
running = True
def drawc(surface,x,y,r):
    global window
    surface = pygame.transform.rotate(surface.gt(),r)##0--points up --90 to the right and so on
    window.blit(surface, (x - surface.get_width() // 2, y - surface.get_height() // 2))
def run():
    global x,y,BLUE,window,imagelist,running,particles,pp
    updpt()
    pp= list(numpy.add(pp, (int(((50-x)/10))*0.1, 1-(((25-y)*0.02)),1)))
    #print(pp[2])
    # Handle event queue
    for event in pg.event.get():
        if event == pg.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pg.K_LEFT]:
        if x > -50:
            x -= 10
            #time.sleep(0.1)
    if  keys[pg.K_RIGHT]:
        if x < 50:
            x += 10
            #time.sleep(0.1)
    if  keys[pg.K_UP]:
        if y > -50:
            y -= 10
            #time.sleep(0.1)
    if  keys[pg.K_DOWN]:
        
        if y < 50:
            y += 10
            #time.sleep(0.1)
    if keys[pg.K_SPACE] :
        pos = pygame.mouse.get_pos()
        #time.sleep(0.01)
        pos = list(pos)
        pos[0] = pos[0] - 420
        pos[1] = pos[1] - 320
        #print(pos)
        particles.append(particle((x*(1+(0.02*20)))+420,320+(y*(1+(0.02*20))),constrain(pos[0],-200,200)*0.05,constrain(pos[1],-200,200)*0.05))
        

    # Clear the screen
    #window.fill(BLUE)
    clears(window)
    updpt()
    drawpt(window)
    time.sleep(0.01)
    

    # Draw the circle
    radius = 50
    center = [x+420, y+320]
    for i in range(len(imagelist)-1,0,-1):
        drawc(imagelist[i],(x*(1+(0.02*i)))+420,320+(y*(1+(0.02*i))),x)

    # Update screen display
    pg.display.flip()

    # Fetch next event
while running:
    run()
# Cleanup resources after quitting
pg.quit()