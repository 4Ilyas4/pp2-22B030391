import os
path ='C://Users//User//Desktop//programming//my//pp2-22B030391'
t = 0 
if os.access(path,os.F_OK):
    print("Exist")
    t = 1
else:
    print("Doesnt")
print("\n")
j = os.scandir(path)
k = 1
if t == 1:
    for i in j:
        if i.is_dir() or i.is_file():
            print("file "+ str(k)+":")
            print(i.name)
            print("directory "+ str(k)+":")
            print(os.path.dirname(i))
            print("\n")
            k += 1
         # os.path.dirname(os.path.dirname(i)))) -
         # os.path.basename(os.path.dirname(i))
