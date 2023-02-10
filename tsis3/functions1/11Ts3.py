def isp(s):
    return s == s[::-1]
print("Введите строку")
s = str(input())
f = isp(s)
if f:
    print("Yes")
else:
    print("No")
