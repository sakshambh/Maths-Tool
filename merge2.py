import mysql.connector as mysqlq
import numpy as np
import matplotlib.pyplot as pl
from prettytable import PrettyTable as pt
g=mysqlq.connect(host="localhost",user="root",passwd="newdelhi96")
cur=g.cursor()
cur.execute("show databases")
dbs=cur.fetchall()
value=0
for i in dbs:
    if "maths_tool" in i:
        value=1
    else:
        continue
if value==0:
    cur.execute("create database maths_tool")
    cur.execute("use maths_tool")
elif value==1:
    cur.execute("use maths_tool")
cur.execute("show tables")
tab=cur.fetchall()
val=0
for i in tab:
    if "users" in i:
        val=1
    else:
        continue
if val==0:
    cur.execute("create table users(id numeric primary key,e_id varchar(20) unique, name varchar(40) not null, pass varchar(15) not null)")    
"""Fuctions"""
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
        if r[0].isdigit() and r[1].isdigit():
            if r[0]>r[1]:
                r[0],r[1]=r[1],r[0]
                return r
                break
            elif r[0]==r[1]:
                print("Range is not acceptable..\n\n")
            else:
                return r
                break
        else:
            print("please enter in a to b format")
            continue
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
def login():
    k=0
    while k<5:
        a=input("Enter your user id: ")
        st="select id,pass from users where e_id=\"%s\""%(a)
        cur.execute(st)
        l=cur.fetchall()
        if len(l)!=0:
            break
        elif len(l)==0:
            print("userid is invalid\nPlease try again")
            k+=1
    else:
        print("create a new account")
        return 0
    while True:
        b=input("Enter password-> ")
        if l[0][1]==b:
            z=1
            break
        else:
            print("wrong password!!")
    return l[0][0]          #returning id
def account():
    while True:
        a=input("Your name-> ")
        if len(a)==0:
            print("field cannot be empty!!")
        else:
            while True:
                z=0
                b=input("enter user id-> ")
                cur.execute("select e_id from users where e_id=\"%s\""%b)
                l=cur.fetchall()
                if len(b)==0:
                    print("field cannot be empty!!")
                elif len(l)!=0:
                    print("User id exists")
                else:
                    break
            break
    while True:
        c=input("Enter passwd-> ")
        if len(c)==0:
            print("field cannot be empty!!")
        else:
            break
    cur.execute("select * from users")
    l=cur.fetchall()
    n=len(l)
    st="insert into users values(%d,\"%s\",\"%s\",\"%s\")"%(n+1,b,a,c)
    cur.execute(st)
    g.commit()
    print("your account has been created!!!:)")
    q=str(n+1)
    std="create table %s(sno numeric unique ,dnt datetime,eqn varchar(40),eqnm varchar(50))"%("d"+q)
    cur.execute(std)
    return n+1                #returning its id
def menu(x):
    print("*"*50)
    st="select * from users where id=%d"%x
    cur.execute(st)
    l=cur.fetchall()
    t=l[0]
    print("welocme %s"%(t[2]))
    print()
    print("1. New graph \n2. View older graphs and equations \n3. Exit")
    while True:
        a=input("Pleace select your choice -> ")#func menu end
        if a in ("1","2","3"):
            break
        else:
            print("only 3 ch...")
    return a
def savegph(a,b,c):
    e="d"+str(a)
    cur.execute("select * from %s"%e)
    l=cur.fetchall()
    n=len(l)
    z=n+1
    st="insert into %s values(%d,now(),\"%s\",\"%s\")"%(e,z,b,c)
    cur.execute(st)
    g.commit()
def show(n):
    n="d"+str(n)
    t=pt(["Sr.no","Equation","Date and time"])
    st="select sno,eqn,dnt from %s"%(n)
    cur.execute(st)
    l=cur.fetchall()
    z=len(l)
    for i in l:
        t.add_row(i)
    print(t)
    while True:
        a=input("graph??=> ")
        a=a.upper()
        if a=="Y" or a=="YES":
            while True:
                b=input("enter snoo-> ")
                if b.isnumeric() and int(b)<=z:
                    break
                else:
                    print("sno!!!!!")
                    continue
            st="select eqnm from %s where sno=%d"%(n,int(b))
            cur.execute(st)
            la=cur.fetchall()
            en=la[0][0]
            grphh(en)
            print("graph=>>> ")
            pl.show()
        elif a=="N" or a=="NO":
            print("okk?:O")
            break
def grphh(e):
    r=ran()
    x=domain(r)
    y=eval(e)
    pl.plot(x,y)
    pl.grid(True,which="major")
    pl.axhline(y=0,color="k")
    pl.axvline(x=0,color="k")
    pl.show()
#"""main"""
while True:
    q=input("Do you have an account? ")
    print()
    q=q.upper()
    if q=="Y" or q=="YES":
        i=login()
        print()
    elif q=="N" or q=="NO":
        print("Lets create your account!!")
        print()
        i=account()
        print()
    elif q=="E" or q=="EXIT":
        print("goodbye!!:)")
        break
    else:
        print("enter either yes or no!!")
        continue
    while True:
        ch=menu(i)
        if ch =="1":
            print()
            print("Instructions-\nFor trigonometric functions- use function....\
    angle in brackets\nFor inverse functions use arc...\nFor log functi\
    ons, enter base before brackets like loga(x) where b is base\n*Note log\
    (x) will be taken as log base e*\nFor exponents use e**x or e^x\n\nDon't use x as \
    multiplication symbol")
            la=""
            while la!="NO" and la!="N":
                a=eqn()
                c=eqnp(a)
                c=eqnt(c)
                c=eqnl(c)
                print()
                print("graph->\n")
                grphh(c)
                savegph(i,a,c)
                la=input("any more graphs?")
                la=la.upper()
        elif ch=="2":
            show(i)
        elif ch=="3":
            print("Thanks...")
            break
