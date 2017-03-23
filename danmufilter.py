import os
path ='./156277'

for dirpath,dirnames,filenames in os.walk(path):
    for filename in filenames:
        print(filename)
        fullpath=os.path.join(dirpath,filename)
        file=open(fullpath)
        print(file.readline())
        pass
    pass