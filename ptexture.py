import pygame
ptextures = {}#optimisation to not need a rtx 4090 XYT
class ptexture(): # a texture pointer class
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