import os
paths ='C://Users//User//Desktop//programming//my//pp2-22B030391'
print('Exist:',os.access(paths,os.F_OK))
print('Readable:', os.access(paths, os.R_OK))
print('Writable:', os.access(paths, os.W_OK))
print('Executable:', os.access(paths, os.X_OK))
