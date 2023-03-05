import os
path = 'C://Users//User//Desktop//programming//my//pp2-22B030391//tsis6'
paths ='C://Users//User//Desktop//programming//my//pp2-22B030391'

print("   only directories in path tsis6")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
print("   only files in path tsis6")
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)
print('\n')
j = os.scandir(paths)
print("Files and Directories in '% s':" % paths)
for i in j:
    if i.is_dir() or i.is_file():
        print(i.name)
