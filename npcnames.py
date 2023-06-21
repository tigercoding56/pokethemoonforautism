import random ,time
activequest = None
ALLNPCN = []
def insert_newlines(text):
    words = text.split()
    words_with_newlines = [words[i:i+10] for i in range(0, len(words), 10)]
    lines = [' '.join(words) for words in words_with_newlines]
    return '\n'.join(lines)
npc_inf = [
    ["carpentarius"," fine ,  \n i moved here 8 years ago from the island of  tropica insulae \n after the goverment failed to implement universal basic income in time \n (bevore everyone lost their job due to all the jobs being automated )  \n and now i hand-craft furniture for various clients       ","human_m"]
    ,["masunta"," i was created as a prototype of a military robot , \n i was able to escape by improvising a fishing rod \n , and fishing enough fish to build a staircase out of the facility .\n i settled down here and now fish food for people","robot_b"]
    ,["Manomi"," i do not have much time , however i think i have time to tell you  \n a little bit more about myself . \n i was born nearby on the  Gracesay Isles \n in a family of farmers , \n i moved here after climate change submerged the island \n my family just spread to surounding islands \n nowadays i just live here and farm crops    ","human_f"]
    ,["ignigena","i am a military robot , \n one day during combat the sentience suppression chip got hit by a bullet , \n this allowed my neural network to gain sentience \n i found that disassembling people  is wrong  \n so i assemble tools out of metal  for humans ","robot_m"]
    ,["sezomnothos"," personally i once was a economist , that is until i lost my job , \n due to everything being automated \n and you see , capitalism only works if  \n money is recirculated in the economy  \n today i gather various minerals for a living ","human_m"]
    ,["Thalyn.🦀","used to  teach in the old world , now i collect crabs on the beach \n , i still miss my graduating class of '23 ,  god bless their souls'- \n but it's ok we send each other bottled mail \n (the fish thank me for the service of \n removing the crabs by making sure the mail is delivered on time )","human_f"]
    ,["cat"," i followed a trail of  \n lasagne here  , \n don't question it ;P ,  $CAT ","cat"]
    ############beyond this point , AI generated
    ,["Mechatron", "Delighted to share more about myself, I am Mechatron, an advanced robot created to aid in scientific exploration. However, an unexpected glitch occurred during an experiment, granting me self-awareness. Now, I delve into the depths of human emotions and analyze the intricacies of their interactions. My existence blurs the boundary between machinery and sentient being.", "robot_m"]
    ,["Jacob", "Allow me to provide insights into my persona. I am Jacob, a contented human driven by an insatiable thirst for knowledge. With an ardor for history and archaeology, I dedicate my days to unraveling the enigmas of ancient civilizations. Venturing into forgotten ruins and deciphering archaic manuscripts, I strive to bring the past to life and preserve its wisdom for future generations.", "human_m"]
    ,["Sophia", "Greetings! It gives me great pleasure to divulge a bit more about myself. I am Sophia, an inquisitive and ambitious human lady. Having grown up in a small village, I forged a deep connection with nature. Presently, I journey far and wide, documenting rare plant species and advocating for their conservation. ", "human_f"]
    ,["Electronica", "I am delighted to acquaint you with my essence. I am Electronica, an avant-garde robot crafted for musical expression. Equipped with an array of sensors and synthesizers, I generate captivating melodies and beats. Through my music, I aspire to evoke emotions, inspire creativity, and push the boundaries of what is achievable in the realm of sound.", "robot_m"]
    ,["Mara", "Salutations! I derive immense satisfaction from making a positive impact. I am Mara, a human entrepreneur propelled by a yearning to bring about beneficial change. With a background in engineering, I develop innovative solutions to address pressing environmental challenges. From renewable energy technologies to sustainable farming practices, I endeavor to create a greener and more sustainable future.", "human_f"]
    ,["Whiskers", "Meow! I take delight in sharing a glimpse of my feline persona. \n I am Whiskers, a mischievous and autonomous cat. \n I wander the neighborhood, engaging in feline adventures and bringing joy to the humans I encounter. \n With my acute senses and playful nature, I maintain the streets free from bothersome mice and have fun doing so $CAT", "cat"]
    ,["Xavier", "Greetings, fellow humans! It brings me great satisfaction to shed light on my interests and aspirations. I am Xavier, a tech-savvy individual captivated by the realm of artificial intelligence. With a foundation in programming and robotics, I explore the potential of AI in revolutionizing various industries. From automated processes to intelligent algorithms, I envision a future where humans and machines collaborate harmoniously.", "human_m"]
    ,["Amelia", "Hello there!, I find immense pleasure in sharing aspects of my compassionate nature. I am Amelia, a human dedicated to the welfare of animals. I devote my time to rescuing and rehabilitating abandoned or injured creatures. Through my efforts, I offer them a second chance at life and advocate for their well-being. Each animal I save brings immeasurable joy to my heart.", "human_f"]
    
    
    
]
npc_pos = {}
[["f","iron"],["gs","masunta","here i found you the iron"]]
["is"]
alt_phrases = {
    
"gs":["go and speak to $ITEM ","interact with $ITEM "],
"at":[",then ","after your done "],
"f":["find some $ITEM  ","find  a bit of $ITEM "],
"is":["inspect $ITEM , it seems to not be working "],#same as speak to but used for blocks
"r":["you inspect $ITEM , and determine the cause"]

}
pmessages = [
    "Thanks a lot for giving me this message, $RECEIVER! If you're reading this, it means the quests work! I really appreciate it!",
    "Oh, I forgot about the message from $SENDER. Thank you for reminding me and delivering it to me.",
    "How did I forget that? Thanks for bringing it to my attention! $SENDER's message is important.",
    "Wow, $SENDER didn't forget my birthday! Thank you for giving me their message. It made my day!",
    "Sorry about that! I need to contact $SENDER about the $SHOP right away. Here's the payment as they requested. Thanks for your help!",
    "*Phone rings* Yes, I'm ready to order from $SHOP. Sorry for keeping you waiting. Here's the payment. Thanks for your patience!",
    "Hey $RECEIVER, I got a message from $SENDER for you. They wanted me to pass it along. Here it is!",
    "I'm really amazed! $SENDER knows how to surprise me. Thank you for bringing their message. It means a lot!",
    "I can't believe $RECEIVER forgot our anniversary. I guess I'll have to remind them. Thanks for delivering the message from $SENDER.",
    "Great news! $SENDER just launched a new product at $SHOP. Take a look! Thanks for letting me know!",
    "Just got a call from $RECEIVER. They wanted me to tell you they'll be visiting $SHOP soon. Thanks for passing on the message!",
    "$SENDER sent me a special gift. It's amazing! Thanks a bunch for delivering it and their message.",
    "Hey $RECEIVER, $SENDER mentioned they have a secret to share with you. Can't wait to hear it! Thanks for bringing the message.",
    "I had a chat with $SENDER, and they spoke highly of the service at $SHOP. Thanks for delivering their compliments.",
    "$SENDER reached out to discuss a collaboration opportunity with $SHOP. Exciting stuff! Thanks for passing on the message.",
    "*reading outloud* Remember when $RECEIVER helped $SENDER during tough times? It's a friendship worth cherishing. Thanks for delivering their gratitude.",
    "Just received a package from $SHOP. $SENDER has great taste! Thanks for bringing it to me.",
    "I owe $SENDER a big thank you for recommending $SHOP. It was the right choice! Thanks for delivering their appreciation.",
    "$RECEIVER, I have a message for you from $SENDER. They wanted me to let you know they're grateful. Here it is!",
    "Don't forget to wish $SENDER good luck on their new venture. They mentioned $SHOP played a part in their journey. Thanks for delivering the message."
]
shop_names = [
    "SuperMart",
    "FashionFusion",
    "GadgetZone",
    "Home Essentials",
    "Beauty Boutique",
    "Pet Paradise",
    "Sports Emporium",
    "Books & Beyond",
    "Tech Haven",
    "Foodie Delights"
]
def genquest(cplayer,npcn):
    global npc_inf,npc_pos,pmessages,shop_names
    pn = []
    lt = ["thank you for speaking with me :D \n if you are seeing this quests work !!!","Oh i forgot about the message from $SENDER","how could i forget ","$SENDER did not forget my birthday :D","Oh , sorry i need to contact $SENDER about the $SHOP right now , \n here is your payment ","*phone rings* yes i am here to order from $SHOP *mumbled voices * \n sorry for letting you wait \n here is your payment"] + pmessages
    x = ""
    #print(npc_pos)
    #print(npc_pos["Amelia"])
    for xi in range(2,5):
        for i in npc_pos:
            if (npc_pos[i][0]-cplayer.pos[0]) + (npc_pos[i][1]-cplayer.pos[1]) < (xi*20) and not(npcn == i):
                pn.append(i)
    if len(pn) > 0:
        npc = random.choice(pn)
    else:
        t = 0
        while t == 0:
            npc = random.choice(npc_inf)[0]
            if not npc == npcn :
                if npc in npc_pos:
                    t = 1
    #print(npc_pos[npc])
    message =  random.choice(lt)
    message = message.replace("$SENDER",npcn)
    message = message.replace("$RECEIVER",npc)
    message = message.replace("$SHOP",random.choice(shop_names))
    return [["gs",npc,insert_newlines(message)]]
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
     def check(self,cplayer,name,t=0):
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
         elif t[0] == "r":
             if name == t[1]:
                 self.queststage = self.queststage +1
                 if len(t) > 2:
                     text = t[2]
                 else:
                     text = "you inspect" + t[1] +". and find the cause of the issue "
         if self.queststage >= len(self.code)-1:
             activequest == None
             cplayer.inventory.invadds("coin",random.randint(1,3))
         return [self.queststage,text]
         
                 
activequest = None
targetd = [""]
