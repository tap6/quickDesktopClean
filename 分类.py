import os
import shutil

def gettype(filename):
    if(os.path.isfile(filename)):
        arr=str.split(filename,".")
        return str.split(filename,".")[len(arr)-1]
    elif(os.path.isdir(filename)):
        return "dir"
    else:
        return ["???",filename]
'''def mvFile(a,b):
    shutil.move(a,b)

def mvDir(a,b):
    pass
'''

deskpath=os.path.join(os.path.expanduser("~"), 'Desktop')
os.chdir(deskpath)
print(deskpath,os.listdir())

for i in os.listdir():
    if(type(gettype(i))!=list):
        _filetype = gettype(i)
        if not(os.path.exists(_filetype)) and _filetype!="dir":
            os.mkdir(_filetype)
        if(_filetype!="dir"):
            shutil.move(i,_filetype)
        print(_filetype, "\t", i)



    '''if not(os.path.exists(deskpath+"\\"+filetype.guess(i))):
        os.mkdir(deskpath+"\\"+filetype.guess(i))




print(filetype.guess(deskpath+r"\tts"))
'''