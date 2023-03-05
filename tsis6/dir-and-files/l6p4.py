import os
fname = str(input()) +".txt"
#text
k = 0
with open(fname) as f:
    for i in f:
        k += 1   
print("Number of lines in text file: ",k)

