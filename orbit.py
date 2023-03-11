#3n+1 function
def orbit(a):
    for n in range(1,a,1):
        while n%2 == 0:
            if n == 2:
                print(n,end=" V ")
                print(1)
                break
            print(n,end=" V ")
            n = int(n/2)
            while n%2 == 1:
                print(n,end=" ^ ")
                n = (3*n) + 1
        else:
            while n%2 == 1:
                if n == 1:
                    print(1)
                    break
                print(n,end=" ^ ")
                n = (3*n) + 1
                while n%2 == 0:
                    if n == 2:
                        print(n,end=" V ")
                        print(1)
                        break
                    print(n,end=" V ")
                    n=int(n/2)
print(sep = "\n")
orbit(21)

            
        



