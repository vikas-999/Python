'''
def func():
    for i in range(3):
        yield i
res = func()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
'''

def fun():
    l = ["vikas", "bala", "sabbineni", "rohit", "sharma", "virat", "kohli"]
    for i in range(len(l)):
        if i%2 == 0:
            yield(l[i])
r = fun()

print(list(r))
print(next(r))
