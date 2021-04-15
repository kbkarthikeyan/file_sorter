import os
import shutil
import re
pattern = r'\([.*?\])'

#!read the name of the directory and files from the current working directory!
def read_information():
    files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
    dir = [d for d in os.listdir(os.curdir) if os.path.isdir(d)]
    return(files, dir)

#!sort the files to the corresponding folder
def sorti(name, subfolder, files):
    for i in files:
        _new = i.split(".")
        if len(_new) == 2:
            dir = re.split('(\d+)',_new[0])
            if dir[len(dir)-1] in name:
                new_dir = name[dir[len(dir)-1]]
        elif len(_new) ==3:
            dir = re.split('(\d+)',_new[1])
            if dir[len(dir)-1] in name:
                new_dir = name[dir[len(dir)-1]]
        if _new[len(_new)-1].lower() == "csv":
            if "APPROVED" in i:
                sub_dir = subfolder["APPROVED"]
                path_old = os.curdir+"//"+i
                path_new = os.curdir+"//"+new_dir+"//"+sub_dir+"//"+i
                change_folder(path_old, path_new)
            else:
                sub_dir = subfolder["KRONOS"]
                path_old = os.curdir+"//"+i
                path_new = os.curdir+"//"+new_dir+"//"+sub_dir+"//"+i
                change_folder(path_old, path_new)
        elif _new[len(_new)-1].lower() == "db":
                sub_dir = subfolder["DB"]
                path_old = os.curdir+"//"+i
                path_new = os.curdir+"//"+new_dir+"//"+sub_dir+"//"+i
                change_folder(path_old, path_new)
        elif _new[len(_new)-1].lower() == "gsi":
                sub_dir = subfolder["GSI"]
                path_old = os.curdir+"//"+i
                path_new = os.curdir+"//"+new_dir+"//"+sub_dir+"//"+i
                change_folder(path_old, path_new)
        
        elif _new[len(_new)-1].lower() == "dat" or _new[len(_new)-1].lower() == "asc" or _new[len(_new)-1].lower() == "txt":
                sub_dir = subfolder["DETAILS"]
                path_old = os.curdir+"//"+i
                path_new = os.curdir+"//"+new_dir+"//"+sub_dir+"//"+i
                change_folder(path_old, path_new)
        
def sort(files, dir):
    for i in files:
        tmp = i.split(".") #separate the extension to find the directory name!
        if len(tmp) == 3:
            new_dir = file_name(tmp[1])
        else:
            new_dir = file_name(tmp[0])
        #print(tmp, new_dir)
        if tmp[len(tmp)-1] == "csv" or tmp[len(tmp)-1] == "CSV":
            if "APPROVED" in i:
                path_old = os.curdir+"//"+i
                path_new = os.curdir+"//"+new_dir+"//"+FOLDER1+"//"+i
                change_folder(path_old, path_new)
            else: 
                path_old = os.curdir+"//"+i
                path_new = os.curdir+"//"+new_dir+"//"+FOLDER2+"//"+i
                change_folder(path_old, path_new)  
        elif tmp[len(tmp)-1] == "DB" or tmp[len(tmp)-1] == "db" or tmp[len(tmp)-1] == "GSI" or tmp[len(tmp)-1] == "gsi" :
            path_old = os.curdir+"//"+i
            path_new = os.curdir+"//"+new_dir+"//"+FOLDER3+"//"+i
            change_folder(path_old, path_new)
        elif tmp[len(tmp)-1].lower() == "DAT" or tmp[len(tmp)-1] == "dat" or tmp[len(tmp)-1] == "ASC" or tmp[len(tmp)-1] == "asc" or tmp[len(tmp)-1] == "TXT" or tmp[len(tmp)-1] == "txt":
            path_old = os.curdir+"//"+i
            path_new = os.curdir+"//"+new_dir+"//"+FOLDER4+"//"+i
            change_folder(path_old, path_new)

# check the folder name
def file_info(files, directory):
    _tmp = []
    for i in files:
        _new = i.split(".") #separate the extension to find the directory name!
        if len(_new) == 2:
            dir = re.split('(\d+)',_new[0])
            if dir[len(dir)-1] not in _tmp:
                _tmp.append(dir[len(dir)-1])
        elif len(_new) ==3:
            dir = re.split('(\d+)',_new[1])
            if dir[len(dir)-1] not in _tmp:
                _tmp.append(dir[len(dir)-1])
    _tmp_dir = {}
    for i in _tmp:    
        _t = i.lower().split("_")
        for j in directory:
            _u = j.lower().split("_")
            for k in _u:
                if k in _t[0]:
                    _tmp_dir[i] = j
                    break
    return (_tmp_dir)  

def associate_dir_name(directory, set):
    _tmp = {}
    for i in directory:
        for j in set:
            #print(i,j)
            _t = (re.findall(str(j),str(i))) 
            if _t:
                _tmp[j] = i 
    return(_tmp) 
    
def change_folder(path_old, path_new):
    #print(path_new)
    try:
        shutil.move(path_old, path_new) #move to the new path! 
    except: 
        pass
    return
    
def check_sub_folder(path):
    _tmp = {}
    path_name = "./"+path+"/"
    dir = [d.name for d in os.scandir(path_name) if os.path.isdir(d)]
    for i in dir:
        tmp = i.lower()
        j = tmp.split(' ')
        if "approved" in j:
            _tmp["APPROVED"] = i
        elif "kronos" in tmp:
            _tmp["KRONOS"] = i
        elif "details" in tmp:
            _tmp["DETAILS"] = i
        elif "raw" in tmp:
            if "gsi" in tmp:
                _tmp["GSI"] = i
            else:
                _tmp["DB"] = i
    return _tmp            

if __name__ == "__main__":
    files, directory = read_information()
    name = file_info(files, directory)
    for path in directory:
        sub_def = check_sub_folder(path)
        #print(sub_def)
        sorti(name, sub_def, files)    
