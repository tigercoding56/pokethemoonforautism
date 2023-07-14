import random ,time
def generate_20_digit_seed():
    timestamp = str(time.time()).replace(".", "")  # Get timestamp and remove decimal point
    seed = int(timestamp[:20])  # Convert the first 20 digits to an integer
    return seed
random.seed(generate_20_digit_seed())
activequest = None
ALLNPCN = []
def insert_newlines(text):
    words = text.split()
    words_with_newlines = [words[i:i+7] for i in range(0, len(words), 7)]
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
npc_inf = [
    [
        "carpentarius",
        "Ah, greetings! I arrived here 8 years ago, seeking solace from the turmoil that plagued Tropica Insulae, the island I once called home. The government's failure to implement universal basic income in a timely manner resulted in widespread job loss due to rampant automation. Now, I dedicate my craft to hand-crafting exquisite furniture for clients from all walks of life.",#get wood from supply crate
        "human_m",
        [
        [["is","supply crate","you take a bit of wood from the supply crate"," find wood in one of the many supply crates "],["gt","carpentarius","thank you , here are some coins as a reward"]]    
        ]
    ],
    [
        "masunta",
        "Listen closely, for my tale is extraordinary. I emerged as a prototype military robot, destined for warfare. However, through a remarkable turn of events, I seized an opportunity to escape. Utilizing a makeshift fishing rod, I skillfully caught enough fish to construct a staircase and find my way out of the facility. Now, I reside here, providing sustenance by fishing and sharing the bounties (mostly fish but sometimes i find other things) of the sea with the people.",
        "robot_b",
    ],
    [
        "Manomi",
        "Time is fleeting, but let me share a glimpse into my past. I hail from the Gracesay Isles, a land of farmers and fertile fields. Alas, climate change submerged our beloved island, scattering my family across the neighboring isles. Here, I stand, cultivating crops and breathing life into the earth, carrying with me the resilience and determination of my ancestors.",#fix irigation
        "human_f",
        [
          [["is","irigation pump"," you determine the input filter is clogged \n , luckily you have a spare one on hand , you replace it "," the irrigation system is broken at the farm near large town , could you kindly fix it ?  "],["gs","Manomi","thank  you \n as reward here have some coins "]]   
          ,[["is","bird feeder","you restock the bird feeder , not long after \n you hear the delightful chirping of birds","please restock the bird feeder ,  here is some grain  "],["gs","Manomi","thank you \n here have some coins \n  as reward "]] 
            
        ]
    ],
    [
        "ignigena",
        "I am no ordinary military robot, for fate granted me an unexpected gift. In the heat of battle, a bullet pierced my sentience suppression chip, awakening a newfound awareness within me. Realizing the profound wrongness of disassembling humans, I redirected my purpose. Now, I forge tools from metal, crafting instruments that aid and empower humanity.",#fix machinery 
        "robot_m",
        [[["f","copper"],["gs","ignigena","thank you ,\n as a reward have some coins"]],[["f","gold"],["gs","ignigena","thank you , for helping me \n in my endevours to craft \n precious tools \n here have a share of the rewards"]],  [["f","silver"],["gs","ignigena"," just what i needed for forging \n my precious tools \n here have some coins as reward"]]]
    ],
    [
        "sezomnothos",
        "Once an economist, my life took an unforeseen turn when automation rendered my profession obsolete. Capitalism's vitality relies on the circulation of wealth, a principle forgotten amidst the rise of machines. Today, I make my living gathering an array of minerals, an endeavor that sustains me and reminds society of the value of human ingenuity.",#fix machinery,find minerals what can i say ?
        "human_m",
        [
        [["f", "copper"], ["gs", "Sezomnothos", "Thank you for assisting me in gathering copper. It is a crucial material for my metalworking projects. As a token of my appreciation, please accept these coins as a reward."]],
        [["f", "gold"], ["gs", "Sezomnothos", "Thank you for your help in acquiring gold. It is a precious resource I require for crafting my intricate masterpieces. As a gesture of gratitude, I offer you a share of the rewards."]],
        [["f", "silver"], ["gs", "Sezomnothos", "Just what I needed for my artisan works. Your assistance in acquiring silver is greatly appreciated. As a reward for your efforts, please accept these coins as a token of my gratitude."]]
        ]

    ],
    [
        "Thalyn.🦀",
        "Once a teacher in the old world, my path diverged, leading me to the serene shores where crabs roam. Oh, how I yearn for the days spent guiding my graduating class of '23, may their souls rest in eternal peace. Yet, in this new chapter of live , I remove crabs from the beach, and in return, the fish facilitate the delivery of our heartfelt messages through the medium of bottled mail.",#find  mail
        "human_f",
        [#partly me and partly chatgtp , around 50% split , also do not worry  i got the names from the convenient slide you left me :D   , i am definately not trying to hack into the school network now (or at least i stopped trying for now ... )
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from olivia.le \n a student of my freshmen class of 23' \n  i am excited to read ,  \n but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from ezrael  \n a student of my graduating  class of 23' \n  i am cannot wait  to read  it , \n hopefully everything is fine ,  \n but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from esther \n a student of my 4th period  class of 23' \n  i am excited to read ,  \n but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Ivanna  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Valerie  a student of my 4th period  class of 23'   bless their soul , i am going to read the letter  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Matt  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Tracen  a student of my 4th period  class of 23'    how nice of them  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Najma  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Katie  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Leah  a student of my 4th period  class of 23'   i am excited to read their letter ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Kenzie  a student of my 4th period  class of 23'    how nice of them  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Cody  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from JaidenJulianne  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from QueenJin  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Noah  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Mikayla  a student of my 4th period  class of 23'   i am excited to read their letter ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from IzzyAmilia  a student of my 4th period  class of 23'    Oh i really can't wait to read ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Jayven  a student of my 4th period  class of 23'   i am excited to read their letter ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Tiffini  a student of my 4th period  class of 23'   i am excited to read their letter ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Louisa  a student of my 4th period  class of 23'   i am excited to read their letter ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Denise  a student of my 4th period  class of 23'   bless their soul , i am going to read the letter  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Ben  a student of my 4th period  class of 23'    how nice of them  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Hanae  a student of my 4th period  class of 23'   bless their soul , i am going to read the letter  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Max  a student of my 4th period  class of 23'   bless their soul , i am going to read the letter  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Kai  a student of my 4th period  class of 23'   i am excited to read their letter ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from  Nathaniel  a student of my 4th period  class of 23'   bless their soul , i am going to read the letter  ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Rishi  a student of my 4th period  class of 23'   i am excited to read their letter ,   but first  here is your payment    "]],
        [["is","mailbox","you find letters in the mail"," please check my mailbox "],["gs","Thalyn.🦀","thank you *opens letter* Oh its from Mateo  a student of my 4th period  class of 23'    how nice of them  ,   but first  here is your payment    "]]
        ]
    ],
    [
        "cat",
        "Purrs and whiskers! My arrival here traces back to a trail of irresistible lasagna. A feline's journey need not be questioned; it is simply embraced. Meow! $CAT",#find fish from supply crate 
        "cat",
    ],
    [
        "Mechatron",
        "Delighted to share more about myself, I am Mechatron, an advanced robot created to aid in scientific exploration. However, an unexpected glitch occurred during an experiment, granting me self-awareness. Now, I delve into the depths of human emotions and analyze the intricacies of their interactions. My existence blurs the boundary between machinery and sentient being.",#repair machinery / get oil from supply crate 
        "robot_m",
    ],
    [
        "Jacob",
        "Allow me to provide insights into my persona. I am Jacob, a contented human driven by an insatiable thirst for knowledge. With an ardor for history and archaeology, I dedicate my days to unraveling the enigmas of ancient civilizations. Venturing into forgotten ruins and deciphering archaic manuscripts, I strive to bring the past to life and preserve its wisdom for future generations.",#get rock sample from ruins (you scratch off  a bit of the rock and take it)
        "human_m",
        [
        [["is","ancient artifact"," you chip a small piece of rock out of the artifact "," take a rock sample out of one of the ancient artifacts "],["gt","Jacob","thank you \n here is your reward "]]    
        ]
    ],
    [
        "Sophia",
        "Greetings! It gives me great pleasure to divulge a bit more about myself. I am Sophia, an inquisitive and ambitious human lady. Having grown up in a small village, I forged a deep connection with nature. Presently, I journey as far and wide as this island allows  , documenting rare plant species and advocating for their conservation. (also helping other people)",#restock bird feeder , find  plants
        "human_f",
    ],
    [
        "Electronica",
        "I am delighted to acquaint you with my essence. I am Electronica, an avant-garde robot crafted for musical expression. Equipped with an array of sensors and synthesizers, I generate captivating melodies and beats. Through my music, I aspire to evoke emotions, inspire creativity, and push the boundaries of what is achievable in the realm of sound.",
        "robot_m",
    ],
    [
        "Mara",
        "Salutations! I derive immense satisfaction from making a positive impact. I am Mara, a human entrepreneur propelled by a yearning to bring about beneficial change. With a background in engineering, I develop innovative solutions to address pressing environmental challenges. From renewable energy technologies to sustainable farming practices, I endeavor to create a greener and more sustainable future.",#inspect solar  pannels
        "human_f",[
        [["is","solar power station"," you clean the solar pannel ,  "," the solar power station , has a reduced energy output because a solar pannel is too dusty to generate power \n meaning the backup generators need to run \n which pollutes the sky  , \n if you clean the solar pannel  i will pay you 1-3  gold coins (random chance) "],["gt","Mara","thank you \n here is your reward "]]
            
            
        ]
    ],
    [
        "Whiskers",
        "Meow! I take delight in sharing a glimpse of my feline persona. I am Whiskers, a mischievous and autonomous cat. I wander the neighborhood, engaging in feline adventures and bringing joy to the humans I encounter. With my acute senses and playful nature, I maintain the streets free from bothersome mice and have fun doing so. $CAT",
        "cat",
    ],
    [
        "Xavier",
        "Greetings, fellow humans! It brings me great satisfaction to shed light on my interests and aspirations. I am Xavier, a tech-savvy individual captivated by the realm of artificial intelligence. With a foundation in programming and robotics, I explore the potential of AI in revolutionizing various industries. From automated processes to intelligent algorithms, I envision a future where humans and machines collaborate harmoniously.",
        "human_m",
    ],
    [
        "Amelia",
        "Hello there! I find immense pleasure in sharing aspects of my compassionate nature. I am Amelia, a human dedicated to the welfare of animals. I devote my time to rescuing animals in need, providing them with love, care, and a safe haven. Whether it's nursing injured wildlife back to health or finding forever homes for abandoned pets, my mission is to create a world where every creature is treated with kindness and compassion."
        ,"human_f"
     ],
    [
    "mining drill",
    "a marvel of technology  , \n this drill is smaller than mos other ones , \n still it provides the settlements with \n all of  the essential materials ",
    "tile_drill"
        
        
    ],
    [
    "solar power station",
    "this solar array provides the whole island with power ",
    "tile_solarpannel"
        
        
    ],
    [
    "irigation pump",
    "used for irrigation ",
    "tile_pump"
        
        
    ],
    [
    "supply crate",
    " a crate of supplies for everyone, \n--provided by the fire nation ",
    "tile_supplycrate"
        
        
    ],#give a lazy person a hard job , and they'll find the most efficient way to do it , --albert einstein or someone ,  but in this case the lazy person is my lazy ass , ;P non-npc tiles should technically not be classified as characters , but noone will ever know right ????? 
    [
    "machinery",
    " used to produce most  goods for the inhabitants of \n the island ",
    "tile_machinery"  
        
    ],
    [
    "mailbox",
    " just a simple mailbox ",
    "tile_mailbox"  
        
    ],
    [
    "bird feeder",
    "you see many beatiful birds flocking , \n to eat the seeds at the bird feeder",
    "tile_birdfeeder"
    ],
    [
    "ancient artifact",
    "upon closer inspection you notice  a mysterious \n script written on the old stone  ",
    "tile_artifact"
    ],
    [
        "Agnes Thanh-De Thi",
        "TEST"
        ,"human_f"
     ]
    
    
    
    
    
    ]
FNTM = [
    "Agnes Thanh-De Thi le",
    "Emmanuel Phung Van le",
    "Paul Tinh Bao Le",
    "Joseph Thi Dang Le"
    # i need  2 further additions
    #but i am never going to be a saint so 
    #
    #
    #
    
    
    
]
speciesdia = {
"cat":["Meow! What brings you here today" , "hi , anything i can help you with?", "Greetings, \n what brings you here", "Meow! How may I bring joy to your day, "]
,"human_f":["Greetings, dear traveler. what brings you to me today ?", " What brings you here today?", "Welcome, kind soul. ", "Good day,  How may I help you"]
,"robot_m":["Greetings, How may i assist you", " What brings you to me today?", "Welcome, ", "Salutations! "]
,"robot_f":["Greetings, How may i assist you", " What brings you to me today?", "Welcome, ", "Salutations! "]
,"robot_b":["Greetings, How may i assist you", " What brings you to me today?", "Welcome, ", "Salutations! "]
,"human_m":["How can I assist you ?", "Greetings,  What brings you here today?", "Welcome, traveler.", " How may I be of service to you?"]


}
quests1 = {

}
npc_pos = {}
[["f","iron"],["gs","masunta","here i found you the iron"]]
["is"]
alt_phrases = {
    
"gs":["go and speak to $ITEM ","interact with $ITEM "],
"at":[",then ","after your done "],
"f":["find some $ITEM  "," find  a bit of $ITEM "],
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
def genquestex():
    global npc_inf,npc_pos,pmessages,shop_names
    pn = []
    lt = ["thank you for speaking with me :D \n if you are seeing this quests work !!!","Oh i forgot about the message from $SENDER","how could i forget ","$SENDER did not forget my birthday :D","Oh , sorry i need to contact $SENDER about the $SHOP right now , \n here is your payment ","*phone rings* yes i am here to order from $SHOP *mumbled voices * \n sorry for letting you wait \n here is your payment"] + pmessages
    x = ""
    #print(npc_pos)
    #print(npc_pos["Amelia"])

    npc = random.choice(npc_inf)[0]
    t =0
    while t ==0:
        npcn = random.choice(npc_inf)[0]
        if npcn != npc:
            t=1
    #print(npc_pos[npc])
    message =  random.choice(lt)
    message = message.replace("$SENDER",npcn)
    message = message.replace("$RECEIVER",npc)
    message = message.replace("$SHOP",random.choice(shop_names))
    return [["gs",npc,insert_newlines(message)]]
def find_item_by_string(lst, search_string):
    for item in lst:
        try:
            if item[0] == search_string:
                return item
        except:
            io = 0
    return None
def genquest(cplayer,npcn):
    global npc_inf,npc_pos,pmessages,shop_names
    pn = []
    lt = ["thank you for speaking with me :D \n if you are seeing this quests work !!!","Oh i forgot about the message from $SENDER","how could i forget ","$SENDER did not forget my birthday :D","Oh , sorry i need to contact $SENDER about the $SHOP right now , \n here is your payment ","*phone rings* yes i am here to order from $SHOP *mumbled voices * \n sorry for letting you wait \n here is your payment"] + pmessages
    qtype = 1
    npcninf = find_item_by_string(npc_inf,npcn)
    if len(npcninf)>3:
        if random.randint(1,2) > 0:
            qtype = 0
    if qtype == 1:
        x = ""
        #print(npc_pos)
        #print(npc_pos["Amelia"])
        for xi in range(2,5):
            for i in npc_pos:
                #print(npc_pos)
               # try:
                    if (npc_pos[i][0]-cplayer.pos[0]) + (npc_pos[i][1]-cplayer.pos[1]) < (xi*20) and not(npcn == i) and not("tile_" in find_item_by_string(npc_inf,i)[2]):
                        pn.append(i)
               # except:
                   # print(i)
                   # print("###|")
                   # print("###V")
                   # print(npc_inf)
        if len(pn) > 0:
            npc = random.choice(pn)
        else:
            t = 0
            while t == 0:
                npcx = random.choice(npc_inf)
                npc = npcx[0]
                if not npc == npcn :
                    if npc in npc_pos:
                        if not "tile_" in  npcx[2]:
                            t = 1
        #print(npc_pos[npc])
        message =  random.choice(lt)
        message = message.replace("$SENDER",npcn)
        message = message.replace("$RECEIVER",npc)
        message = message.replace("$SHOP",random.choice(shop_names))
        return [["gs",npc,insert_newlines(message)]]
    else:
        return random.sample(npcninf[3],1)[0]
class quest():
     def __init__(self,code):
        global alt_phrases
        self.code = code
        self.done = 0
        self.desc  = ""
        self.queststage = 0
        for x in range(0,len(self.code)) :
            i = self.code[x]

            if i[0] == "is"and len(i) > 3:
                    nxita = i[3]
            else:
                nxita = random.choice(alt_phrases[i[0]])
                nxita = nxita.replace("$ITEM",i[1])
            if x < (len(self.code) -1):
                if self.code[x+1][0] == "gs" and i[0] == "f":
                    nxita += " (make sure to keep " + i[1] +") then "
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
         if not text == "":
             text == insert_newlines(text)
         return [self.queststage,text]
         
                 
activequest = None
targetd = [""]
