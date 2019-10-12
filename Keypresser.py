'''
Created on 25 Jul 2019

@author: rcreaven
'''
import time
from pynput.keyboard import Key, Controller
##Definitions
def pressl(key):
    keyboard.press(key)
    time.sleep(0.25)
    keyboard.release(key)
    
def pressk(key):
    if key=='cmd':
        keyboard.press(Key.cmd)
        time.sleep(0.25)
        keyboard.release(Key.cmd)
    if key=='shift':
        keyboard.press(Key.shift)
        time.sleep(0.25)
        keyboard.release(Key.shift)
    if key=='tab':
        keyboard.press(Key.tab)
        time.sleep(0.25)
        keyboard.release(Key.tab)
    if key=='enter':
        keyboard.press(Key.enter)
        time.sleep(0.25)
        keyboard.release(Key.enter)
    if key=='down':
        keyboard.press(Key.down)
        time.sleep(0.25)
        keyboard.release(Key.down)
    if key=='left':
        keyboard.press(Key.left)
        time.sleep(0.25)
        keyboard.release(Key.left)
    if key=='up':
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    if key=='f4':
        keyboard.press(Key.f4)
        time.sleep(0.25)
        keyboard.release(Key.f4)
    
        
def presshold(key):
    if key=='cmd':
        keyboard.press(Key.cmd)
        time.sleep(0.25)
    if key=='shift':
        keyboard.press(Key.shift)
        time.sleep(0.25)
    if key=='tab':
        keyboard.press(Key.tab)
        time.sleep(0.25)
    if key=='ctrl':
        keyboard.press(Key.ctrl)
        time.sleep(0.25)
    if key=='up':
        keyboard.press(Key.up)
        time.sleep(0.25)
    if key=='alt':
        keyboard.press(Key.alt)
        time.sleep(0.25)
        
def pressrel(key):
    if key=='cmd':
        keyboard.release(Key.cmd)
        time.sleep(0.25)
    if key=='shift':
        keyboard.release(Key.shift)
        time.sleep(0.25)
    if key=='tab':
        keyboard.release(Key.tab)
        time.sleep(0.25)
    if key=='ctrl':
        keyboard.release(Key.ctrl)
        time.sleep(0.25)
    if key=='up':
        keyboard.release(Key.up)
        time.sleep(0.25)
    if key=='alt':
        keyboard.release(Key.alt)
        time.sleep(0.25)
        
        
        
def presstab(times,sc=0):
    if sc==0:
        for _ in range(times):
            keyboard.press(Key.tab)
            time.sleep(0.1)
            keyboard.release(Key.tab)
    else:
        presshold('shift')
        for _ in range(times):
            keyboard.press(Key.tab)
            time.sleep(0.1)
            keyboard.release(Key.tab)
        pressrel('shift')
        
##Start       
time.sleep(1)
keyboard = Controller()
presshold("cmd")
pressl('s')
pressrel('cmd')
keyboard.type('notepad')
time.sleep(1)
pressk('enter')
time.sleep(0.5)
keyboard.type('Update to Tester')
presshold('ctrl')
pressl('s')
pressrel('ctrl')
presstab(10)
for x in range(30):
    pressk('up')
pressk('down')
pressk('enter')
presstab(12, 1)
keyboard.type('name.txt')
pressk('enter')
pressk('left')
pressk('enter')
presshold('alt')
pressk('f4')
pressrel('alt')