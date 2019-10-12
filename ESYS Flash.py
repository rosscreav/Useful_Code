'''
Created on 22 May 2019

@author: rcreaven
'''
import os

###################################
##Flash
def Start_Flash():
    filesfolder="C:\Users\\rcreaven\Documents\Jenkins_Builds\Flash_Files"
    for file_search in os.listdir(filesfolder):
        if file_search.endswith(".pdx"):
            pdxloc=(os.path.join(filesfolder,file_search))
    
    for file_search in os.listdir(filesfolder):
        if file_search.endswith(".tal"):
            talloc=(os.path.join(filesfolder,file_search))     
    
    for file_search in os.listdir(filesfolder):
        if file_search.endswith(".xml"):
            fa_loc=(os.path.join(filesfolder,file_search))
    vin='I020'
    templatename=pdxloc.strip('C:\Users\\rcreaven\Documents\Jenkins_Builds\Flash_Files\\')
    templatename=templatename.strip('.pdx')
    templatename='I020_'+templatename
    print 'templatename:' +templatename
    esysbat='C:\EC-Apps\ESG\E-Sys\E-Sys.bat'
    os.system('{} -pdximport {} -project {}'.format(esysbat,pdxloc,templatename))
    print 'PDX Loaded'
    result=os.system('{} -tal {} -fa {} -project {} -vehicleinfo {}'.format(esysbat, talloc,fa_loc,templatename,vin))
    return result

def Flash_Status(status):
    skipfat=True
    if status==0:
        print 'Flash successful'
        skipfat=False
    elif status==1:
        print 'Flash has failed'
        print'Because of an error the action could not be finished.'
    elif status==2:
        print 'Flash has failed'
        print 'The action has been executed with errors.'
    elif status==3:
        print 'Flash has failed'
        print 'No connection to the server.'
    elif status==4:
        print 'Flash has failed'
        print 'The action has been executed without errors but with warnings.'
    else:
        print 'Unknown return value'
        print 'Value {} returned'.format(str(status))
    return skipfat

##TODO Flash test##
print 'HERE IS FLASH TEST'
status=Start_Flash()
skipfat=Flash_Status(status)

if skipfat==True:
    for i in range(3):
        status=Start_Flash()
        Flash_Status(status)
        if status==0:
            skipfat=False
            break

if skipfat!=False:
    print 'Flash failed 4 times closing'
