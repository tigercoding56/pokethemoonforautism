
import dialog
import time
class ddialog():
    def __init__(self):
        self.active = 0
class nbcdialog():
    def __init__(self,dialog):
        self.dialog = dialog
        self.cp = 1
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
            
            res = dialog.rndialog(dialogt[str(cp)][0],tlx,nbcdialog.cs)
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
"1":[" you approach the robot and being by telling it...",{"...who are you ?":2,"...could you please move somewhere else":3,"...have  a nice day (exits dialog)":0}]
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
info3dialog = {
"1":["hi what do you want ",{"tell me a story of a land far away":2,"how are you ":6,"can you give me a summary of why i am here":3,"have a good day :D":4,"nice to see you again":5," bye":0}],
"2":["sure \n"]
}
