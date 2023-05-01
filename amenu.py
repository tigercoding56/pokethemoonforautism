#adatptive menu
t = [["city1",(0,0),1],["city2",(3,0),1],["city4",(0,0),0]]
def gm(t):
    li =[]
    xl = {}
    cl =[]
    for i in t:
        if i[2] == 1:
            li.append(i[0])
            xl[str(i[0])] = i[1]

    dl = {"1":["where would you like to travel to",xl]}
    return [dl]
gm(t)