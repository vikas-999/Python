for n in range(1,20):
    while n%2 == 0:
        if n == 2:
            print(n)
            print(1)
            break
        print(n)
        n = n/2
        while n%2 == 1:
            print(n)
            print((3*n)+1)
            n = (3*n)+1
    else:
        while n%2 == 1:
            print(n)
            print((3*n)+1)
        n= (3*n)+1
        while n%2 == 0:
            if n == 2:
                print(n)
                print(1)
                break
            print(n)
            n=n/2





