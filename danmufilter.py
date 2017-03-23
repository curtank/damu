import os
import json
path ='./156277'
jsonlist=[]
for dirpath,dirnames,filenames in os.walk(path):
    for filename in filenames:
        if 'danmu' not in filename:
            continue
            pass
        print(filename)
        fullpath=os.path.join(dirpath,filename)
        file=open(fullpath)
        for line in file.readlines():
            jstr=json.loads(line)
            #print(jstr)
            pass
    pass
print(jsonlist)
jsonstr='{"s":1,"a":2}'
print(type(jsonstr))
j=json.loads(jsonstr)
print(j)