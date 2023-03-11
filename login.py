login = {"admin":'admin',
         "qi7354wc":'Rohit@123',
         "xy5703wc":'Juhi1234'}
username = input("enter your username :")
password = input("enter your password :")
user_info = []
password_info = []
user = {username:password}
for i in login:
    user_info.append(i)
for j in login.values():
    password_info.append(j)
if username in user_info and password in password_info:
    print("login sucessfull")
else:
    print("invalid credentials check your username and password")


    


