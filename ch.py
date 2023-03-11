ch = input("eneter: ")
if ord("0") <= ord(ch) <= ord("9"):
    print("its a digit")
elif ord("A") <= ord(ch) <= ord("Z"):
    print("upper")
elif ord("a") <= ord(ch) <= ord("z"):
    print("lower")
else:
    print("special char")
