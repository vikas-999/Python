def fun(n,i=0):
    if i > n:
        return i
    else:
        print(i)
        i+=1
        fun(n,i)
       
print(fun(20))
