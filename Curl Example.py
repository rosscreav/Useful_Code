'''
Created on 15 May 2019

@author: rcreaven
'''
import os
import shutil
import time
 
os.system("curl https://www.python.org/static/apple-touch-icon-144x144-precomposed.png > image.png")
print(os.getcwd())

dtc="C:/Users/rcreaven/Desktop/temp"
os.mkdir(dtc) 
os.rename("C:/Users/rcreaven/eclipse-workspace/Download Test/default/image.png","C:/Users/rcreaven/Desktop/temp/image.png")
time.sleep(7)
shutil.rmtree(dtc)