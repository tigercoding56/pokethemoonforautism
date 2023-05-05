import pygame
import time
import math
import ptext
from listbox import ListBox
from pygamebutton import PygButton
#from diagui import App
#import diagui as agui
import random
X = 420
Y = 320
diaoverides = [["$TIME","time.asctime(time.localtime())"],["$SendContentID","\" \""]]
color = (200,220,255)
wcolor = (255,200,150)
def scale(x,y,x1,y1):
    return (x*2,y*2,x1*2,y1*2)
sbtn = PygButton(caption="submit",rect=scale(370,250,50,70))
surface = pygame.display.set_mode((X,Y))
list_box = ListBox(0, 500, 740, 140, ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6'])
def dialog(prompt="",options=["Exit"]):
    global surface, list_box,diaoverides
    t = True
    list_box.setl(options)
    time.sleep(0.1)
    for i in diaoverides:
        #try:
            prompt = prompt.replace(i[0],eval(i[1]))
        #except Exception as ex23:
           # io = 0
            #print(ex23)
    while t:
        for event in pygame.event.get():
            dia.scene.do_event(event)
            if "click" in sbtn.handleEvent(event):
                t = False
            if event.type == pygame.QUIT:
                pygame.quit()
            list_box.handle_event(event)
        pygame.draw.rect(surface, color, pygame.Rect(0, 0, 840, 640))
        ptext.draw( prompt, (10, 80),  color="black")
    #print(dia.scenes[0].nodes[0].i)
        list_box.draw(surface)
        sbtn.draw(surface)
        pygame.display.update()
        pygame.display.flip()
    return  list_box.selected_item


def rndialog(prompt="",options=["Exit"],cpos=0):
    global surface,list_box , diaoverides
    t = True
    for i in diaoverides:
        try:
            prompt = prompt.replace(i[0],eval(i[1]))
        except Exception as ex23:
            print("dia overide failed  \n " + str(i) + "\n error:" + "\n" + str(ex23))
    list_box.setl(options)
    for event in pygame.event.get():
            if "click" in sbtn.handleEvent(event):
                t = False
            if event.type == pygame.QUIT:
                pygame.quit()
            list_box.handle_event(event)
    pygame.event.clear(pump=True)
    pygame.draw.rect(surface, color, pygame.Rect(0, 0, 840, 640))
    ptext.draw( prompt, (10, 70),  color="black")
    list_box.draw(surface)
    sbtn.draw(surface)
    pygame.display.update()
    #pygame.display.flip()
    output = [list_box.selected_item,t]
    return  output
        