'''
Created on 10 Jun 2019

@author: rcreaven
'''
from Tkinter import *
from glob import glob
from os.path import join
import time

token=''
##Gets a list of all the camera tokens
def get_cam_tokens():
    dirs=glob("C://Users//rcreaven//Documents//Jenkins_Builds//Config//Tokens/*/")
    directories=['Please select a cam']
    for x in dirs:
        x=x[63:-1]
        directories.append(x)
    return directories

##Opens a menu to select tokens for camera from the list
def menu(dirs):
    OPTIONS = dirs#etc
    master = Tk()
    variable = StringVar(master)
    variable.set(OPTIONS[0]) # default value
    w = OptionMenu(master, variable, *OPTIONS)
    w.pack()
    def ok():
        global token
        token = "C:\\Users\\rcreaven\\Documents\\Jenkins_Builds\\Config\\Tokens\\" + variable.get()
        if token!='Please select a cam':            
            master.destroy()
    button = Button(master, text="OK", command=ok)
    button.pack()
    back = Frame(master, width=500, bg='black')
    back.pack()
    mainloop()







dirs=get_cam_tokens()
menu(dirs)
print token
time.sleep(30)













