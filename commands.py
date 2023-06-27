ccmd = {}
ccmd["/1"] = "pos1 = gtcpos(True)"
ccmd["/2"] = "pos2 = gtcpos(True)"
ccmd["/fill"] ='''
for tx in gprt(pos1[0],pos2[0]):
    for ty in gprt(pos1[0],pos2[0]):
        print(str([[tx,ty],selectedt])+",",end='')
        cmap.structuremap.smmap([tx,ty],cmap.tiles[selectedt])


'''
def gprt(n1,n2):
    dist = n2-n1
    abdist = abs(dist) + 0.0000001
    it = int(dist/abdist)
    return  range(int(n1),int(n2)+it,it)

