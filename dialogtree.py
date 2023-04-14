
import dialog
import asyncio
import time

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


cnpcdial = None
def rnbcdialog(nbcdialog):## should not be blocking (i hope)
    if nbcdialog.active == True:
        cdlg = nbcdialog.cdlg
        cp = nbcdialog.cp
        dialogt = nbcdialog.dialog
        try:
            tlx = nbcdialog.tlx
            tlh = nbcdialog.tlh
            
            res = dialog.rndialog(dialogt[str(cp)][0],tlx,nbcdialog.cs)
            if res[1] == False:
                res = res[0]
            else:
                nbcdialog.cs = res[0]
                return nbcdialog
            if type(tlh[res]) is int:
                cp = tlh[res]
                if cp < 1:
                    nbcdialog.val = 0
                    cdlg ="ex"
            else:
                nbcdialog.val = tlh[res]
                cdlg ="ex"
        except:
            print("not valid dialog",dialogt)
            nbcdialog.val = 0
        if not nbcdialog.cp == cp:
            nbcdialog.cp = cp
            nbcdialog.updl(cp)
        if not nbcdialog.cdlg == cdlg:
            nbcdialog.cdlg = cdlg
        if cdlg == "":
            nbcdialog.active = 1
            return nbcdialog
        else:
            nbcdialog.active = 0
            return nbcdialog

def rdialog(dialogt): ##blocking 
    cdlg = ""
    cp = 1
    while cdlg == "":
        asyncio.sleep(0)
        try:
            tlx = []
            tlh = []
            for key in dialogt[str(cp)][1]:
                tlx.append(str(key))
                tlh.append(dialogt[str(cp)][1][key])
            res = dialog.rndialog(dialogt[str(cp)][0],tlx)
            if type(tlh[res]) is int:
                cp = tlh[res]
                if cp < 1:
                    return 0
                    cdlg ="ex"
            else:
                return tlh[res]
                cdlg ="ex"
        except:
            print("not valid dialog",dialogt)
            return 0
            
        
        
        
        
        
        
        
        

introdialog = {
"1":[" you approach the robot and being by telling it...",{"...who are you ?":2,"...could you please move somewhere else":3,"...have  a nice day (exits dialog)":0}]
,"2":["i am script_kiddi45 \n and i am here because i need your help.!\n the animals in this area where friendly ... \n but then i messed up my code \n and now they are hostile .  ",{" once you move out of my way i can help you":4," how can i help you ":5,"go away":6,"happens to me every monday":5}]
,"3":["sorry , (moves away) i wanted to tell you ...",{" (listen)":10,"what did you want to tell me ?":2}]
,"10":["... i wanted to tell you that \n my name is script_kiddi45 \n and i am here because i need your help.!\n the animals in this area where friendly ... \n but then i messed up my code \n and now they are hostile .  ",{" how can i help you ":5,"go away i do not wish to help you":6,"happens to me every monday":5,"maybe later ":6}]
,"4":["ok (moves away) , if you want more info meet me in the town center ",{"sounds good":"mv","will do":"mv","maybe later":"mv"}]
,"5":["Thank you ,\n(note from creator have fun  :D ) , meet me in the town center for more information",{"ok , i'll explore around for a bit bevore that though .":"mv","sounds great":"mv"}]
,"6":[" if you reconsider you can find me in the town center ",{"ok":"mv","have a nice day ":"mv"}]
}



