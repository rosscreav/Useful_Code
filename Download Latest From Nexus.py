import os 
import zipfile
import shutil
import subprocess
import time
import ntpath
import sys
from os import listdir
from os.path import isfile, join

########Global
i=0

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
            
def loadversionname():
    mypath="C:\Users\\rcreaven\Documents\Jenkins_Builds"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    try:
        name=onlyfiles[0]
        name=name[24:-4]
        return name
    except:
        null='a'
        return null

def delete_old_vers(filename):
    f_zip="C:\Users\\rcreaven\Documents\Jenkins_Builds\BMW_RVC_Jenkins_Binaries-{}.zip".format(filename)
    folder=f_zip[0:-4]
    try:
        shutil.rmtree(folder)
        os.remove(f_zip)
    except:
        pass

def get_curr_version():
    data= subprocess.check_output('curl -g -u url')
    ##truncate the html by the filers
    pos=data.find('<td>')               ##lower end
    data=data[pos:len(data)]
    pos=data.find('maven-metadata.xml') ##upper end
    data=data[0:pos]
    names=[]                            ##output data
    search=0                            ##Start postion for search
    while True:
        startindex=data.find('a href=\"2019',search)
        #print 'startin:'+str(startindex)
        endindex=data.find('\"',startindex+8)
        #print 'endin:'+str(endindex)
        name=data[startindex+8:endindex-1]
        if name!='href':
            print 'appending:' +name
            names.append(name)
        elif name=='href':
            break
        search=endindex+5
    print "Latest Version:"+str(names[-1])
    return names[-1]
    
def download(filename):
            print("Downloading:"+filename)
            curlresponse=os.system("curl -X GET -u username:pass url".format(filename,filename))
            if curlresponse==0:
                filedownload="savename" .format(filename)
                b = os.path.getsize(filedownload)
                print 'Download successful'
            else: 
                if i==4:
                    print 'Downloading Failed'
                    sys.exit()
                download(filename)
                i=i+1;
            print('size is:'+str(b))
            if(b<10000):
                os.remove(filedownload)
                download(filename)
                          
##Unzips to folder to a new folder               
def unzipdownload(filename,newloc):
    foldername=filename[:-4]
    folderlocation='C:\Users\\rcreaven\Documents\Jenkins_Builds\{}'.format(foldername)
    os.mkdir(folderlocation) 

    zip_ref=zipfile.ZipFile(newloc,'r')
    zip_ref.extractall(folderlocation)
    zip_ref.close()

##Start##
versionnum=loadversionname()
filename=get_curr_version()
print 'Version Detected:' +versionnum
##Check is there a new version
if versionnum==filename:
    print '##sleeping##'
    time.sleep(60)
else:
    if versionnum!='a':
        delete_old_vers(versionnum)
        
    download(filename)
    filename="BMW_RVC_Jenkins_Binaries-{}.zip".format(filename)
    currfile="C:\Users\\rcreaven\eclipse-workspace\Random_Stuff\default\{}" .format(filename)
    newloc="C:\Users\\rcreaven\Documents\Jenkins_Builds\{}".format(filename)
    print("Here:"+currfile)
    print("There"+newloc)
    os.rename(currfile,newloc)
    unzipdownload(filename, newloc)
