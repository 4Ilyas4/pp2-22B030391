import os
with open("ez.txt","w+") as f:
    f.write("")
    
pat = os.getcwd() + "\ez.txt"
print(pat)
#os.remove(pat)
