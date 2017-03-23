import os
import json
import pickle
def gotjson(filepath):
    jsonformats=[]
    file=open(filepath)
    for line in file.readlines():
        jstr=json.loads(line)dfd
        #print(jstr)
        jsonformats.append(jstr)
        pass
    return jsonformats
    pass


def sumdata(roomid):
    jsonlist=[]
    path ='./'+str(roomid)
    for dirpath,dirnames,filenames in os.walk(path):
        for filename in filenames:
            if 'danmu' not in filename:
                continue
            print(filename)
            fullpath=os.path.join(dirpath,filename)
            jsonlist.extend(gotjson(fullpath))
    storefile=path+"/summdata"
    pickle.dump(jsonlist,open(storefile,"wb"))

#print(jsonlist)
roomids=[156277,13703,154537,3484,633019]
for roomid in roomids:
    sumdata(roomid)
    pass


storefile="./156277/summdata"
get=pickle.load(open(storefile,"rb"))
print(str(len(get)))
print(str(type(get[1])))
