def reverse(s):
    for i in range(len(s)):
        print(s[len(s)-i-1], end=" ")
print("Введите строку")
s = input().split()
print("реверс:")
reverse(s)
