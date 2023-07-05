import pygame
def svimg(xgmap):
    frametime = 0
    tx = pygame.Surface((240*40,240*20))
    for x in range(1,480):
            for y in range(1,240):
                x = x 
                y = y
                threed = True
                tile = xgmap.heightmap.rmmap((x ,y))
                tile2= xgmap.structuremap.rmmap((x ,y) ,True)
                #tile3= xgmap.readraw(xgmap.threedeffecthax,x ,y )
                tile4= xgmap.getheight(x ,y)
                tile5= xgmap.getheight(x ,y+1)
                tile6 = xgmap.getheight(x ,y-1)
                img = tile.gtx(frametime).gt()
                tx.blit(img,(x*20,y*20))
                if not tile2 == "none":
                    if tile2.name == "steppingstones":
                       threed = False
                    img2 = xgmap.read(xgmap.structuremap,x ,y ,exc="gt()").gt()
                    tx.blit(img2,(x*20,y*20))
                if threed == True:
                  if not (tile5 == (0,255,255,255) or tile5 == "none" or tile5 == (255,0,0,255) ):
                      if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                           if (tile4) > (tile5):
                               tx.blit(xgmap.threedoverlay,(x*20,y*20))
                  if not (tile6 == (0,255,255,255) or tile6 == "none" or tile6 == (255,0,0,255) ):
                      if not (tile4 == (0,255,255,255) or tile4 == "none" or tile4 == (255,0,0,255)):
                           if (tile4) > (tile6):
                               tx.blit(xgmap.threedoverlay2,(x*20,y*20))
    pygame.image.save(tx, "fmap.png")