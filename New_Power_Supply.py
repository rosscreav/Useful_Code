'''
Created on 22 May 2019

@author: rcreaven
'''
import serial
import time

def set_BDC_supplly(V,I):
    s=serial.Serial(0)
    s.write('INST CH1')
    s.write("VOLT "+str(V)+"\r\n")
    s.write("CURR "+str(I)+"\r\n")
    s.close()
    
def set_UCAP_supplly(V,I):
    s=serial.Serial(0)
    s.write('INST CH2')
    s.write("VOLT "+str(V)+"\r\n")
    s.write("CURR "+str(I)+"\r\n")
    s.close()
    
def set_output(OP):
    s=serial.Serial(0)
    s.write("OUTP "+str(OP)+"\r\n")
    s.close()

    
##Start
while True:
    set_BDC_supplly(12.50, 1)
    set_UCAP_supplly(12.50, 1)
    time.sleep(3)
    set_output(1)
    time.sleep(3)
    #set_output(0)
    


    
    time.sleep(5)
