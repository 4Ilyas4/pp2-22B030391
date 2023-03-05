import os
l = []
with open("text.txt","r") as f:
    for i in f:
        l.append(i)
with open("This_7exFile.txt","w+") as f:
    for i in range(len(l)):
        f.write(l[i])
