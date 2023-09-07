_O='upd_after_init failed with reason:\n\n'
_N='needs_upd_after_init'
_M='inventory'
_L='.dat'
_K='savegame'
_J='DATA.dat'
_I='DATA'
_H='0.2'
_G=None
_F='0.2-D'
_E='settings'
_D='none'
_C='WMP'
_B=False
_A=True
import pygame,UIdialogdef,standartUIdialogref,waterFX,gc
from math import floor
from copy import deepcopy
import renderbase
from renderbase import svimg
import time,ptext,pickle,base64
from commands import ccmd
from commands import gprt
import enemies as EM,xmap
from xmap import dlgtree
from xmap import gmap
from xmap import*
from pygamebutton import PygButton
from pygame.locals import DOUBLEBUF
onweb=0
pos1=[0,0]
pos2=[0,0]
markp=0
sound_intr=-1
selectedt=0
xprint=print
printatall=1
def zprint(x,**kwargs):
	global printatall
	if printatall==1:xprint(x,**kwargs)
print=zprint
mobilebuttons=pygame.image.load('Resources/MISC_ASSETS/buttonmp.png')
mobilebuttonsd=pygame.image.load('Resources/MISC_ASSETS/buttonmpdown.png')
upkey_txt=[waterFX.get_texture_slice(mobilebuttons,32,0,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,32,0,slice_size=32)]
downkey_txt=[waterFX.get_texture_slice(mobilebuttons,32,64,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,32,64,slice_size=32)]
leftkey_txt=[waterFX.get_texture_slice(mobilebuttons,64,32,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,64,32,slice_size=32)]
rightkey_txt=[waterFX.get_texture_slice(mobilebuttons,0,32,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,0,32,slice_size=32)]
intkey_txt=[waterFX.get_texture_slice(mobilebuttons,32,32,slice_size=32),waterFX.get_texture_slice(mobilebuttonsd,32,32,slice_size=32)]
del mobilebuttons
del mobilebuttonsd
muted=1
pygame.mixer.init()
cmap=gmap(tiles)
for update_x in range(cmap.structuremap.size[0]):
	for update_y in range(cmap.structuremap.size[1]):
		tilex=cmap.read(cmap.structuremap,update_x,update_y,_A)
		try:
			if hasattr(tilex,_N):cmap=tilex.updtmp(cmap);cmap.structuremap=cmap.sett(cmap.structuremap,update_x,update_y,tilex)
		except Exception as iex:print(_O+str(iex))
for update_x in range(cmap.heightmap.size[0]):
	for update_y in range(cmap.heightmap.size[1]):
		tilex=cmap.read(cmap.heightmap,update_x,update_y,_A)
		try:
			if hasattr(tilex,_N):cmap=tilex.updtmp(cmap);cmap.heightmap=cmap.sett(cmap.heightmap,update_x,update_y,tilex)
		except Exception as iex:print(_O+str(iex))
outsoundtrack=pygame.mixer.Sound('audio/peasant kingdom.ogg')
insoundtrack=pygame.mixer.Sound('audio/JRPG_town_loop.ogg')
fcw=0
cplayer.speed=.5
def fancywatertrans(x):
	global fcw;fcw=fcw+int(x)*.1
	if fcw>1:fcw=1
	elif fcw<.1:fcw=0
def intsound(x):
	global sound_intr,outsoundtrack,insoundtrack,muted
	if muted==0:
		if x==1:
			if not sound_intr==1:outsoundtrack.fadeout(2000);insoundtrack.play(-1,fade_ms=2000)
		if x==0:
			if not sound_intr==0:insoundtrack.fadeout(2000);outsoundtrack.play(-1,fade_ms=2000)
		sound_intr=x;outsoundtrack.set_volume(1-sound_intr);insoundtrack.set_volume(sound_intr)
	else:outsoundtrack.stop();insoundtrack.stop()
ptextures={}
class xtexture:
	def __init__(self,location,a=1,rescale=1):
		global ptextures
		if not str(location)in ptextures:a=1;preimg=pygame.image.load(str(location)).convert_alpha();ptextures[str(location)]=preimg;del preimg
		self.location=str(location)
	def gt(self):global ptextures;return ptextures[self.location]
if __import__('sys').platform=='emscripten':from platform import window;onweb=1;muted=0;window.fs_loaded=_B
else:import os
ActionQueue=[]
mousepos=[1,0]
transition=[1,_C,_C]
AREAS=[_C,'ARENA','INV']
ACTIVEAREA=_C
X=840
Y=640
default_data={_E:[1,1,1,1,0]}
def save_data(slot,data):
	global onweb,default_data
	if onweb:default_data[slot]=data;sd=[_F,default_data];window.localStorage.setItem(_I,str(base64.b64encode(pickle.dumps(sd)).decode('ascii')))
	else:
		sd=deepcopy(default_data);sd[slot]=data;default_data=deepcopy(sd)
		with open(_J,'wb')as svg:pickle.dump([_F,sd],svg)
def load_data(slot,default):
	global onweb,default_data
	if onweb:
		if not window.localStorage.getItem(_I)==_G:
			temp=window.localStorage.getItem(_I);sd=pickle.loads(base64.b64decode(temp))
			if sd[0]==_F:
				if slot in sd[1]:default_data=sd[1];return sd[1][slot]
	elif os.path.exists(_J):
		with open(_J,'rb')as svg:
			sd=pickle.load(svg)
			if sd[0]==_F:
				if slot in sd[1]:default_data=sd[1];return sd[1][slot]
				else:return default
	return default
def save(slot):
	global cmap,onweb,xmap,cplayer
	if onweb:sd=[_H,cplayer,cmap.structuremap.getdiff(),cmap.heightmap.getdiff(),xmap.tiledef.quests];window.localStorage.setItem(str(slot),str(base64.b64encode(pickle.dumps(sd)).decode('ascii')))
	else:
		sd=[_H,cplayer,cmap.structuremap.getdiff(),cmap.heightmap.getdiff(),xmap.tiledef.quests]
		with open(_K+slot+_L,'wb')as svg:pickle.dump(sd,svg)
def load(slot):
	global cmap,onweb,xmap,cplayer
	if onweb:
		if not window.localStorage.getItem(str(slot))==_G:
			temp=window.localStorage.getItem(str(slot));sd=pickle.loads(base64.b64decode(temp))
			if sd[0]==_H:cplayer=sd[1];cmap.structuremap.applydiff(sd[2]);cmap.heightmap.applydiff(sd[3]);xmap.tiledef.quests=sd[4]
	elif os.path.exists(_K+slot+_L):
		with open(_K+slot+_L,'rb')as svg:
			sd=pickle.load(svg)
			if sd[0]==_H:cplayer=sd[1];cmap.structuremap.applydiff(copy.deepcopy(sd[2]));cmap.heightmap.applydiff(copy.deepcopy(sd[3]));xmap.tiledef.quests=copy.deepcopy(sd[4]);xmap.tiledef.quests={'intro':3,'HOFF':0,'getradio1':1,'seldone':1,'reportbackrd':1,'radiodone':1,'ART':1,'rbf2':2,'GTH':1}
def scale(x,y,x1,y1):return x*2,y*2,x1*2,y1*2
invbtn=PygButton(caption=_M,rect=scale(320,280,100,20))
svbtn=PygButton(caption='save game',rect=scale(320,260,100,20))
lvbtn=PygButton(caption='load game',rect=scale(320,240,100,20))
intbtn=PygButton(caption='interact ',rect=scale(320,300,100,20))
dbbtn=PygButton(caption='costumise tile',rect=scale(320,220,100,20))
settingsbtn=PygButton(caption='settings ',rect=scale(320,200,100,20))
def gtqx(x,y):return 650+x,254+y,32,32
upbtn=PygButton(rect=gtqx(32,0),normal=upkey_txt[0],highlight=upkey_txt[0],down=upkey_txt[1])
downbtn=PygButton(rect=gtqx(32,64),normal=downkey_txt[0],highlight=downkey_txt[0],down=downkey_txt[1])
leftbtn=PygButton(rect=gtqx(64,32),normal=leftkey_txt[0],highlight=leftkey_txt[0],down=leftkey_txt[1])
rightbtn=PygButton(rect=gtqx(0,32),normal=rightkey_txt[0],highlight=rightkey_txt[0],down=rightkey_txt[1])
intxbtn=PygButton(rect=gtqx(32,32),normal=intkey_txt[0],highlight=intkey_txt[0],down=intkey_txt[1])
pygame.key.set_repeat(250)
fancywaterl=0
def smwt(x):
	fancywaterl=fancywaterl+x*.1
	if fancywaterl<.1:fancywaterl=0
def getattacks():global defaultpk;return defaultpk
class text:
	def __init__():0
class characterinstance:
	def __init__(self,name,desc,pos):self.name=name;self.desc=desc;self.pos=pos
class playerinstance:
	def __init__(self,inv,basechar):self.inv=inv;self.pos=basechar.pos;self.name=basechar.name;self.desc=basechar.desc
class camera:
	def __init__(self):self.cx=0;self.cy=0;self.targetx=0;self.targety=0;self.percentage=1;self.lx=0;self.ly=0;self.steps=1
	def lerp(self,v1,v2,percentage):return v1+(v2-v1)*percentage
	def move(self,tx,ty,steps=10):self.targetx=tx;self.targety=ty;self.lx=self.ctx;self.ly=self.cty;self.steps=steps;self.percentage=0;self.cx=tx;self.cy=ty
	def tp(self,tx,ty):self.steps=0;self.percentage=0;self.lx=tx;self.ly=ty;self.targetx=tx;self.targety=ty;self.ctx=tx;self.cty=ty;self.cx=tx;self.cy=ty
	def run(self):
		if self.percentage<self.steps:self.percentage=self.percentage+1;self.ctx=self.lerp(self.lx,self.targetx,1/(self.steps-self.percentage));self.cty=self.lerp(self.ly,self.targety,1/(self.steps-self.percentage))
		if self.percentage>=self.steps:self.ctx=self.targetx;self.cty=self.targety
		self.cx=int(self.ctx);self.cy=int(self.cty)
message=['',0]
def calc_dir(point1,point2):
	dx=point2[0]-point1[0];dy=point2[1]-point1[1];direction_rad=math.atan2(dy,dx);direction_deg=math.degrees(direction_rad)
	if direction_deg<0:direction_deg+=360
	direction_int=int(round(direction_deg));return direction_int
def get_tile_value(x,y,frametime,skip_percentage=2):
	tile_x=x;tile_y=y;num_tiles_x=4000;num_tiles_y=4000;skip_tiles=int(num_tiles_x*num_tiles_y*(skip_percentage/100));tile_index=(tile_x+tile_y*num_tiles_x)%(num_tiles_x*num_tiles_y);interlace_state=int((tile_index//num_tiles_x+tile_index%num_tiles_x+frametime//(skip_percentage+1))%2==0 and tile_index>=skip_tiles)
	if frametime%(skip_percentage+1)==interlace_state:return 1
	else:return 0
previouspos=[0,0]
def get_direction(x1,y1,x2,y2):dx=x2-x1;dy=y2-y1;radians=math.atan2(dy,dx);degrees=math.degrees(radians);return degrees
class render:
	def __init__(self):global X,Y,fcw;self.optbuffer={};self.TUPD=0;self.tilecache={};self.tileentsp=[];self.tilebuffer={};self.skytexture=xtexture('img/sky.png').gt();self.skytexture=pygame.transform.scale(self.skytexture,(X,Y));self.wateroffsetext=waterFX.generate_texture(pygame.time.get_ticks()/2000,40,40);self.screen=pygame.display.set_mode((X,Y));self.vbuffer=pygame.surface.Surface((840,840)).convert_alpha();self.wrfb=pygame.surface.Surface((40,4)).convert();self.wrfb2=pygame.surface.Surface((40,8)).convert();self.playerpreimg=pygame.transform.scale(pygame.image.load('img/player.png'),(40,40));self.highlight=pygame.transform.scale(pygame.image.load('img/hilight.png'),(40,40));self.arenaimg=pygame.image.load('img/battlearena.png');self.grass_texture_image='Resources/MISC_ASSETS/Grass_color.png';self.grass_normal_map_image='Resources/MISC_ASSETS/Grass_normal.png';self.bggrasstxt=waterFX.apply_normal_map(self.grass_texture_image,self.grass_normal_map_image,45,(0,0))
	def gets(self,value,t='False'):0
	def shaderz(self):
		for x in range(1,320):
			for y in range(1,320):color=self.screen.get_at((x,y))
	def renderarena(self):self.screen.blit(self.arenaimg,(0,0))
	def hash_tile(self,tile1,tile2,tile4,tile5,tile6):
		if tile2==_D:return str(str(type(tile1).__name__)+str(tile4)+str(tile5)+str(tile6))
		else:return str(type(tile1).__name__+type(tile2).__name__+str(tile4)+str(tile5)+str(tile6))
	def hash_tiles(self,tiles):
		thash=''
		for i in tiles:
			if not i.__class__.__name__=='str':
				try:
					if i.__class__.__name__=='int':thash=thash+str(i)
					else:thash=thash+str(type(i).__name__+str(i.name))
				except Exception as IE:thash=thash+str(type(i).__name__)+str(i)
		return thash
	def renderwmp(self,camera,xgmap,frametime):
		E='reflectivity';D='UAM';C='steppingstones';B='grass';A='water';global mousepos,message,onweb,selectedt,rlcam,fcw,settings,previouspos;performance=0;self.screen.blit(self.skytexture,(0,0));tileupd=self.TUPD;self.TUPD=0;cmap.run_ent();getmessage();wvb=[];vb1=[];vb2=[];vbr=[];vb3=[];vb4=[];vb5=[];csound=0;wimg='';wimgb='';xteeed=0
		if floor(previouspos[0])!=floor(camera.cx)or floor(previouspos[1])!=floor(camera.cy):previouspos=camera.cx,camera.cy;xteeed=1
		ptdraw=[]
		for xtt in range(-1,17):
			for ytt in range(0,18):
				x=xtt;y=ytt;threed=_A;ptdraw=ptdraw+[[[x,y],cmap.read_ent((int(x+self.gets(camera.cx,_A)),int(y+self.gets(camera.cy,_A))))]]
				if xteeed==1 or not(xtt,ytt)in self.tilecache or frametime%5==1:tile=xgmap.heightmap.rmmap((int(x+self.gets(camera.cx,_A)),int(y+self.gets(camera.cy,_A))));tile2=xgmap.structuremap.rmmap((int(x+self.gets(camera.cx,_A)),int(y+self.gets(camera.cy,_A))),_A);tile4=xgmap.getheight(int(x+self.gets(camera.cx,_A)),int(y+self.gets(camera.cy,_A)));tile5=xgmap.getheight(int(x+self.gets(camera.cx,_A)),int(y+self.gets(camera.cy,_A)+1));tile6=xgmap.getheight(int(x+self.gets(camera.cx,_A)),int(y+self.gets(camera.cy,_A)-1));self.tilecache[xtt,ytt]=tile,tile2,tile4,tile5,tile6
				else:tile,tile2,tile4,tile5,tile6=self.tilecache[xtt,ytt]
				if not tile.name==A:img=tile.gtx(frametime).gt()
				if tile2==_D:txa=0
				else:
					if tile2.name=='townmarker':csound=1
					try:txa=tile2.animated
					except:tile2.animated=0;txa=0
				stile=0;t=self.hash_tiles([tile,tile2,tile4,tile5,tile6]);xtu=str(x)+','+str(y)
				if xtu in self.optbuffer:
					if self.optbuffer[xtu]==t:stile=1
					else:self.optbuffer[xtu]=t
				else:self.optbuffer[xtu]=t
				xs=stile;performance=settings[2]
				if not(tile.animated==0 and txa==0):stile=0;self.optbuffer[xtu]=t
				if B in tile.name and tile2==_D:
					if performance==0:stile=1
					stile=0
				if settings[1]==1 and stile==0 and not xs==0:
					if tileupd>105 and(xtt%5+frametime%5)%int(tileupd/30)!=1:stile=1
				if hasattr(tile,D)and xteeed:stile=0
				if hasattr(tile2,D)and xteeed:stile=0
				if hasattr(tile2,'name'):
					if tile2.name=='pedestal':fn=frametime;stile=0;img2=tile.gtx(fn).gt()
				if tile.name==A:
					fn=frametime%30;img=tile.gtx(fn).gt()
					if fn==1:stile=0
					elif fn==12:stile=0
					elif fn==23:stile=0
				if stile==0:
					self.TUPD=self.TUPD+1
					if not tile.name==A:
						ximg=img.copy()
						if hasattr(tile,E):ximg.set_alpha(255-tile.reflectivity);self.vbuffer.fill((0,0,0,0),(x*40,y*40,40,40))
						if performance==3:
							if B in tile.name and tile2==_D:point=40*xtt+floor(self.gets(camera.cty,_A))*40,ytt+floor(self.gets(camera.cty,_A))*40;xti=waterFX.apply_normal_map(self.grass_texture_image,self.grass_normal_map_image,calc_dir(point,(840+self.gets(camera.ctx,_A)*40,self.gets(camera.cty,_A)*40)),point);xti.set_alpha(100);ximg.blit(xti,(0,0))
							elif B in tile.name:xti=self.bggrasstxt;xti.set_alpha(100);ximg.blit(xti,(0,0))
						vb1.append((ximg,(x*40,y*40)))
					elif tile.name==A:
						wimg=img
						if wimg=='':
							if frametime%4==1:
								if performance==0:self.wateroffsetext=waterFX.generate_texture(pygame.time.get_ticks()/2000,40,40)
						xti='';wimgx=wimg.copy()
						if settings[1]==0:fcw=1
						wimgx.set_alpha(200);self.vbuffer.fill((0,0,0,0),(x*40,y*40,40,40));wvb.append((wimgx,(x*40,y*40)))
						if 0==0:
							if tile.name==A and tile2==_D:
								wtile=xgmap.read(xgmap.heightmap,x+self.gets(camera.cx,_A),y+self.gets(camera.cy,_A)+1);wtile2=xgmap.read(xgmap.structuremap,x+self.gets(camera.cx,_A),y+self.gets(camera.cy,_A)+1,_A)
								if not wtile.name==A:
									self.wrfb.blit(pygame.transform.scale(pygame.transform.flip(wtile.gt().gt(),_B,_B),(40,4)),[0,0])
									if not wtile2==_D:
										if not wtile2.name==C:self.wrfb.blit(pygame.transform.scale(pygame.transform.flip(wtile2.gt().gt(),_B,_B),(40,4)),[0,0])
									self.wrfb.set_alpha(100);vb5.append((self.wrfb,(x*40,y*40+36)))
								wtile=xgmap.read(xgmap.heightmap,x+self.gets(camera.cx,_A),y+self.gets(camera.cy,_A)-1);wtile2=xgmap.read(xgmap.structuremap,x+self.gets(camera.cx,_A),y+self.gets(camera.cy,_A)-1,_A)
								if not wtile.name==A:
									self.wrfb2.blit(pygame.transform.scale(pygame.transform.flip(wtile.gt().gt(),_B,_A),(40,8)),[0,0])
									if not wtile2==_D:
										if not wtile2.name==C:self.wrfb2.blit(pygame.transform.scale(pygame.transform.flip(wtile2.gt().gt(),_B,_A),(40,8)),[0,0])
									self.wrfb.set_alpha(100);vb5.append((self.wrfb,(x*40,y*40)))
					if not tile2==_D:
						if tile2.name==C:threed=_B
						img2=xgmap.read(xgmap.structuremap,x+self.gets(camera.cx,_A),y+self.gets(camera.cy,_A),exc='gtx('+str(frametime)+')').gt()
						if not tile2.hidden:
							ximg2=img2.copy()
							if hasattr(tile2,'metalshading'):ximg2.blit(waterFX.specular(ximg2,xtexture('img/normal.png').gt(),(int(.2*get_direction(xtt*40+self.gets(camera.ctx),ytt*40+self.gets(camera.cty),159*2+20,159*3))-45)%360),(0,0))
							if hasattr(tile2,'shineimage'):ximg2.blit(waterFX.specular(ximg2,tile2.shineimage.gt(),(int(.2*get_direction(xtt*40+self.gets(camera.ctx),ytt*40+self.gets(camera.cty),159*2+20,159*3))-45)%360),(0,0))
							if hasattr(tile2,E):ximg2.set_alpha(255-tile2.reflectivity);self.vbuffer.fill((0,0,0,0),(x*40,y*40,40,40))
							if not hasattr(tile2,'ex_shadow'):
								if tile2.place_last:vb2.append((ximg2,(x*40,y*40)))
								else:vb3.append((ximg2,(x*40,y*40)))
							elif not tile2.pos in self.tileentsp:xent=cmap.entities[3];xent.texture=tile2.shadowtxt;xent.pos=tile2.pos;cmap.add_entity(xent,tile2.pos);self.tileentsp.append(tile2.pos)
		if len(wvb)>0:self.vbuffer.blits(wvb)
		self.vbuffer.blits(vb1)
		if len(vb2)>0:self.vbuffer.blits(vb2)
		if len(vbr)>0:self.vbuffer.blits(vbr)
		if len(vb3)>0:self.vbuffer.blits(vb3)
		if len(vb4)>0:self.vbuffer.blits(vb4)
		if len(vb5)>0:self.vbuffer.blits(vb5)
		blitpos=[0,0]
		if list(mousepos)==[-1,0]:blitpos=140*2+self.gets(camera.ctx),160*2
		elif list(mousepos)==[1,0]:blitpos=200*2+self.gets(camera.ctx),160*2
		elif list(mousepos)==[0,1]:blitpos=160*2,200*2+self.gets(camera.cty)
		elif list(mousepos)==[0,-1]:blitpos=160*2,140*2+self.gets(camera.cty)
		t=self.vbuffer;blitpos=list(blitpos);intsound(csound);self.screen.blit(t,(self.gets(camera.ctx),self.gets(camera.cty)))
		for i in ptdraw:
			x=i[0][0]*40+self.gets(camera.ctx);y=i[0][1]*40+self.gets(camera.cty);ent_list=i[1]
			for current_ent in ent_list:self.screen=current_ent.draw(x+int(40*(current_ent.pos[0]%1)),y+int(40*(current_ent.pos[1]%1)),self.screen)
		self.screen.blit(self.playerpreimg,(159*2,159*2));self.screen.blit(self.highlight,blitpos);return blitpos
drawsys=render()
mycam=camera()
rlcam=camera()
cplayer.pos[0]=218
cplayer.pos[1]=21
mycam.tp(218,21)
rlcam.tp(mycam.cx,mycam.cy)
frametime=0
drawsys.screen=pygame.display.set_mode((X,Y))
def gtcpos(t=_B):
	global cplayer,mousepos;rlpos=mousepos
	if not t:return[cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1]]
	else:return[cplayer.pos[0]+8+rlpos[0],cplayer.pos[1]+8+rlpos[1]]
def interact(rlpos=_G):
	global ccmd,cmap,cplayer,mousepos,message,ActionQueue
	if rlpos==_G:
		rlpos=mousepos;t=cmap.gettile(cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1],1)
		if t.name=='vendingmachine':dlgtree.cnpcdial=UIdialogdef.vendingmachinedia(xmap.tiledef.testlist,cplayer.inventory.getcount('coin'))
		if t.interactable:
			res=t.interact(cplayer,cmap)
			if len(res)>0:cplayer=res[0]
			if len(res)>1:cmap=res[1]
			if len(res)>3:t=res[3];cmap.setmap(cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1],t)
			if t.callback(test=1):ActionQueue.append([cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1]])
	else:
		t=cmap.gettile(rlpos[0],rlpos[1],1);t.pos=rlpos
		if t.interactable:
			res=t.callback(cmap,cplayer,test=0)
			if len(res)>0:cmap=res[0]
			if len(res)>1:cplayer=res[1]
			if len(res)>3:t=res[3];cmap.setmap(rlpos[0],rlpos[1],t)
def getmessage():
	global message,cplayer,mousepos,dbbtn;rlpos=mousepos;mg=cmap.gettile(cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1],1);mg2=cmap.gettile(cplayer.pos[0]+rlpos[0],cplayer.pos[1]+rlpos[1],-1)
	try:message=mg.message
	except:io=0
	if hasattr(mg2,'PBA'):
		if mg2.PBA==1:dbbtn.enabled=1
		else:dbbtn.enabled=0
	else:dbbtn.enabled=0;io=0
isinvo=_B
endtime=0
settings=load_data(_E,default_data[_E])
def initsettings():global settings;settings=load_data(_E,default_data[_E]);dlgtree.cnpcdial=UIdialogdef.settingsdia(settings)
def savesettings(x):global settings;print(x);settings=x;save_data(_E,x)
if onweb and settings[4]==0:dlgtree.cnpcdial=dlgtree.UIdialogbase()
dlgtree.cnpcdial.active=1
clock=pygame.time.Clock()
CUSTOM_EVENT=pygame.USEREVENT+1
pygame.time.set_timer(CUSTOM_EVENT,200)
itimeout=0
cplayer.speed=1
cmap.add_entity(cmap.entities[2],(217+8,20+8))
def main():
	E='default';D='blue';C='down';B=1.;A='click';global muted,itimeout,rlcam,clock,cplayer,ccmd,markp,pos1,pos2,selectedt,endtime,isinvo,mycam,drawsys,frametime,cmap,ACTIVEAREA,AREAS,transition,mousepos,pactare,ActionQueue,dlgtree,message;start_time=time.time();cmap.playerpos=[pos+8 for pos in cplayer.pos];mycam.move(cplayer.pos[0],cplayer.pos[1]);mycam.run()
	if onweb:
		if settings[3]==0:muted=1
		else:muted=0
	frametime=frametime+1%120;tiledef.npcdia.quests=tiledef.quests
	if not(isinvo or dlgtree.cnpcdial.active):
		if len(ActionQueue)>0:interact(ActionQueue[0]);del ActionQueue[0]
		if ACTIVEAREA==_C:
			if frametime%2==1:dt=clock.tick(60);start_time=time.time();blitpos=drawsys.renderwmp(mycam,cmap,frametime);ptext.draw(str(message),(blitpos[0],blitpos[1]+20),shadow=(B,B),scolor=D,fontsize=16);ptext.draw(''+str(cplayer.pos[0])+','+str(cplayer.pos[1])+' fps:'+str(1000/dt),(10,0),shadow=(B,B),scolor=D,fontsize=16)
		elif ACTIVEAREA=='ARENA':drawsys.renderarena()
	if isinvo:
		temp=irender(cplayer.inventory.inv);cplayer.inventory.inv=temp[1]
		if temp[0]==1:isinvo=_B
	pokeinteraction=0;pokelevel=0
	if itimeout>0:itimeout=itimeout-1
	if not(isinvo or dlgtree.cnpcdial.active):
		cmap.add_entity(cmap.entities[0],[mycam.ctx+8.5,mycam.cty+8.5])
		for event in pygame.event.get():
			if event.type==pygame.QUIT:pygame.quit()
			if A in intbtn.handleEvent(event)or A in intxbtn.handleEvent(event):interact()
			if A in invbtn.handleEvent(event):isinvo=_A
			if A in svbtn.handleEvent(event):save(E)
			if A in lvbtn.handleEvent(event):load(E)
			if A in settingsbtn.handleEvent(event):initsettings()
			if A in dbbtn.handleEvent(event):
				s=gtcpos(_A);seltile=cmap.heightmap.rmmap(s)
				if hasattr(seltile,'PBA'):
					if seltile.PBA==1:dlgtree.cnpcdial=UIdialogdef.invdia(s[0],s[1])
			keyeventlist=[0,0,0,0]
			if C in leftbtn.handleEvent(event):
				if not itimeout>0:keyeventlist[1]=1;mousepos=[1,0];itimeout=2
			elif C in rightbtn.handleEvent(event):
				if not itimeout>0:keyeventlist[0]=1;mousepos=[-1,0];itimeout=2
			elif C in upbtn.handleEvent(event):
				if not itimeout>0:keyeventlist[2]=1;mousepos=[0,-1];itimeout=2
			elif C in downbtn.handleEvent(event):
				if not itimeout>0:keyeventlist[3]=1;mousepos=[0,1];itimeout=2
			if event.type==pygame.KEYDOWN and ACTIVEAREA==_C and not isinvo:
				cplayer.pos[0]=cplayer.pos[0];cplayer.pos[1]=cplayer.pos[1]
				if event.key==pygame.K_RIGHT:keyeventlist[1]=1;mousepos=[1,0]
				elif event.key==pygame.K_LEFT:keyeventlist[0]=1;mousepos=[-1,0]
				elif event.key==pygame.K_UP:keyeventlist[2]=1;mousepos=[0,-1]
				elif event.key==pygame.K_DOWN:keyeventlist[3]=1;mousepos=[0,1]
				elif event.key==pygame.K_SPACE:interact()
				elif event.key==pygame.K_q:0
				elif event.key==pygame.K_w:keyeventlist[2]=1;mousepos=[0,-1]
				elif event.key==pygame.K_a:keyeventlist[0]=1;mousepos=[-1,0]
				elif event.key==pygame.K_s:keyeventlist[3]=1;mousepos=[0,1]
				elif event.key==pygame.K_d:keyeventlist[1]=1;mousepos=[1,0]
				elif event.key==pygame.K_PAGEDOWN:selectedt+=1;selectedt=selectedt%len(cmap.tiles)
				elif event.key==pygame.K_PAGEUP:selectedt+=-1;selectedt=selectedt%len(cmap.tiles)
				elif event.key==pygame.K_0 and onweb==0:print(str([gtcpos(_A),cmap.tiles[selectedt].name+cmap.tiles[selectedt].__class__.__name__,1])+',',end='');cmap.structuremap.smmap(gtcpos(_A),cmap.tiles[selectedt])
				elif event.key==pygame.K_o and onweb==0:print(str([gtcpos(_A),cmap.tiles[selectedt].name+cmap.tiles[selectedt].__class__.__name__,0])+',',end='');cmap.heightmap.smmap(gtcpos(_A),cmap.tiles[selectedt])
				elif event.key==pygame.K_1 and onweb==0:pos1=gtcpos(_A)
				elif event.key==pygame.K_f and onweb==0:
					for tx in gprt(pos1[0],pos2[0]):
						for ty in gprt(pos1[1],pos2[1]):print(str([[tx,ty],cmap.tiles[selectedt].name+cmap.tiles[selectedt].__class__.__name__,1])+',',end='');cmap.structuremap.smmap([tx,ty],cmap.tiles[selectedt])
				elif event.key==pygame.K_2 and onweb==0:pos2=gtcpos(_A)
				nexttile=0
			if keyeventlist==[1,0,0,0]and ACTIVEAREA==_C:
				if cmap.gettile(cplayer.pos[0]-cplayer.speed,cplayer.pos[1],4)==1:nexttile=cmap.gettile(cplayer.pos[0]-cplayer.speed,cplayer.pos[1],1);cplayer.pos[0]=cplayer.pos[0]-cplayer.speed
			elif keyeventlist==[0,0,1,0]:
				if cmap.gettile(cplayer.pos[0],cplayer.pos[1]-cplayer.speed,4)==1:nexttile=cmap.gettile(cplayer.pos[0],cplayer.pos[1]-cplayer.speed,1);cplayer.pos[1]=cplayer.pos[1]-cplayer.speed
			elif keyeventlist==[0,0,0,1]:
				if cmap.gettile(cplayer.pos[0],cplayer.pos[1]+1,4)==1:nexttile=cmap.gettile(cplayer.pos[0],cplayer.pos[1]+cplayer.speed,1);cplayer.pos[1]=cplayer.pos[1]+cplayer.speed
			elif keyeventlist==[0,1,0,0]:
				if cmap.gettile(cplayer.pos[0]+1,cplayer.pos[1],4)==1:nexttile=cmap.gettile(cplayer.pos[0]+cplayer.speed,cplayer.pos[1],1);cplayer.pos[0]=cplayer.pos[0]+cplayer.speed
	if transition[0]<.5:transition[0]=transition[0]+.01;EM.transition(drawsys.screen,transition[0]);EM.transition(drawsys.screen,transition[0]);ACTIVEAREA=transition[1]
	elif transition[0]<1:
		transition[0]=transition[0]+.01;EM.transition(drawsys.screen,1-transition[0]*2);EM.transition(drawsys.screen,1-transition[0]*2)
		if not ACTIVEAREA in[_M]:ACTIVEAREA=transition[2]
	elif not ACTIVEAREA in[_M]:ACTIVEAREA=transition[2]
	if 0==0:
		if dlgtree.cnpcdial.active:
			if not hasattr(dlgtree.cnpcdial,'runUI'):
				if not dlgtree.cnpcdial.__class__.__name__=='ddialog':dlgtree.cnpcdial=dlgtree.rnbcdialog(dlgtree.cnpcdial)
				else:dlgtree.cnpcdial.active=0
			else:
				dlgtree.cnpcdial.cmap=cmap;dlgtree.cnpcdial.drawsys=drawsys;dlgtree.cnpcdial.cplayer=cplayer
				if dlgtree.cnpcdial.initialised==0:dlgtree.cnpcdial.initialise()
				dlgtree.cnpcdial.runUI();cmap=dlgtree.cnpcdial.cmap;drawsys=dlgtree.cnpcdial.drawsys;cplayer=dlgtree.cnpcdial.cplayer
				if dlgtree.cnpcdial.active==0 and hasattr(dlgtree.cnpcdial,'returndialog'):
					try:dlgtree.cnpcdial=standartUIdialogref.SR[dlgtree.cnpcdial.returndialog]
					except:io=0
				if dlgtree.cnpcdial.active==0 and hasattr(dlgtree.cnpcdial,_E):savesettings(dlgtree.cnpcdial.settings);print('saving data');dlgtree.cnpcdial=dlgtree.ddialog()
	if dlgtree.cnpcdial.active==0:dlgtree.cnpcdial.active==dlgtree.ddialog()
	if not(isinvo or dlgtree.cnpcdial.active):
		pygame.draw.rect(drawsys.screen,(245,235,250),pygame.Rect(scale(320,0,420,320)));teal=.8;tealx=.7;pygame.draw.rect(drawsys.screen,(int(245*teal),int(235*teal),int(250*teal)),pygame.Rect(scale(322,2,418,98)));pygame.draw.rect(drawsys.screen,(int(25*tealx),int(235*tealx),int(29*tealx)),pygame.Rect(scale(322+cplayer.pos[0]*.2,2+cplayer.pos[1]*.2,2,2)))
		if ACTIVEAREA==_C:
			invbtn.draw(drawsys.screen);intbtn.draw(drawsys.screen);svbtn.draw(drawsys.screen);lvbtn.draw(drawsys.screen);dbbtn.draw(drawsys.screen);settingsbtn.draw(drawsys.screen)
			if settings[0]==1:rightbtn.draw(drawsys.screen);leftbtn.draw(drawsys.screen);upbtn.draw(drawsys.screen);downbtn.draw(drawsys.screen);intxbtn.draw(drawsys.screen)
			if onweb==0:drawsys.screen.blit(cmap.tiles[selectedt].gt().gt(),(650,200))
	endtime=time.time()
if __name__=='__main__':import main;mycam.tp(52,13);cplayer.pos=[52,13]