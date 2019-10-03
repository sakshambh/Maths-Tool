import mysql.connector as mysqlq
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
    return n+1
def menu(x):
    print("*"*50)
    st="select * from users where id=%d"%x
    cur.execute(st)
    l=cur.fetchall()
    t=l[0]
    print("welocme %s"%(t[2]))
"""main"""
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
    menu(i)
            
            
            
        
        
