def spy_game(s):
    bol="False"
    for i in range(len(s)):
        if s[i] == '0' and s[i+1] == '0' and s[i+2] == '7':
            bol="True"
    print(bol)
print("Введите числа")
s = str(input())
spy_game(s)
