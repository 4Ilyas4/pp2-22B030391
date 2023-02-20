
def ev(n):
    i = 0 
    while True:
        if i > n :
            return
        if i%2==0:
            yield i
        i += 1
n = int(input())
r = ev(n)

j=int(n/2)
for i in range(j+1):
    print(next(r))
