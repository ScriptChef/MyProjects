#Login System

def login():
    file = open("Login Data File.txt","r")
    arrayofusers = file.readlines()
    usermatch=False
    passmatch=False
    userentry=str(input("Please enter your username: "))
    passentry=str(input("Please enter your password: "))
    for i in range(0,len(arrayofusers)):
        if arrayofusers[i].strip()==userentry and arrayofusers[i+1].strip()==passentry:
            usermatch=True
            passmatch=True
    if (usermatch==True) and (passmatch==True):
        print("Login Successful. Welcome to Robert Smyth IT System.")
    tries=1
    while (usermatch==False) or (passmatch==False) or tries==3:
        if tries==3:
            print("Too many tries. Program will now quit.")
            quit()
        print("Username or password is invalid. Please try again.")
        userentry=str(input("Please enter your username: "))
        passentry=str(input("Please enter your password: "))
        for i in range(0,len(arrayofusers)):
            if arrayofusers[i].strip()==userentry and arrayofusers[i+1].strip()==passentry:
                usermatch=True
                passmatch=True
        tries+=1
        if (usermatch==True) and (passmatch==True):
            print("Login Successful. Welcome to Robert Smyth IT System.")
    file.close()

        
def register():
    file = open("Login Data File.txt","a")
    newuser=str(input("Enter the username that you require: "))
    newpass=str(input("Enter the password that you require: "))
    file.write("\n"+newuser+"\n"+newpass)
    file.close()
    login()

    

def close():
    confirm=str(input("Please confirm exit of the program: (y/n)"))
    if (confirm=='y') or (confirm=='Y'):
        quit()
    elif (confirm=='n') or (confirm=='N'):
        menu()

def menu():
    option=int(input("Enter an option (1)Login (2)Register (3)Quit: "))
    if option==1:
        login()
    elif option==2:
        register()
    else:
        close()

        
#Main Program
file = open("Login Data File.txt","r")
arrayofusers = file.readlines()
usermatch=False
passmatch=False
userentry=""
passentry=""
menu()
    


