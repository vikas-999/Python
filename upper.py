'''wap to check the given case is upper or not, with and without inbuilt method'''
#with inbuilt method
letter = input("enter the character : ")
if letter.isupper() == True:
    print(f"{letter} is upper case")


#without inbuilt
letter = input("enter the character : ")
if "A" <= letter <= "Z":
    print(f"{letter} is upper case")

