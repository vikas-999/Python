import pyodbc


mydb = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-N3H274QF;"
    "Database=login;"
    "Trusted_Connection=yes;"
    )
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
'''sqlform = "insert into Customers values(%s,%s)"
Customers = [("abc","abc"),("qi7354wc","Rohit@123"),("abd","abd")]
mycursor.executemany(sqlform, Customers)
conn.commit()
'''
'''
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
    username = input("enter a username :")
    password = input("enter a password :")
    re_password = input("re-enter a password :")
    if password == re_password and username not in user_info:
        login.update({username : password})
        print("you are sucessfully registered")
        print("==============================================================================================")
        print("you can start login now")
        username = input("enter your username :")
        password = input("enter your password :")
        for i in login:
            user_info.append(i)
        for j in login.values():
            password_info.append(j)
        if username in user_info and password in password_info:
            print("login sucessfull")
        else:
            print("invalid credentials check your username and password")
    elif password != re_password:
        print("password not matched")
    else:
        print("username is already taken try new username")
else:
    username = input("enter your username :")
    password = input("enter your password :")
    for i in login:
        user_info.append(i)
    for j in login.values():
        password_info.append(j)
    if username in user_info and password in password_info:
        print("login sucessfull")
    else:
        print("invalid credentials check your username and password")

'''
