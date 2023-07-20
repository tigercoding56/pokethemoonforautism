import ptext
import dialog
import time
import pygame.gfxdraw
import math
import waterFX
from  ptexture import ptexture
import pygame
import numpy
from pygamebutton import PygButton
from slider import SliderSwitch
import random
def gtqx(x,y):
            return (650+x,254+y,32,32) 
class flightsim():
    def __init__(self):
        self.active = True
        self.particles = []
        self.pp = [0, 0, 0]
        self.tile_textures = {}
        self.imagelist = []
        self.initialised = 1
        mobilebuttons = pygame.image.load('Resources/MISC_ASSETS/buttonmp.png')
        mobilebuttonsd = pygame.image.load('Resources/MISC_ASSETS/buttonmpdown.png')
        upkey_txt = [waterFX.get_texture_slice(mobilebuttons,32,0,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,32,0,slice_size=32)]
        downkey_txt = [waterFX.get_texture_slice(mobilebuttons,32,64,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,32,64,slice_size=32)]
        leftkey_txt = [waterFX.get_texture_slice(mobilebuttons,64,32,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,64,32,slice_size=32)]
        rightkey_txt = [waterFX.get_texture_slice(mobilebuttons,0,32,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,0,32,slice_size=32)]
        intkey_txt = [waterFX.get_texture_slice(mobilebuttons,32,32,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,32,32,slice_size=32)]
        del(mobilebuttons)
        del(mobilebuttonsd)
        self.upbtn = PygButton(rect=gtqx(32,0),normal=upkey_txt[0],highlight=upkey_txt[0],down=upkey_txt[1])
        self.downbtn = PygButton(rect=gtqx(32,64),normal=downkey_txt[0],highlight=downkey_txt[0],down=downkey_txt[1])
        self.leftbtn = PygButton(rect=gtqx(64,32),normal=leftkey_txt[0],highlight=leftkey_txt[0],down=leftkey_txt[1])
        self.rightbtn = PygButton(rect=gtqx(0,32),normal=rightkey_txt[0],highlight=rightkey_txt[0],down=rightkey_txt[1])
        self.exbtn = PygButton(rect=gtqx(32,32),normal=intkey_txt[0],highlight=intkey_txt[0],down=intkey_txt[1])
        for i in range(1,5):
            self.imagelist.append(ptexture('img/a10l'+str(i)+'.png'))
            self.imagelist.append(ptexture('img/a10l'+str(i)+'.png'))
            self.imagelist.append(ptexture('img/a10l'+str(i)+'.png'))
            self.imagelist.append(ptexture('img/a10l'+str(i)+'.png'))

        # Initialize Pygame
        pygame.init()

        # Set up the display window
        self.window = pygame.display.set_mode((840, 640))

        # Load the font
        self.font = pygame.font.Font(None, 24)

        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (56, 76, 255)

        self.x = 0
        self.y = 0

    class particle():
        def __init__(self, x, y, velx, vely):
            self.x = x
            self.y = y
            self.velx = velx
            self.vely = vely
            self.lifetime = 50

    def find_peaks_in_range(self, start, end):
        k_start = int(math.floor((start + self.pp[1]) / 400 - math.asin(1) / math.pi))
        k_end = int(math.ceil((end + self.pp[1]) / 400 - math.asin(1) / math.pi))
        ks = range(k_start, k_end + 1)

        peak_locations = []
        for k in ks:
            i = 400 * (math.asin(1) / math.pi + k) - self.pp[1]
            if i >= start and i <= end:
                peak_locations.append(i)
        return peak_locations



    def constrain(self, val, min_val, max_val):
        if abs(val) < 1:
            if random.randint(1, 2) == 1:
                val = 1
            else:
                val = -1
        return min(max_val, max(min_val, val))

    def drawc(self, surface, x, y, r):
        surface = pygame.transform.rotate(surface.gt(), r)
        self.window.blit(surface, (x - surface.get_width() // 2, y - surface.get_height() // 2))

    def runUI(self):
        
        self.pp = list(numpy.add(self.pp, (int((( self.x-25) / 10)) * 0.1, 1 - (((25 - self.y) * 0.02)), 1)))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.active = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or 'click' in self.leftbtn.handleEvent(event):
                if self.x > -50:
                    self.x -= 10
            if keys[pygame.K_ESCAPE] or 'click' in self.exbtn.handleEvent(event):
                self.active =0
            if keys[pygame.K_RIGHT] or 'click' in self.rightbtn.handleEvent(event):
                if self.x < 50:
                    self.x += 10
            if keys[pygame.K_UP] or 'click' in self.upbtn.handleEvent(event):
                if self.y > -50:
                    self.y -= 10
            if keys[pygame.K_DOWN] or 'click' in self.downbtn.handleEvent(event):
                if self.y < 50:
                    self.y += 10
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pos = pygame.mouse.get_pos()
            pos = list(pos)
            pos[0] = pos[0] - 420
            pos[1] = pos[1] - 320
            self.particles.append(self.particle((self.x * (1 + (0.02 * 20))) + 420, 320 + (self.y * (1 + (0.02 * 20))),self.constrain(pos[0], -200, 200) * 0.05, self.constrain(pos[1], -200, 200) * 0.05))

        self.clears(self.window)
        self.updpt()
        self.updpt()
        self.drawpt(self.window)
        center = [self.x+420, self.y+320]
        for i in range(len(self.imagelist)-1,0,-1):
            self.drawc(self.imagelist[i],(self.x*(1+(0.02*i)))+420,320+(self.y*(1+(0.02*i))),self.x)
        #print(self.x)
        self.upbtn.draw(self.window)
        self.downbtn.draw(self.window)
        self.leftbtn.draw(self.window)
        self.rightbtn.draw(self.window)
        self.exbtn.draw(self.window)
        time.sleep(0.01)

        pygame.display.flip()

    def clears(self, surface):
        for i in range(0, 640):
            t = max(min(int(math.sin((i + self.pp[1]) / 400) * 255), 255), 40)
            pygame.gfxdraw.hline(surface, 0, 840, i, (40, 40, (t / 255) * 100 + 150))

        for xt in self.find_peaks_in_range(-300, 1000):
            for i in range(1, 20):
                ikey = hash(str(i)) % 3000
                z = int(((self.pp[2] + ikey) % 300)) / 300
                x = (int((self.pp[0] + (i * 45)) % 900) - 25)
                self.drawcloud(x, int(xt) + (z * 50), z, surface)
                #print(int(x))

    def drawcloud(self, x, y, z, surface):
        z = min(max(z, 0), 1)
        cloud = ptexture('img/cloud.png').gt()
        surface.blit(pygame.transform.scale_by(cloud,z),(int(x)-(cloud.get_height()/5),int(y)-(cloud.get_width()/2)))
        #surface.blit(pygame.transform.scale(cloud, z),(int(x) - (cloud.get_height() // 2), int(y) - (cloud.get_width() // 2)))

    def updpt(self):
        for i in range(len(self.particles) - 1, -1, -1):
            try:
                if self.particles[i].lifetime < 1:
                    if len(self.particles) < 2:
                        self.particles = []
                    else:
                        del (self.particles[i])
                else:
                    self.particles[i].lifetime += -1
                    self.particles[i].x += self.particles[i].velx
                    self.particles[i].y += self.particles[i].vely
            except:
                self.particles = []

    def drawpt(self, surface):
        for i in self.particles:
            pygame.draw.line(surface, (169, 54, 45), (i.x, i.y), (i.x + i.velx, i.y + i.vely), 2)

    def run(self):
        while self.active:
            self.runUI()

        # Cleanup resources after quitting
        pygame.quit()

# Create an instance of the UIdialogbase class and start the UI dialog
if __name__ == "__main__":
    ui_dialog = flightsim()
    ui_dialog.run()
