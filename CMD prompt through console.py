
##reskin of windows cmd prompt
import os
import sys 

i=0
while i==0:
    cmd=raw_input(">>>")
    if cmd== 'kill':
        sys.exit()
    else:
        os.system(cmd)