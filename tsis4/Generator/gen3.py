
def d34(n):
    i = 0 
    while True:
        if i > n :
            return
        if i%12==0:
            yield i
        i += 1
n = int(input())
r = d34(n)
k = int(n/12)
for i in range(k+1):
    print(next(r))
