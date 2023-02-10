def per(s, i, l): 
    if i==l: 
        print(s)
    else: 
        for j in range(i,l): 
            s[i], s[j] = s[j], s[i]
            per(s, i+1, l)
print("Введите строку")           
sr = str(input())
n = len(sr) 
s = list(sr)
print("Перестановки:")
per(s, 0, n)
