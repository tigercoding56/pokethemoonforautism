import pygame,random
import math
import time
ptextures = {}#optimisation to not need a rtx 4090 XYT
class xtexture(): # a texture pointer class
    def __init__(self,location,a=1,rescale=1):
        global tile_textures
        if not str(location) in ptextures:
            a = 1
            preimg = pygame.image.load(str(location)).convert_alpha()
            ptextures[str(location)] = preimg
            del(preimg)
        self.location = str(location)
    def gt(self):
        global ptextures
        return ptextures[self.location]
planet_textures = []
pygame.init()
pygame.display.set_mode((1,1))
for i in range(1,24):
    name_cache = "Planets/planet-"+str(i)+".png"
    planet_textures.append(name_cache)
    io = xtexture(name_cache)

width = 800
height = 600

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 153)

# Create stars
num_stars = 200
stars = []
for _ in range(num_stars):
    x = random.randint(0, width*4)
    y = random.randint(0, height*4)
    size = random.randint(1, 3)
    color = random.choice([WHITE, YELLOW])  # Colorize the stars
    stars.append((x, y, size, color))

# Create planets
num_planets = 20
planets = []
planet_images = []
for i in range(num_planets):
    x = random.randint(0, width*4)
    y = random.randint(0, height*4)
    size = random.randint(10, 20)
    planets.append((x, y, size))

# Create galactic fog
fog_image = pygame.image.load("Planets/bg.png")  # Replace with actual fog image



def  drawplanetsurface(mouse_x,mouse_y,width,height):
        global fog_image,planets,stars,planet_textures
        screen = pygame.surface.Surface((width,height))
        # Draw planets
        i=0
        gx = mouse_x / 100
        gy = mouse_y / 100
        screen.blit(fog_image, (gx, gy))
        screen.blit(fog_image, (gx+512, gy))
        screen.blit(fog_image, (gx+512, gy+512))
        screen.blit(fog_image, (gx, gy+512))
        for planet in planets:
            i = i +1
            x, y, size = planet
            parallax_x = ((x - mouse_x) / (100-size)) 
            parallax_y = ((y - mouse_y) / (100-size) )
            xt = (x + parallax_x )% 2000
            yt = (y + parallax_y) % 2000
            
            if not (xt > (width+128) or yt > (height+128)) :
                planet_image = pygame.transform.scale(xtexture(planet_textures[i%len(planet_textures)]).gt(), (size, size))
                screen.blit(planet_image, (int(xt ), int(yt )))

        # Draw stars with parallax effect
        i = 0
        for star in stars:
            i = i +1
            x, y, size, color = star
            parallax_x = ((x - mouse_x) / (100-size)) 
            parallax_y = ((y - mouse_y) / (100-size) )
            xt = (x + parallax_x )% 2000
            yt = (y + parallax_y) % 2000
            if (i % 50 ) == 1:
                if not(xt > (width+228) or yt > (height+228)) :
                    screen.blit(xtexture('Planets/fog.png').gt(), (int(xt ), int(yt )))
            else:
                if not( xt > (width+128) or yt > (height+128)) :
                    pygame.draw.circle(screen, color, (int(xt), int(yt )), size)
        return screen

# Main game loop


# Quit the game
pygame.quit()

