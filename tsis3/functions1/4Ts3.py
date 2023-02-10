def filter_prime(n):
    c = 1
    for i in range(2,n):
        if(n%i==0):
            c=0
    if(c==1):
        print(n, end=" ")
print("Введите через пробел числа")
d = input().split()
print("простые числа :")
for i in range(len(d)):
    filter_prime(int(d[i]))
