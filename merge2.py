import numpy as np    
import mysql.connector as mysqlq
import matplotlib.pyplot as pl
from prettytable import PrettyTable as pt
import math as ma
import random as rd
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
def eqn(k):
    while True:
        a=input("Enter equation %s->\nf(x)="%k)
        a=a.strip()
        a=a.lower()
        if "x" not in a:
            print("Enter the equation in form y=f(x)")
        else:
            return a
            break
def ran():
    while True:
        print()
        r=input("Enter range- (a to b) -> ")
        r=r.strip()
        r=r.split("to")
        try:
            r[0],r[1]=float(r[0].strip()),float(r[1].strip())
        except:
            print()
            print("please enter in 'a to b' format")
            continue
        if r[0]>r[1]:
            r[0],r[1]=r[1],r[0]
            return r
            break
        elif r[0]==r[1]:
            print()
            print("Range is not acceptable..\n\n")
        else:
            return r
            break
def domain(r):
    x=np.linspace(r[0],r[1],2000)
    return x
def eqnp(e):
    e=e.lower()
    e=e.replace("^","**")
    l=list(e)
    for i in range(0,len(l)):
        if l[i]=="x" and i!=0:
            if e[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")","e"]:
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
        if l[i]=="s" and l[i+1]=="i" and l[i-1]!="c":
            if i==0:
                l[i]="np.s"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.s"
            else:
                l[i]="np.s"
        elif l[i]=="c" and l[i+1]=="o" and l[i-1]!="c":
            if i==0:
                l[i]="np.c"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.c"
            else:
                l[i]="np.c"
        elif l[i]=="t" and l[i-1]!="c":
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
def eqntarc(e):
    l=list(e)
    for i in range(len(l)):
        if l[i]=="a" and l[i+1]=="r" and l[i+2]=="c":
            if i==0:
                l[i]="np.a"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.a"
            else:
                l[i]="np.a"
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
def eqnexp(e):
    l=list(e)
    for i in range(len(l)):
        if l[i]=="e":
            if i==0:
                l[i]="np.e"
            elif l[i-1] in ["0","1","2","3","4","5","6","7","8","9","x",")"]:
                l[i]="*np.e"
            else:
                l[i]="np.e"
        else:
            continue
    e="".join(l)
    return e
def eqnflor(e):    #gif
    l=list(e)
    for i in range(len(l)):
        if l[i]=="[" and "]" in l[i+1:]:
            l[i]="np.floor("
        else:
            continue
    l=[")" if i=="]" else i for i in l]
    e="".join(l)
    return e
def eqnmod(e):
    l=list(e)
    for i in range(len(l)):
        if l[i]=="|" and i<len(l)-1 and l[i+1]=="(":
            l[i]="np.fabs("
        elif l[i]=="|" and i!=0 and l[i-1]==")":
            l[i]=")"
        else:
            continue
    e="".join(l)
    return e
def login():
    k=0
    while k<5:
        a=input("Enter your user id: ")
        a=a.strip()
        st="select id,pass from users where e_id=\"%s\""%(a)
        cur.execute(st)
        l=cur.fetchall()
        if len(l)!=0:
            break
        elif len(l)==0:
            print("user-id is invalid\nPlease try again\n")
            k+=1
    else:
        print("create a new account")
        return None
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
        a=a.strip()
        if len(a)==0:
            print()
            print("field cannot be empty!!")
        else:
            while True:
                z=0
                b=input("enter user id-> ")
                b=b.strip()
                cur.execute("select e_id from users where e_id=\"%s\""%b)
                l=cur.fetchall()
                if len(b)==0:
                    print("field cannot be empty!!")
                elif len(l)!=0:
                    print("User id exists")
                    print()
                    print("Please try with a different name :) ")
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
    print("*"*46)
    st="select * from users where id=%d"%x
    cur.execute(st)
    l=cur.fetchall()
    t=l[0]
    vrl=len(t[2])
    print("* ","welcome %s"%(t[2])," "*(32-vrl),"*")
    print("* "," "*41,"*")
    print("* ","1. New graph"," "*28,"*")                    #42
    print("* ","2. Combined Graphs"," "*22,"*")
    print("* ","3. View older graphs and equations"," "*6,"*")
    print("* ","4. Log-out"," "*30,"*")
    print("*"*46)
    while True:
        a=input("Pleace select your choice -> ")#func menu end
        a=a.strip()
        if a in ("1","2","3","4"):
            break
        else:
            print("only 4 ch...")
    return a
def savegph(a,b,c):
    e="d"+str(a)
    cur.execute("select * from %s"%e)
    l=cur.fetchall()
    if len(l)==0:
        n=0
    else:
        n=l[-1][0]
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
    if len(l)==0:
        print("no older graphs...")
        return None
    else:
        z=l[-1][0]
    for i in l:
        t.add_row(i)
    print(t)
    while True:
        print()
        print("*"*55)
        print("* ","1. Create a graph of an earlier equation."," "*8,"*")
        print("* ","2. Delete any Earlier graph"," "*22,"*")
        print("* ","3. Create simultaneous graphs"," "*20,"*")
        print("* ","4. Back to menu"," "*34,"*")
        print("*"*55)
        print()
        while True:
            try:
                a=input("Pleace select your choice -> ")
                a=a.strip()
                a=int(a)
            except:
                print("Kindly enter a number")
            if a in [1,2,3,4]:
                break
            else:
                print("Kindly enter 1 to 6")
        if a==1:
            while True:
                print()
                b=input("Enter the serial number of the equation for which graph is required -> ")
                if b.isnumeric() and int(b)<=z:
                    break
                else:
                    print()
                    print("Please enter Valid serial number -> ")
                    continue
            st="select eqn,eqnm from %s where sno=%d"%(n,int(b))
            cur.execute(st)
            la=cur.fetchall()
            print(la)
            try:
                enaa=la[0][0]
                en=la[0][1]
                grphh(en,enaa)
                print("graph=>>> ")
                pl.show()
            except:
                print()
                print("Error")
        elif a==2:
            while True:
                zz=0
                st="select sno from %s"%(n)
                cur.execute(st)
                kk=cur.fetchall()
                c=input("Enter the serial number of equation => ")
                if c.isnumeric() and int(c)<=z:
                    c=int(c)
                    for it in kk:
                        if c in it:
                            break
                        else:
                            pass
                    else:
                        print()
                        print("already deleted ")
                        zz=3214
                        break
                    break
                else:
                    print()
                    print("Please enter valid serial number")
                    continue
            if zz!=3214:
                try:
                    st="delete from %s where sno=%d"%(n,int(c))
                    cur.execute(st)
                    g.commit()
                    print()
                    print()
                    print("success, Equation has been deleted")
                except:
                    print()
                    print("failure")
                st="select sno,eqn,dnt from %s"%(n)
                cur.execute(st)
                l=cur.fetchall()
                if len(l)==0:
                    print("no graphs remaining")
                    return None
                else:
                    t=pt(["Sr.no","Equation","Date and time"])
                    for i in l:
                        t.add_row(i)
                    print(t)
            elif zz==3214:
                pass
        elif a==3:
            combgsh(n)
            print("graph=>> ")
            pl.show()
        elif a==4:
            print()
            print(":O")
            break
def combgsh(n):
    st="select sno from %s"%n
    cur.execute(st)
    la=cur.fetchall()
    col=["g","r","m","y","c"]
    while True:
        a=input("number of gaphs-> ")
        a=a.strip()
        if a.isdigit() and int(a)<5:
            a=int(a)
            if a>len(la):
                print("Not enough graphs :)")
                continue
            else:
                break
        else:
            print("please enter a number less than 5 :)")
    for i in range(1,a+1):
        while True:
            c=input("Serial number of equation %d-> "%i)
            if c.isdigit():
                c=int(c)
                for ii in la:
                    if c==ii[0]:
                        break
                    else:
                        continue
                else:
                    print("number not in list")
                    continue
                break
            else:
                print("please enter a number :)")
        st="select eqnm,eqn from %s where sno=%d"%(n,c)
        cur.execute(st)
        eq=cur.fetchall()
        eq1=eq[0][0]
        eqn2=eq[0][1]
        grphh(eq1,eqn2,col[i-1])
def grphh(e,a,c="b"):
    global qla
    r=ran()
    x=domain(r)
    qla=x
    try:
        y=eval(e)
    except:
        print("error occ..")
        return None
    pl.plot(x,y,c,label="y= %s"%a)
    pl.grid(True,which="major")
    pl.axhline(y=0,color="k")
    pl.axvline(x=0,color="k")
    pl.xlabel("X axis -->")
    pl.ylabel("Y axis -->")
    pl.legend(loc="upper left")
def combg(i):
    while True:
        try:
            a=int(input("How many simultaneous graphs are required ? (1 to 6)"))
            print()
        except:
            print("Please Enter Numeric value :)")
            print()
            continue
        if a>6:
            print("Please enter number upto 6 :> ")
            print()
        elif a==0:
            print("Kindly Enter the value from 1 to 6 ;)")
            print()
        else:
            break
    for q in range(1,a+1):
        l=["b","g","r","m","y","c"]
        a=eqn(q)
        c=eqnp(a)
        c=eqnt(c)
        c=eqnmod(c)
        c=eqnl(c)
        c=eqnflor(c)
        c=eqnexp(c)
        c=eqntarc(c)
        r=ran()
        x=domain(r)
        try:
            y=eval(c)
        except:
            print("error occ..")
            break
        pl.plot(x,y,color=l[q-1],label="y= %s"%a)
        savegph(i,a,c)
    pl.grid(True,which="major")
    pl.axhline(y=0,color="k")
    pl.axvline(x=0,color="k")
    pl.xlabel("X axis -->")
    pl.ylabel("Y axis -->")
    pl.legend(loc="upper left")
    pl.show()
def grpha(i,p=""):
    a=eqn(p)
    c=eqnp(a)
    c=eqnt(c)
    c=eqnmod(c)
    c=eqnl(c)
    c=eqnflor(c)
    c=eqnexp(c)
    c=eqntarc(c)
    print()
    col=["b","g","r","m","y","c"]
    rew=rd.randint(0,5)
    grphh(c,a,col[rew])
    pl.show()
    savegph(i,a,c)
#^^^^main^^^^
print("Welcome to maths tool..")
print("Perfect place for creating graphs")
while True:
    q=input("Do you have an account with xyz Software?(Y/n) ")
    q=q.strip()
    print()
    q=q.upper()
    if q=="Y" or q=="YES":
        i=login()
        print()
        if i is None:
            continue
        else:
            pass
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
        if ch =="1":    #i=person 
            print()
            print("Instructions-")
            print("1.) write equation like ax3+bx2+cx+d,  or ae^(bx)")
            print("2.) for trignometric function write like asin(bx) or asin(bx^2)")
            print("3.) For modulus function write as |(ax)|")
            print("4.) For greatest integer function write as [ax]")
            print("5.) For logarithm function write as log(ax) {natural log}")
            print("6.) '*' for multiplication and '/' for division")
            print()
            la=""
            while la!="NO" and la!="N":
                grpha(i)
                la=input("Want to continue with another graph? ")
                print()
                la=la.upper()
        elif ch=="2":
            print()
            print("Instructions-")
            print("1.) write equation like ax3+bx2+cx+d,  or ae^(bx) or ")
            print("2.) for trignometric function write like asin(bx) or asin(bx^2)")
            print("3.) For modulus function write as |(ax)|")
            print("4.) For greatest integer function write as [ax]")
            print("5.) For logarithm function write as log(ax) {natural log}")
            print("6.) '*' for multiplication and '/' for division")
            print()
            le=""
            while le!="NO" and le!="N":
                combg(i)
                while True:
                    le=input("Want to continue with another graph? ")
                    print()
                    le=le.strip()
                    le=le.upper()
                    if le in ("Y","YES","NO","N"):
                        break
                    else:
                        print("Yes or no")
        elif ch=="3":
            show(i)
        elif ch=="4":
            print("Thank you :)")
            break
