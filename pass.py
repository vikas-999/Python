print("ENTER YOUR USERNAME AND PASSWORD")
print()
print(
    "passwords rules:\nlength more than 8\n1 upper case number\n2 digits\none special charecter\nno 3 consecutive letters from username")
print()
x = input("enter the username:")
y = input("enter the password:")


# password verification function
def verify_password(u, p):
    pass_dig = 0
    pass_upper = 0
    pass_char = 0
    pass_consec = 0
    if len(p) >= 8:
        pass_len = True
    else:
        print("password length is too short")
    for i in p:
        if i in "1234567890":
            pass_dig += 1
    if pass_dig == 0:
        print("your password should have two digit in the password")
    for j in p:
        if "A" <= j <= "Z":
            pass_upper += 1
    if pass_upper == 0:
        print("your password should have atleast one uppercase")
    for k in p:
        if "A" <= k <= "Z" or "a" <= k <= "z" or "0" <= k <= "9":
            continue
        pass_char += 1
    if pass_char == 0:
        print("your password should have atleast one special character")
    for l in range(0, len(u) - 2, 1):
        if u[0 + l:3 + l:1].upper() in p.upper():
            pass_consec += 1
    if pass_consec > 0:
        print("there are three consecutive letters from username")
    if pass_len == True and pass_dig >= 2 and pass_upper >= 1 and pass_char >= 1 and pass_consec == 0:
        print("strong password")


verify_password(x, y)






