'''
Created on 21 May 2019

@author: rcreaven
'''
import os
filename='2019-05-21_12.11_96'
currentversion="BMW_RVC_Jenkins_Binaries-{}".format(filename)
mainpath="C:\Users\\rcreaven\Documents\Jenkins Builds\{}\\21_PDX-Container".format(currentversion)
print mainpath
results=[]
##PDX file
for file in os.listdir(mainpath):
    if file.endswith(".pdx"):
        loc=(os.path.join(mainpath,file))
            
print loc
##FA file
for file in os.listdir(mainpath):
    if file.endswith("Enabled.xml"):
        loc=(os.path.join(mainpath,file))
print loc
##Tal
for file in os.listdir(mainpath):
    if file.endswith("SWE+BEGU_ID_000075c8.tal"):
        loc=(os.path.join(mainpath,file))
print loc