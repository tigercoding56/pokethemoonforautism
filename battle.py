import pygame
import PIL
from PIL import Image
import time
import ptext
from xmap import *
pygame.init()
X = 320
Y = 320
height = 100
overlap = 100
pygame.key.set_repeat(250)

pygame.init()
 
# Initializing surface
surface = pygame.display.set_mode((X, Y))
 
# Initializing RGB Color
color = (0, 0, 255)
 
# Changing surface color
surface.fill(color)
pygame.display.flip()
def display(surface):
        i = 130
        pygame.draw.polygon(surface,(0,0,0),[(0,0),(i,0),(i + (overlap * 0.5) + 51,Y-height),(0,Y-height)],0)
        pygame.draw.polygon(surface,(255,255,255),[(320,Y-height),(320-i,Y-height),(320-(i + (overlap * 0.5) + 51),0),(320,0)],0)
        pygame.draw.polygon(surface,(55,55,110),[(0,320),(0,Y-(i*0.7692307692307693)),(320,Y-(i*0.7692307692307693)),(320,320)],0)
        pygame.display.flip()    
def transition(surface):
    for i in range(1,130):
        pygame.draw.polygon(surface,(0,0,0),[(0,0),(i,0),(i + (overlap * 0.5) + 51,Y-height),(0,Y-height)],0)
        pygame.draw.polygon(surface,(255,255,255),[(320,Y-height),(320-i,Y-height),(320-(i + (overlap * 0.5) + 51),0),(320,0)],0)
        pygame.draw.polygon(surface,(55,55,110),[(0,320),(0,Y-(i*0.7692307692307693)),(320,Y-(i*0.7692307692307693)),(320,320)],0)
        pygame.display.flip()
        time.sleep(0.01)
transition(surface)