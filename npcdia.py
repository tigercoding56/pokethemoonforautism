npcdia1 = {
"1":["hi how are you today ? \n",{"good":2,"could be better":3,"i am not feeling well":4}]    
,"2":[" good to hear , \n i am also feeling good ",{"bye":10}]
,"10":["have a good day ",{"exit dialog":0}]
,"3":[" at least you are not feeling \n worse , \n what happened",{"bye":10,"(speak about what happened)":11}]
,"11":["(the robot expresses  \n empathy for what happened)  , \n ",{"bye":10}]
,"4":[" just relax , \n time always changes \n it will be better \n eventually if not soon  , \n what happened?",{"have a good day":10,"(speak about what happened)":11}]
,"menu":["what do you want to ask me ?",{"how are you ?":5,"what is the time":6}]
,"5":["i am fine , \n how are you today ?",{"good":2,"could be better":3,"i am not feeling well":4}]
,"6":["it is 25:0:2 standart military time ,\n date :  sep , 4 , 2076 ",{"i want to ask you":"menu","have a nice day ":0}]
}


def gnpcdia():
    global npcdia1
    return npcdia1


confuseddia = {
"1":["error 408 , TPU timeout",{" (back away)":0}]   
}

milvetdia1 = {
"1":[" oh i should have known that \n the fire nation would\n be back",{"fire nation?":2,"  the attack was from 1 hacker , not a nation ":3,"what?":2}]
,"2":["yes \n , a infamous hacking group \n it tried to overthrow our goverment \n multiple times -it was split up \n by the police in 2077",{" the attack was one hacker not a group":3}]
,"3":["Oh , in that case i would advise finding out what the hackers intentions are",{" as far as i know they are bad  (hero of robots storyline)":4,"maybe we ought to find out (more perfect union storyline)":5,"i'll think about it (exit dialog)":0}]##divergence point##
,"4":["in that case , there should be a pc in the town that is south (down) \n from the copper pile\n interact with it and take the info chip it provides \n give it to me so i can decode it",{"ok":"hob","anything to help the robots":"hob","will do":"hob","got it":"hob"}]
,"5":[" a wise decision , \ni was in the airforce and crashed an airplane \n,a a-10 \n, somewhere to the west of a pile of \n coppper ore \n not much left except a radio transmitter you could use to contact the hacker \n after you are done , come back and tell me what \n the hackers reasoning is ",{"yes":"MPU","will do ":"MPU"}]
}

milvetdia_un_a= {
"1":["to get to the radio \n follow the footpath until you get to \n a pile of copper ore , there should be \n a crashed airplane to the west  of it  \n interact with the radio near it \n",{"thank you for clarification":0,"got it":0}]
}
milvetdia_un_b= {
"1":["to get to the terminal \n follow the footpath until you get to \n a pile of copper ore , then follow the path \n south (leading down the map)  of it  \n there should be a town , enter it and \n the terminal should be in one of the  houses \n select the get infochip option \n from the terminal's menu ",{"thank you for clarification":0,"got it":0}]
}
hackerdia2 = {
"1":["after telling the hacker the news \n he tells you that he will setup teleportation beacons to the abandoned oil platform  \n he is now using as base \n and asks you to visit , to help plan an attack , that will \n force the goverment to stop \n any unethical practizes ",{" ok":"stb"}]    
}
milvetdia_f={
"1":["what justification did the hacker \n have for slowing us down?",{"he mistook us for military robots":2,"something about the goverment being oppressive":3}]
,"2":["well \n  there is another island  not far from here \n with military robots , and the \n goverment is not very good \n in fact the US has not had a \n good goverment since the \n resource wars of 2068",{"(tell about the hacker)":4}]
,"3":[" that is a fair point , but sadly we are not powerfull enough to \n make a more perfect union \n as the goverment unalived almost everyone who actually \n had common sense \n except for a few ... ,thanks to \n the effort of the teachers at \n  IUSD- the International ,Union of Student Debt\n ",{"well the hacker offered to help":4}]
,"4":["well joining the \" fire nation\" cannot possibly be worse \n than the state the US goverment has \n fallen into , (robot leaves and some  \n time passes until it returns) i asked the robots , and they \n are all on-board with joining the hacker \n ",{"i'll report back to the hacker now":"reportback"}]
}
rdia ={##### this is just a  game , the whole story has inspiration from the world of fallout, but should not infringe on any copyrigthed content #####
    
 "1":["you follow the instructions of the robot \nand activate the radio \n after some time you decide to \n send out ",{"who are you , and why did you disable the robots":2,"anyone there?":3}],
 "2":[" i am cyberhack85 \n and those robots\n you are talking about \n are unhealthcare \n machines -- keepable of  unaliving \n thousands of people \n per minute", {"tell me more about the robots":4} ],
 "3":["yes what do you want from me?",{"i want to know who you are  and why you disabled the robots":3}],
 "4":["the robots are military robots\n made by the US goverment \n  this was not that bad \n until they kicked professor sabado , out of the project  \n without sabado to regulate ethics \n the whole project turned to mayham going as far \n as to ... ",{"(listen)":7,"as far as to what?":7}],
 "5":["yes , the goverment thinks they \n dismantled the group \n , but they did not",{"one concern i have is that the robots on this island are nice":6}],
 "6":[" (2 minutes later) , oh , i wasted energy disabling the wrong robots, \n i think there is a old oil rig near the island \n that would make a good base ,i'll enable the robots again ,\n and you can ask the robot that send you  here\n if the robots would  \n mind joining my hacking group \n-- the \"fire nation \"",{" i will ask the robot that send me here ":"ac","yes":"ac","got it":"ac"}],
 "7":["test the military robots , in schools ... \n told the schools it was to keep the peace and prevent crimes \n in reality those robots killed any students that where \n deemed to be unfit for society \n including any with even slight disabilities \nand all students that had any kind of mental disorder \n  , helped a bunch of friends hack one of the robots ,  and the rest is history ",{"is that how the fire nation started?":5,"the robots on this island have all been nice to me ":6}]
    
    
}

urdia = {
"1":["you mess around with the radio for a bit , \n and some music plays",{"ok":0}]    
}

tdia = {
"1":["the terminal displays a menu allowing you to \n perform a variety of actions",{"logs":2,"eject info chip":"ac","datetime":3,"exit":0}]
,"2":["which log?",{"standart military":4,"standart personal":5,"logs to show to regulatory agency":6}]
,"3":["it is 25:0:2 standart military time , date :  sep , 4 , 2076",{"return to menu":1}]
,"4":["commander , we lost 5 robots already , \n .. .. just pretend we got all of the targets \n and dont tell anyone",{"return to menu":1}]
,"5":[" , the  military robots are going insane , \n 1 heroic student managed \n to keep olivia. le and a bunch of others safe \n apparently the goverment is worried about \n how smart she is   \n  ,we managed to save \n the vast majority of our students  \n  -- ms dhiman signing off ",{"return to menu":1}]
,"6":["all the casualities  \nwhere suicides Mister NATO , \n we DeFInaTeLy did not \n just unalive a bunch of our own people \n to test how effective \n our weapons are \n ",{"return to menu":1}]
}