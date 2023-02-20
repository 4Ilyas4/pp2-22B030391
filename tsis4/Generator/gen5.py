
def sq(n):
        i = 0
        while True:
            if i > n:
                return
            res = n - i
            yield res
            i += 1
n = int(input())
ev  = sq(n)
for i in range(0,n+1):
    print(next(ev))
