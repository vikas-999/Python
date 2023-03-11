login = {"admin":'admin',
        "qi7354wc":'Rohit@123',
        "xy5703wc":'virat1234'}
user_info = []
password_info = []
for i in login:
    user_info.append(i)
for j in login.values():
    password_info.append(j)
print("---------------------------WELCOME TO REGISTRATION PAGE-----------------------------------")
print("Are you a new user")
print("if yes click 1")
print("if no click 0")
result = int(input("enter your choice :"))
if result == 1:
    x = input("enter a username :")
    y = input("enter a password :")
    re_password = input("re-enter a password :")
    if y == re_password and y not in user_info:
        print("strong password")
        login.update({x : y})
        print("you are sucessfully registered")
        print("==============================================================================================")
        print("you can start login now")
        x = input("enter your username :")
        y = input("enter your password :")
        for i in login:
            user_info.append(i)
        for j in login.values():
            password_info.append(j)
        if x in user_info and y in password_info:
            print("login sucessfull")
        else:
            print("invalid credentials check your username and password")
    elif y != re_password:
        print("password not matched")
    else:
        print("username is already taken try new username")
 
else:
    x = input("enter your username :")
    y = input("enter your password :")
    for i in login:
        user_info.append(i)
    for j in login.values():
        password_info.append(j)
    if x in user_info and y in password_info:
        print("login sucessfull")
    else:
        print("invalid credentials check your username and password")


    


