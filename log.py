import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Kingsvip123#",database = "credentials")
cursor = mydb.cursor()

print("---------------------------WELCOME TO REGISTRATION PAGE-----------------------------------")
print("Are you a new user")
print("if yes click 1")
print("if no click 0")
result = int(input("enter your choice :"))
if result == 1:
    x = input("enter a username :")
    y = input("enter a password :")
    re_password = input("re-enter a password :")
    cursor.execute("select * from cred")
    for z in cursor:
        if z[1] == x:
            s = True
        else:
            s = False
    if y == re_password and s != True :
        cursor.execute("select * from cred")
        for i in cursor:
            pass
        c = i[0] + 1
        sql = "INSERT INTO cred (cid, username, password) VALUES (%s, %s, %s)"
        var = (c, x, y)
        cursor.execute(sql, var)
        mydb.commit()
        print("you are sucessfully registered")
        print("==============================================================================================")
        print("you can start login now")
        x = input("enter your username :")
        y = input("enter your password :")
        cursor.execute("select * from cred")
        for i in cursor:
            if i[1] == x and i[2] == y:
                print("login sucessfull")
                e = True
            else:
                e = False
        else:
            if e != True:
                print("invalid credentials")
    elif y != re_password:
        print("password not matched")
    else:
        print("username is already taken try new username")

else:
    x = input("enter your username :")
    y = input("enter your password :")
    cursor.execute("select * from cred")
    for i in cursor:
        if i[1] == x and i[2] == y:
            print("login sucessfull")
            e = True
        else:
            e = False
    else:
        if e != True:
            print("invalid credentials")

        




        

