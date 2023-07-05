import ptext
import dialog
import inventory as inv_handle
from inventory import cplayer  , irender
import time
import pygame
from pygamebutton import PygButton
from slider import SliderSwitch
#WTF is wrong with my family
#
#they are legitly arguing about ;
# not opening a bag of food fast enough 
# my mom told my sister to cook some fish sandwhich thingies
#and some bag was not opened soon enough (so dad thought food was not being made )
#
ccredits = {
    "Curt":" \"Characters Zombies and Weapons Oh my \"- resource pack",
    "GrafxKid":"\Gum Bot sprites\"-used for various robot sprites ",
    "the tuxemon project":"inspiration (and also how i found the music for this game)",
    "Olivia,le":"some drawings which have been used to make background for cat characters \n about-me dialog section",
    "AndHeGames":"\"32x32 pixel art creatures volume 3\"- unused , but could be used later  \n(i am not sure if i will end up using them)",
    "Spring Spring":"\"Peasant kingdom\"-used as music in the wild (under cc-by 3.0)",
    "Yubatake":" \"JRPG collection \"-- JRPG_town_loop used for towns ",
    "isaiah658":"\" isaiah658's Pixel Pack #2 \"-some tiles of it are used",
    "Fleurman":"\"Laser Gate\"-used for laser gates",
    "BizmasterStudios":"\" Gold Coin/Token \" -base for coin texture ",
    "Proxy Games":"\" Wooden Crate Texture\"-texture for sound markers ( basically the game switches sound track \n if you see one of these tiles)",
    "chatgtp":"somewhat helping me optimise my code \n(although it is a pain to get it to do what you want)",
    "attribution notice for cc-by 3.0":"https://creativecommons.org/licenses/by/3.0/"
    
    
}
class ddialog():
    def __init__(self):
        self.active = 0
        self.val = 0
class UIdialogbase():
    def __init__(self):
        self.active = 1
        self.val = 0
        self.res = [840,640]
        self.buttons = {}
        self.sliders = []
        self.t=pygame.image.load('Resources/MISC_ASSETS/exitbtn.png')
        self.add_btn("exit","exitbtn",(0.05,0.05),text1=self.t,text2=self.t)
        self.initialised = 0
        self.frametime = 0 
    def scale(self,x,y):
        return [int(x*self.res[0]),int(y*self.res[1])]
    def initialise(self):
        self.add_btn("start game","exitbtn",(0,0.9),(1,0.1))
    def add_slider(self,name,pos,items=["ON","OFF"],size=[80,20],default=0):
        self.sliders.append([name,SliderSwitch(pos,size[0],size[1],items,default),(pos[0]-(len(name)*12)-int(size[0]*0.1)),pos[1]-(int(size[1]*0.4))])
    def add_btn(self,text,name,pos,size=(0.1,0.1),text1=None,text2=None,enabled=1):
        pos = self.scale(pos[0],pos[1])
        size=self.scale(size[0],size[1])
        t= PygButton(caption=text,rect=(pos[0],pos[1],size[0],size[1]),normal=text1,down=text1,highlight=text2)
        t.enabled = enabled
        self.buttons[name] = t 
    def renderframe(self):
        global ccredits
        #self.drawsys.screen
        teal = 0.1
        self.frametime = (self.frametime + 1)%((len(ccredits)*70)/4.5)
        #time.sleep(0.05)
        pygame.draw.rect(self.drawsys.screen, (int(245*teal),int(235*teal),int(250*teal)), pygame.Rect((self.scale(0, 0)+self.scale( 1, 1))))
        ptext.draw( "sorry , for the lack of a good storyline  , \n i am bad at writing good dialog ...", (20,20), color="white",fontsize=32)
        ptext.draw( "thank you to ", (60,100), color="white",fontsize=20)
        indexx = 0
        i = [6,4,7,8,4,5]
        icolors = ["blue","red","black","yellow","gold","silver","green"]
        for key in ccredits:
            name = key
            indexx += 1
            work = ccredits[key]
            ptext.draw( name + " for " + work, (20*i[indexx % 5],140+(((indexx*70))+(self.frametime*4.5) )%(len(ccredits)*70)), color=icolors[indexx%6],fontsize=30)
        #ptext.draw( " ", (30,70), shadow=(1.0,1.0), scolor="gold",fontsize=16)
    #def mouseklick(self,x,y):
        #pass
    def btnp(self,name):
        if name == "exitbtn":
            self.active = 0
    def touch(self,event):
        pass
    def keydown(self,key):
        pass
    def slider(self,name,value):
        pass
    def fill(self,x,y,w,h,bg,screen=None):
        if  screen ==  None:
             pygame.draw.rect(self.drawsys.screen, bg, (x, y, w, h))
        else:
             pygame.draw.rect(screen, bg, (x, y, w, h))
    def string(self,stri,x,y,width=0,color="white",size=16):#(string,x,y)
        ptext.draw(str(stri),pos=(x,y),color=color )
    def runUI(self):
        self.renderframe()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                for i in range(0,len(self.sliders)):
                    slider = self.sliders[i][1]
                    self.slider(self.sliders[i][0],slider.handle_event(event))
                    self.sliders[i][1] = slider
                    
                for key,value in self.buttons.items():
                    t= value.handleEvent(event)
                    #print(t)
                    if "down" in t:
                        self.btnp(key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.touch(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.active = 0
                    self.keydown(event.key)
        for key , value in self.buttons.items():
            value.draw(self.drawsys.screen)
        for i in range(0,len(self.sliders)):
            self.sliders[i][1].draw(self.drawsys.screen)
            ptext.draw(str(self.sliders[i][0]),pos=(self.sliders[i][2],self.sliders[i][3]),color="blue" )
        time.sleep(0.05)
                
                        
                
class nbcdialog():
    def __init__(self,dialog,do=[]):
        self.dialog = dialog
        self.cp = 1
        self.do = do
        self.cdlg = ""
        self.active = 1
        self.val = ""
        self.cs = 0
        self.dac = 0
        self.tlx = []
        self.tlh = []
        for key in self.dialog["1"][1]:
                self.tlx.append(str(key))
                self.tlh.append(self.dialog["1"][1][key])
    def updl(self,i):
                self.tlx =[]
                self.tlh = []
                for key in self.dialog[str(i)][1]:
                    self.tlx.append(str(key))
                    self.tlh.append(self.dialog[str(i)][1][key])


cnpcdial = ddialog()
def rnbcdialog(nbcdialog):## should not be blocking (i hope)
    if nbcdialog.active:
        cdlg = ""
        cp = nbcdialog.cp
        dialogt = nbcdialog.dialog
        #try:
        if True:
            tlx = nbcdialog.tlx
            tlh = nbcdialog.tlh
            
            res = dialog.rndialog(dialogt[str(cp)][0],tlx,nbcdialog.cs,nbcdialog.do)
            if not res[0] == nbcdialog.cs:
                 nbcdialog.cs = res[0]
            if res[1] == False and (not res[0] == None) :
                res = res[0]
            else:
                nbcdialog.cs = res[0]
                del(res)
                del(cdlg)
                return nbcdialog
            if str(tlh[res]) in dialogt:
                cp = tlh[res]
                if not nbcdialog.cp == cp:
                        nbcdialog.cp = cp
                        nbcdialog.updl(str(cp))
                        print("updating list")
            else:
                nbcdialog.val = tlh[res]
                print(tlh[res])
                cdlg ="ex"
        #except:
            #print("not valid dialog",dialogt)
           # nbcdialog.val = 0
           # nbcdialog.active = 0
        if not nbcdialog.cdlg == cdlg:
            nbcdialog.cdlg = cdlg
        if cdlg == "":
            nbcdialog.active = 1
            return nbcdialog
        else:
            nbcdialog.active = 0
            del(res)
            del(cdlg)
            return nbcdialog

# def rdialog(dialogt): ##blocking 
#     cdlg = ""
#     cp = 1
#     while cdlg == "":
#         try:
#             tlx = []
#             tlh = []
#             for key in dialogt[str(cp)][1]:
#                 tlx.append(str(key))
#                 tlh.append(dialogt[str(cp)][1][key])
#             res = dialog.rndialog(dialogt[str(cp)][0],tlx)
#             if type(tlh[res]) is int:
#                 cp = tlh[res]
#                 if cp < 1:
#                     return 0
#                     cdlg ="ex"
#             else:
#                 return tlh[res]
#                 cdlg ="ex"
#         except:
#             print("not valid dialog",dialogt)
#             return 0
#             
        
        
        
        
        
        
        
        

introdialog = {
"1":["   you approach the robot and being by telling it...",{"...who are you ?":2,"...could you please move somewhere else":3,"...have  a nice day (exits dialog)":0}]
,"2":["i am script_kiddi45 \n and  i am here because i need your help.!\n society is collapsing  after a evil hacker \n slowed down the text processors of the other robots \n now they are not able to communicate \n let alone work together in a functioning society \n  . (they could not figure out how to slow down your\n processor since \n it had a different architecture ) and \n i was camouflaged and hiding in the grass  ",{" once you move out of my way i can help you":4," how can i help you ":5,"go away":6,"happens to me every monday":5}]
,"3":["sorry , (moves away) i wanted to tell you ...",{" (listen)":10,"what did you want to tell me ?":2}]
,"10":["... i wanted to tell you that \n my name is script_kiddi45 \n and i am here because i need your help.!\n society is collapsing  after a evil hacker \n slowed down the text processors of the other robots \n now they are not able to communicate \n let alone work together in a functioning society \n  . (they could not figure out how to slow down your \n processor since \n it had a different architecture ) and \n i was camouflaged and hiding in the grass ",{" how can i help you ":5,"go away i do not wish to help you":6,"happens to me every monday":5,"maybe later ":6}]
,"4":["ok (moves away) , if you want more info meet me\n in the town center ",{"sounds good":"mv","will do":"mv","maybe later":"mv"}]
,"5":["Thank you ,\n(note from creator have fun  :D )\n , meet me in the town center for more information",{"ok , i'll explore around for a bit bevore that though .":"mv","sounds great":"mv"}]
,"6":[" if you reconsider you can find\nme in the town center ",{"ok":"mv","have a nice day ":"mv"}]
}

info1dialog = {
"1":["the robot is visibly relived that \n you came to help it",{"ask it what should we do about the evil hacker?":2," well im ready for more info ":2,"i'll be back later":0}]    
,"2":[" well if you can get me 2 copper \n (i recall   copper ore  being  \njust after the stepping stones) \n i would be able to make a terminal so that we can \n override the evil hackers malware \n for the robots in this town  ",{"sure i'll get you 2 copper (accept quest) ":"ac","i'll think about it (leaves dialog)":0}]
}
info2dialoga = {
"1":["thank you , i'll make a firmware patch for the \n other robots right now ",{"need any other help":2,"what do we ought to do next":2}],
"2":["well for one it would be good if you could \n get some of the other robots to help , i'll watch over this town and make sure \n the hacker does not return .",{"will do ":"ac","got it ":"ac"}]
}
info2dialogb = {
"1":[" follow the stepping stones , and then interact with the copper ore ",{"i'll be on my way then":0,"maybe later ":0}]
}
WIDLdialog = {
"1":[" do you want \n to travel to \n dolphin island $WENDY ",{"yes":"idl","maybe later ":0}]    
}
FIDLdialog = {
"1":[" do you want \n to travel to \n Wahu island $FEI ",{"yes":"idl","maybe later ":0}]    
}
WRTTdialog = {
"1":[" do you want \n to return to \n Uwofei island $WENDY ",{"yes":"idl","maybe later ":0}]    
}
FRTTdialog = {
"1":[" do you want \n to return to \n dolphin island $FEI ",{"yes":"idl","maybe later ":0}]    
}
info3dialog = {
"1":["hi what do you want ",{"tell me a story of a land far away":2,"how are you ":6,"can you give me a summary of why i am here":3,"have a good day :D":4,"nice to see you again":5," bye":0}],
"2":["sure \n"]
}
