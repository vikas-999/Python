#wap to check the given character is special character or not
#without inbuilt
'''
char = input("enter the special character : ")
sp_char = "!@#$%^&*~|\/<> "
if char in sp_char:
    print(f"{char} a special character")
    '''
#with inbuilt

char = input("enter the special character : ")
if char.islower() == True:
    print(f"{char} a special character")

