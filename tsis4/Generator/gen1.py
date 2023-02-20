
def squgen(n):
    i = 1
    while i <= n:
        yield i*i
        i += 1
    
N = 5
squares = squgen(N)
for i in range(5):
    print(next(squares))
