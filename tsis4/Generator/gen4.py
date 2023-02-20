
def squares(a,n):
        i = a
        while True:
            if i > n:
                return
            res = i*i
            yield res
            i += 1
a = int(input())
n = int(input())
ev  = squares(a,n)
for i in range(a,n+1):
    print(next(ev))
