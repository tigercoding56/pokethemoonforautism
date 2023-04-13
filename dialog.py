import pygame
import time
import math
import ptext
from pygamebutton import PygButton
from diagui import App
import diagui as agui
import random
X = 420
Y = 320
color = (200,220,255)
wcolor = (255,200,150)

sbtn = PygButton(caption="submit",rect=(370,250,50,320-250))
class DIAAPP(App):
    def __init__(self,**options):
        super().__init__(**options)
        agui.Scene(id=0)
        self.inv = agui.ListBox(["dia1","dia2","dia3","dia4"],pos=(0,250),width=370,m=5,fontsize=20,cmd="",name="mn1")        
        App.scene = App.scenes[0]
dia = DIAAPP()
surface = pygame.display.set_mode((X,Y))
def dialog(prompt="",options=["Exit"]):
    global surface
    t = True
    dia.scenes[0].nodes[0].set_list(options)
    while t:
        for event in pygame.event.get():
            dia.scene.do_event(event)
            if "click" in sbtn.handleEvent(event):
                t = False
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.draw.rect(surface, color, pygame.Rect(0, 0, 420, 320))
        ptext.draw( prompt, (10, 70),  color="black")
        dia.run()
    #print(dia.scenes[0].nodes[0].i)
        dia.scenes[0].nodes[0].render()
        dia.scenes[0].nodes[0].draw()
        dia.scene.update()
        dia.scene.draw()
        sbtn.draw(surface)
        pygame.display.update()
        pygame.display.flip()
    return  dia.scenes[0].nodes[0].i
        
#print(dialog("hi how are you?",["good"," normal ","bad"]))