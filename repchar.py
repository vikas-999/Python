str = input("enter a string:")
noduplicate = ""
duplicate = ""
for i in str:
    if str.count(i) < 2:
        noduplicate = noduplicate + i
    else:
        duplicate = duplicate + i
print(duplicate)

