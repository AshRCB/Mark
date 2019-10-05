
users={}
status=''

def displaymenu():
    status=input("are you registered user(y/n)? press q to quit: ")
    if status=='y':
        olduser()
    elif status=='n':
        newuser()
    elif status=='q':
        exit()

def newuser():
    create_login=input("\nCreate login name: ")
    if create_login in users:
        print("\n User already exist!")
    else:
        create_password=input("Create password: ")
        users[create_login]=create_password
        print(" User created\n")
        
def olduser():
    login=input("\nEnter login name: ")
    if login in users:
        password=input("Enter password: ")
        if users[login]==password:
            print(" login successful\n")
        else:
            print("Wrong password.\n")
    else:
        print("user doesnt exist\n")

while status!='q':
    displaymenu()
