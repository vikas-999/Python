
a = [2,3,4,5,6]
b = [2,5,8,1]
c = [9,1,2,3]
for i in range(4):
    try:
        print(a[i])
        a.remove(i)
        print(a)
        print(b[i])
        b.remove(i)
        print(b)
        print(c[i])
        c.remove(i)
        print(c)
    except (ValueError, IndexError) as msg:
        print(f"=={msg}== in the loop no {i+1}")
    else:
        print(f"no error in the loop {i+1}")
    finally:
        print(f"===========end of the loop {i+1}==========")
