import os
import json
import pickle
def gotjson(filepath):
    jsonformats=[]
    file=open(filepath)
    for line in file.readlines():
        jstr=json.loads(line)
        #print(jstr)
        jsonformats.append(jstr)
        pass
    return jsonformats
    pass
path ='./156277'
jsonlist=[]

for dirpath,dirnames,filenames in os.walk(path):
    for filename in filenames:
        if 'danmu' not in filename:
            continue
            pass
        print(filename)
        fullpath=os.path.join(dirpath,filename)
        jsonlist=gotjson(fullpath)
        jsonlist.extend(jsonlist)
    pass
#print(jsonlist)
storefile="./156277/summdata"
pickle.dump(jsonlist,open(storefile,"wb"))
get=pickle.load(open(storefile,"rb"))
print(type(get))
