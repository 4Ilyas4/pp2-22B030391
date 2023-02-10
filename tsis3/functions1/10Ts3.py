def uq(s):
    for i in range(len(s)):
        b = "True"
        for j in range(i,len(s)):
            if int(s[i])==int(s[j]) and i != j:
                b="False"
    if(b=="True"):
        print(int(s[i]))
l = input().split()
uq(l)
