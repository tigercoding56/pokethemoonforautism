import random ,time
random.seed(time)
activequest = None
ALLNPCN = []
npc_inf = [
    ["carpentarius"," fine ,  \n i moved here 8 years ago from the island of  tropica insulae \n after the goverment failed to implement universal basic income in time \n (bevore everyone lost their job due to all the jobs being automated )  \n and now i hand-craft furniture for various clients       ","human_m"]
    ,["masunta"," i was created as a prototype of a military robot , \n i was able to escape by improvising a fishing rod \n , and fishing enough fish to build a staircase out of the facility .\n i settled down here and now fish food for people","robot_b"]
    ,["Manomi"," i do not have much time , however i think i have time to tell you  \n a little bit more about myself . \n i was born nearby on the  Gracesay Isles \n in a family of farmers , \n i moved here after climate change submerged the island \n my family just spread to surounding islands \n nowadays i just live here and farm crops    ","human_f"]
    ,["ignigena","i am a military robot , \n one day during combat the sentience suppression chip got hit by a bullet , \n this allowed my neural network to gain sentience \n i found that disassembling people  is wrong  \n so i assemble tools out of metal  for humans ","robot_m"]
    ,["sezomnothos"," personally i once was a economist , that is until i lost my job , \n due to everything being automated \n and you see , capitalism only works if  \n money is recirculated in the economy  \n today i gather various minerals for a living ","human_m"]
    ,["Thalyn.🦀","used to  teach in the old world , now i collect crabs on the beach \n , i still miss my graduating class of '23 ,  god bless their souls'- \n but it's ok we send each other bottled mail \n (the fish thank me for the service of \n removing the crabs by making sure the mail is delivered on time )","human_f"]
    ,["cat"," i followed a trail of  \n lasagne here  , \n don't question it ;P ,  $CAT ","cat"]
    
    
    
    
]
[["f","iron"],["gs","masunta","here i found you the iron"]]
alt_phrases = {
    
"gs":["go and speak to $ITEM ","interact with $ITEM "],
"at":[",then ","after your done "],
"f":["find some $ITEM  ","find  a bit of $ITEM "],
"is":["inspect $ITEM , it seems to not be working "]#same as speak to but used for blocks 

}
def genquest():
    global npc_inf
    return [["gs",random.choice(npc_inf)[0],"thank you for speaking with me :D \n if you are seeing this quests work !!!"]]
class quest():
     def __init__(self,code):
        global alt_phrases
        self.code = code
        self.done = 0
        self.desc  = ""
        self.queststage = 0
        for x in range(0,len(self.code)) :
            i = self.code[x]
            nxita = random.choice(alt_phrases[i[0]])
            nxita = nxita.replace("$ITEM",i[1])
            if x < (len(self.code) -1):
                if self.code[x+1][0] == "gs" and i[0] == "f":
                    nxita += " (make sure to keep " + i[1] +") then"
                else:
                    nxita += random.choice(alt_phrases["at"])
                
            self.desc = self.desc + nxita
     def check(self,cplayer,name):
         global activequest
         try:
             t = self.code[self.queststage]
         except:
            activequest == None
            self.done = 1
            return [len(self.code),""]
         #invcheck(self,ist,rm=0,tm=1)
         text = ""
         if t[0] == "f":
             if len(self.code) -1 > self.queststage:
                 x = self.code[self.queststage]
                 if x[0] == "gs":
                     if name == x[1]:
                         if cplayer.inventory.invcheck(t[1],1):
                             self.queststage = self.queststage +2
                             if len(x) > 2:
                                 text = x[2]
                             else:
                                 text = "thank you  for the " + t[1]
                         else:
                             text = "you do not have enough " + t[1]
                 else:
                      if cplayer.inventory.invcheck(t[1],1):
                            self.queststage = self.queststage +1
                            txt = ""
             else:
                 if cplayer.inventory.invcheck(t[1],1):
                            self.queststage = self.queststage +1
                            txt = ""
         elif t[0] == "gs" or t[0] == "is":
             if name ==  t[1]:
                 self.queststage = self.queststage +1
                 if len(t) > 2:
                     text = t[2]
         if self.queststage >= len(self.code)-1:
             activequest == None
         return [self.queststage,text]
         
                 
activequest = None
targetd = [""]