t = True
while t :
    print("what do you want todo?")
    print(" 1- new dialog")
    print(" anything else- exit")
    if input() == "1":
        dialog = {}
        y = True
        while y :
            x = 1
            linenum = input("what line is this  (enter to exit)")
            if linenum == "":
                y = 0
                print(dialog)
            else:
                u = input("prompt\n")
                dial = {}
                while x :
                    i = input("write anything to add as dia item , press enter to move on to next line")
                    if not i=="":
                        line = input("what line should this jump to ?")
                        dial[i] = line
                    else:
                        x = 0
                dialog[str(linenum)] = [u,dial]
            
            
            
                    
        
    