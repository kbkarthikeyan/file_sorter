import os
import shutil
import re
#!read the name of the directory and files from the current working directory!
def read_information():
    files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
    dir = [d for d in os.listdir(os.curdir) if os.path.isdir(d)]
    return(files, dir)

#!sort the files to the corresponding folder only name
def sort(files, dir): 
    for i in files:
        tmp = i.split(".") #separate the extension to find the directory name!
        if tmp[0] in dir:
            path_old = os.curdir+"//"+i
            path_new = os.curdir+"//"+tmp[0]+"//"+i
            shutil.move(path_old, path_new) #move to the new path! 

#!sort the files to the corresponding folder with namenumber
def sort_fn(files, dir):
    for i in files:
        tmp = i.split(".") #separate the extension to find the directory name!
        tmp = re.split('(\d+)',tmp[0])
        if tmp[0] in dir:
            path_old = os.curdir+"//"+i
            path_new = os.curdir+"//"+tmp[0]+"//"+i
            shutil.move(path_old, path_new) #move to the new path! 
            
files,directory = read_information()
sort(files,directory)    
