"""Welcome User"""
i={}
l=[]
bio={}
def login():        #func login
    global i
    global ch
    global us
    for k in range(5):
        a=input("Enter your user id: ")
        if a in i:
            while True:
                b=input("Enter password: ")
                if i[a]==b:
                    us=a
                    ch=menu(a)  #menu()
                    return 2
                    break
                else:
                    print("Try again")
            break
        else:
            print("Wrong id, Try again")            #func login end
            pass
    else:
        print("Maximum limit reached")
def account():              #func account
    global i
    global l
    global ch
    global us
    e={}
    a=input("Enter Your name: ")
    while True:
        try:
            b=int(input("Enter your number: "))
            break
        except:
            print("Please enter a numeric value")
            continue
    f=input("Enter your mail id-> ")
    while True:
        c=input("Enter userid :")
        if c in i:
            print("User id exs: ")
        else:
            d=input("Enter your password: ")
            i[c]=d
            e["Name"]=a
            e["Number"]=b
            e["mail"]=f
            e["User_id"]=c
            e["Passw"]=d
            l.append(e)
            print("Welldone, Your account has been created")
            us=a
            ch=menu(c)
            break                           #func account end
def menu(x):                    #func menu 
    print("*"*50)
    global l
    for i in l:
        if i["User_id"]==x:
            break
    n=i["Name"]
    no=i["Number"]
    print("Welcome %s your phone number is- %d"%(n,no))
    print()
    print("1. Edit your information \n2.Add biodata \n3.Change Password \n4. Exit")
    a=int(input("Pleace select your choice -> "))               #func menu end
    return a
def edit(y):                    #func edit
    global l
    d=0
    for i in l:
        if i["User_id"]==y:
            break
        d+=1
    print("Name- ",i["Name"])
    print("Phone number- ",i["Number"])
    print("E-Mail id- ",i["mail"])
    while True:
        b=input("What you want to change? ")
        b=b.upper()
        if b=="NAME":
            c=input("Enter new name- ")
            i["Name"]=c
            l[d]=i
        elif b=="PHONE NUMBER" or b=="NUMBER":
            while True:
                try:
                    c=int(input("Enter new number-> "))
                    i["Number"]=c
                    l[d]=i
                    break
                except:
                    print("Please enter numeric value")
                    continue
        elif b=="MAIL" or b=="EMAIL":
            c=input("Enter new mail id-> ")
            i["mail"]=c
            l[d]=i
        else:
            print("Select name or number only")
        e=input("Do you want to change any thing else? ")
        e=e.upper()
        if e=="Y" or e=="YES":
            continue
        elif e=="N" or e=="NO":
            break
    print("Your information has beem successfully updated")     #func edit end
def biodata(y):                  #func biodata
    global l
    global bio
    if y in bio:
        print("Your biodata-> ",bio[y])
        a=input("Do you want to add something? ")
        a=a.upper()
        if a=="Y" or a=="YES":
            c=input("Enter changes (this will add in the end or your earlier biodata)\n=> ")
            bio[y]=bio[y]+" "+c            
    else:
        b=input("Enter your biodata\n=> ")
        bio[y]=b
    print("Your updated bio data is-\n",bio[y])         #func biodata end
def passch(x):                     #func change password
    d=0
    for i in l:
        if i["User_id"]==x:
            break
        d+=1
    while True:
        a=input("Confirm password- ")
        if a==i["Passw"]:
            b=input("enter new password- ")
            i["Passw"]=b
            l[d]=i
            break
        else:
            print("Please try again!!")         #func chage password end
print("Welcome to xyz")
while True :
    while True:
        print()
        q=input("Do you have an account? ")
        print()
        q=q.upper()
        if q=="Y" or q=="YES":
            zz=login()
            print()
            if zz==2:
                break
        elif q=="N" or q=="NO":
            print("Lets create your account!!")
            print()
            account()
            print()
            break
    print("Yoiu entered choice number ",ch)
    while True:
        if ch==1:
            edit(us)
        elif ch==2:
            biodata(us)
        elif ch==3:
            passch(us)
        elif ch==4:
            print("Goodbye!!")
            break
        ch=menu(us)
    qq=input("*Do you want to continue?* ")
    qq=qq.upper()
    if qq=="Y" or qq=="YES":
        continue
    elif qq=="N" or qq=="NO":
        break
