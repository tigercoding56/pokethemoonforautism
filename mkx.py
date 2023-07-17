import timeit
def mrhna(x,y):#computionally expensive , can be used to simulate low-end hardware
    t=x
    for i in range(1,x) :
        t=t+(i*y)
        if x > 0:
            t = t + mrhna(y-1,x)
    return t
def xt():
    mrhna(23,5)
print(timeit.timeit(xt,number=10)/10)