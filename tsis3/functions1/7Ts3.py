def has_33(s):
    b="False"
    for i in range(len(s)-1):
        if(s[i]=='3' and s[i+1]=='3'):
            b="True"
    print(b)
print("Введите числа через пробел")
s = str(input())
has_33(s)
