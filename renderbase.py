import pygame
def svimg(xgmap):
    frametime = 0
    tx = pygame.Surface((240*20,240*20))
    for x in range(1,240):
            for y in range(1,240):
                x = x 
                y = y
                threed = True
                tile = xgmap.read(xgmap.heightmap,x ,y )
                tile2= xgmap.read(xgmap.structuremap,x ,y ,True)
                #tile3= xgmap.readraw(xgmap.threedeffecthax,x ,y )
                tile4= xgmap.readraw(xgmap.threedfx,x ,y )
                tile5= xgmap.readraw(xgmap.threedfx,x ,y +1)
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
                           if (tile4[0]) > (tile5[0]):
                               tx.blit(xgmap.threedoverlay,(x*20,y*20))
    pygame.image.save(tx, "fmap.png")