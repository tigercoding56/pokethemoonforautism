import pygame
import random
import math
from pygame.locals import *
import copy
#import numpy as np
SCREEN_SIZE = (640, 480)
CELL_SIZE = 2
NUM_ENTITIES = 20
import timeit

class Entity():
    def __init__(self, x, y):
        self.pos = [x, y]
        self.vel = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.delme = 0
    
    def run(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] < 0:
            self.pos[0] = 0
            self.vel[0] = -self.vel[0]
        elif self.pos[0] > SCREEN_SIZE[0]:
            self.pos[0] = SCREEN_SIZE[0]
            self.vel[0] = -self.vel[0]
        if self.pos[1] < 0:
            self.pos[1] = 0
            self.vel[1] = -self.vel[1]
        elif self.pos[1] > SCREEN_SIZE[1]:
            self.pos[1] = SCREEN_SIZE[1]
            self.vel[1] = -self.vel[1]
        
        return self


class EntityMap():
    def __init__(self):
        self.mmap = {}
    
    def snap(self, p1, p2):
        if [math.floor(i) for i in p1] == [math.floor(i) for i in p2]:
            return 0
        else:
            return 1
        
    def write(self, entity, pos,cp=1):
        entity.pos = pos
        if cp:
            entity = copy.deepcopy(entity)
        key = tuple([math.floor(x/CELL_SIZE) for x in pos])
        if key in self.mmap:
            self.mmap[key].append(entity)
        else:
            self.mmap[key] = [entity]
    
    def run(self):
        keys_to_remove = []
        kwtw = []
        for key ,value in self.mmap.items():
            if len(value) <1:
                keys_to_remove.append(key)
            else:
                self.mmap[key] = [i.run() for i in self.mmap[key]]
                rmi = [self.mmap[key].pop(i) for i in range(len(self.mmap[key])-1, -1, -1) if self.snap(self.mmap[key][i].pos,list(key))]
                delthis = [self.mmap[key].pop(i) for i in range(len(self.mmap[key])-1, -1, -1) if self.mmap[key][i].delme]
                for i in rmi:
                    kwtw.append(i)
                    
                
        for i in keys_to_remove:
            del(self.mmap[i])
        for i in kwtw:
            self.write(i,i.pos,cp=0)
        del(kwtw)
        del(keys_to_remove)
class EntityMap():
    def __init__(self):
        self.mmap = {}
    
    def snap(self, p1, p2):
        for i in range(len(p1)):
            if int(p1[i]) != int(p2[i]):
                return False
        return True
        
    def write(self, entity, pos, cp=1):
        entity.pos = pos
        if cp:
            entity = copy.deepcopy(entity)
        key = tuple([int(x/CELL_SIZE) for x in pos])  # round down to nearest cell
        if key in self.mmap:
            self.mmap[key].append(entity)
        else:
            self.mmap[key] = [entity]
    
    def run(self):
        keys_to_remove = []
        kwtw = []
        for key, value in self.mmap.items():
            if not value:
                keys_to_remove.append(key)
            else:
                value = [i.run() for i in value]
                rmi = []  # indices of entities to be removed
                delthis = []  # entities to be deleted
                for i in range(len(value)-1, -1, -1):
                    if self.snap(value[i].pos, [x*CELL_SIZE for x in key]):
                        rmi.append(i)
                    elif value[i].delme:
                        delthis.append(i)
                for i in rmi:
                    kwtw.append(value.pop(i))
                for i in delthis:
                    value.pop(i)
                self.mmap[key] = value
        
        for i in keys_to_remove:
            del(self.mmap[i])
        for i in kwtw:
            self.write(i, i.pos, cp=0)
        del(kwtw)
        del(keys_to_remove)


def main():
    # Initialize pygame
    pygame.init()
    tx=1
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Entity Demo")

    # Create some entities
    entities = []
    for i in range(0,9999):
     x = random.randint(0, SCREEN_SIZE[0])
     y = random.randint(0, SCREEN_SIZE[1])
     entities.append(Entity(x, y))

    entity_map = EntityMap()
    for entity in entities:
        entity_map.write(entity, entity.pos)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        


        entity_map.run()
        elapsed_time = timeit.timeit(lambda: entity_map.run(), number=1)
        print(elapsed_time)

        screen.fill((0, 0, 0))


        tx= tx +1%5
        for pos_list in entity_map.mmap.values():
            #tx = 0
            for entity in pos_list:
                x = int(entity.pos[0])
                y = int(entity.pos[1])
                #print(x)
                #if random.randint(1,5)==2:
                
                pygame.draw.circle(screen, (255, entity.pos[0]%255,entity.pos[1]% 255), (x, y), 1)

        pygame.display.flip()

    pygame.quit()
main()