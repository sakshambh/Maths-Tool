#maths tool
import numpy as np
import matplotlib.pyplot as pl
def eqn():
    while True:
        print("Instructions-\nFor triginometric functions- use ")
        a=input("Enter equation->\nf(x)=")
        if "x" not in a:
            print("Enter the equation in form y=f(x)")
        else:
            return a
            break
def ran():
    while True:   
        r=input("Enter range- (a - b) -> ")
        r=r.split("-")
        r[0],r[1]=int(r[0].strip()),int(r[1].strip())
        if r[0]>r[1]:
            r[0],r[1]=r[1],r[0]
            return r
            break
        elif r[0]==r[1]:
            print("Please enter different range...\n\n")
        else:
            return r
            break
def domain(r):
    x=np.arange(r[0],r[1],0.4)
    return x
#main
while True:
    a=eqn()
    b=ran()
    x=domain(b)
    y=eval(a)
    print()
    print("graph->\n")
    pl.plot(x,y)
    pl.show()
    
