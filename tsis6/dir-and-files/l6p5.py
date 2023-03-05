import os
l = [1,2,3,4,5]
with open("newfile.txt", "w+") as f:
    f.write(str(l))
