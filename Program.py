#maths tool
import numpy as np
import matplotlib.pyplot as pl
def eqn():
    while True:
        a=input("Enter equation->\nf(x)=")
        if "x" not in a:
            print("Enter the equation in form y=f(x)")
        else:
            return a
            break
def ran():
    while True:   
        r=input("Enter range- (a to b) -> ")
        r=r.split("to")
        r[0],r[1]=float(r[0].strip()),float(r[1].strip())
        if r[0]>r[1]:
            r[0],r[1]=r[1],r[0]
            return r
            break
        elif r[0]==r[1]:
            print("Range is not acceptable..\n\n")
        else:
            return r
            break
def domain(r):
    x=np.linspace(r[0],r[1],1000)
    return x
def eqnp(e):
    e=e.lower()
    e=e.replace("^","**")
    l=list(e)
    for i in range(1,len(l)):
        if l[i]=="x":
            if e[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*x"
            else:
                continue
        else:
            continue
    e="".join(l)
    return e
def eqnt(e):
    l=list(e)
    for i in range(len(l)):
        if l[i]=="s" and l[i+1]=="i":
            if i==0:
                l[i]="np.s"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.s"
            else:
                l[i]="np.s"
        elif l[i]=="c":
            if i==0:
                l[i]="np.c"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.c"
            else:
                l[i]="np.c"
        elif l[i]=="t":
            if i==0:
                l[i]="np.t"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.t"
            else:
                l[i]="np.t"
        else:
            continue
    e="".join(l)
    return e
def eqnl(e):
    l=list(e)
    for i in range(len(l)):
        if l[i]=="l" and l[i+3]=="(":
            if i==0:
                l[i]="np.l"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.l"
            else:
                l[i]="np.l"
        else:
            continue
    e="".join(l)
    return e
#main
print("Instructions-\nFor trigonometric functions- use function....\
angle in brackets\nFor inverse functions use arc...\nFor log functi\
ons, enter base before brackets like loga(x) where b is base\n*Note log\
(x) will be taken as log base e*\nFor exponents use e**x or e^x\n\nDon't use x as \
multiplication symbol")
while True:
    a=eqn()
    b=ran()
    x=domain(b)
    c=eqnp(a)
    c=eqnt(c)
    c=eqnl(c)
    y=eval(c)
    print()
    print("graph->\n")
    pl.plot(x,y)
    pl.show()
    
