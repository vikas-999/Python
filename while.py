#just using while loop
a = [22,11,34,23,46,35,58,69,70]
i = 0
while i < len(a):
    if a[i]%2 == 0:
        print(a[i],"is even")
    else:
        print(a[i],"is odd")
    i = i + 1
