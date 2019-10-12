'''
Created on 26 Jun 2019

@author: rcreaven
'''
import os
import random
import time
colors=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
while True:
    num=random.randint(0,15)
    num2=random.randint(0,15)
    string="color {}{}".format(str(colors[num]),str(colors[num2]))
    os.system(string)
    print "Color={}".format(string)
    time.sleep(0.5)