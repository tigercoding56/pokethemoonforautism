import datetime
messages = [ ## most of the the messages are taken from fortune cookies  
"S.O.S the creatures have turned hostile on island 2 ",
"a smart computer programmer   once said : 01101001 01101100 01101111 01110110 01100101 01111001 01101111 0111010101101001 01101100 01101111 01110110 01100101 01111001 01101111 0111010101101001 01101100 01101111 01110110 01100101 01111001 01101111 01110101",
"these qoutes are all taken from the fortune program for linux -- except some of them ",
"'And 1.1.81 is officially BugFree(tm), so if you receive any bug-reports on it, you know they are just evil lies'- (By Linus Torvalds)",
"Too often I find that the volume of paper expands to fill the available space",
"You will think of something funnier than this to add to the fortune cookies",
"Base 8 is just like base 10, if 8th was the highest number you could go to bevore needing another digit ",
"Do not underestimate the value of print statements for debugging. -- probably left some accidentally",
"A day without seeing you is like a day without sunshine ",
"If you wish to live wisely, ignore sayings -- including this one.",
"You will have  happiness and  good  friends (to the best of their ability). ",
"S.O.S ms wong made it clear there was going to be a 3k  today",
'''　
   \t  ### ###　
　#########　
　#########　　
　　######　　　
　　　###　　　　
　　　 #　　　　　
'''
]

class playerobj():
    def __init__(self):
        self.name = "olivia ,le"#hardcoded since who else is going to play?
        self.inventory = {}
        self.pos = [0,0]
        self.questmarker = [[0,0],1]
        self.replacementwords = {"$player":self.name,"$time":str(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))}
        self.creature = 'none'

player = playerobj()
        
        
