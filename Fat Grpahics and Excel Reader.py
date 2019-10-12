'''
Created on 29 May 2019

@author: rcreaven
'''
import zipfile
import os
from os.path import isfile, join
from os import listdir,mkdir
from shutil import copyfile, rmtree 
import xlrd
import matplotlib.pyplot as plt
import numpy as np
import shutil


listoffileswithpre=[]

def get_result_xls(name):
    results=[]
    mypath='C:\Users\\rcreaven\Documents\Jenkins_Builds\\Results\\{}'.format(name)
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for x in onlyfiles:
        if 'xls' in x and 'result' in x:
            results.append(x)
    try:
        rmtree("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Xls _Results")
        mkdir("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Xls _Results")
    except:
        mkdir("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Xls _Results")
    names=[]
    for files in results:
        num=files.find('_',7)
        num=files.find('_',num+2)
        names.append(files[0:num])
    
    i=0
    fileloc=[]
    for filename in results:
        src=mypath+"\\"+filename
        dst="C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Xls _Results\\{}.xls".format(names[i])
        copyfile(src,dst)
        fileloc.append(dst)
        i=i+1


##Get graphs from xls files

def pullresults(xls):
    xlsname=xls[71:-4]
    filename=xlrd.open_workbook(xls)
    sheet=filename.sheet_by_index(0)
    results=[]
    while True:
        for x in range(2,1000):
            try:
                
                cell=sheet.cell(x,2)
                string=str(cell)
                string=string[7:-1]
                results.append(string)
            except:
                break
        break
    
    passed=0
    green_yellow_fail=0
    yellow_fail=0
    orange_fail=0
    red_fail=0
    N_A=0
    failed=0
    pre=0
    err=0
    ##Loop Through all X results
    for x in results:
        if x=='N/A':
            N_A=N_A+1
        elif x.lower()=='FAIL'.lower():
            failed=failed+1
        elif x=='PRE' or x=='ERR':
            listoffileswithpre.append(xlsname)
            if x=='PRE':
                pre=pre+1
            else:
                err=err+1
        elif int(x)==8:
            passed=passed+1
        elif int(x)==7:
            green_yellow_fail=green_yellow_fail+1
        elif int(x)==6:
            yellow_fail=yellow_fail+1
        elif int(x)==5:
            orange_fail=orange_fail+1
        elif int(x)<5:
            red_fail=red_fail+1
          
        
    ##OUTPUT=[PASSED,YELLOW FAIL,ORANGE FAIL,RED FAIL,N/A]
    results=[passed, green_yellow_fail, yellow_fail, orange_fail, red_fail, N_A, failed, pre, err]
    output=[xlsname,results]
    return output

  
def get_total(List):
    passed=0
    green_yellow_fail=0
    yellow_fail=0
    red_fail=0
    N_A=0
    orange_fail=0
    failed=0
    pre=0
    err=0
    for x in List:
        data=x[1]
        passed=passed+data[0]
        green_yellow_fail=green_yellow_fail+data[1]
        yellow_fail=yellow_fail+data[2]
        orange_fail=orange_fail+data[3]
        red_fail=red_fail+data[4]
        N_A=N_A+data[5]
        failed=failed+data[6]
        pre=pre+data[7]
        err=err+data[8]
    totals=[passed,green_yellow_fail,yellow_fail,orange_fail,red_fail,N_A,failed,pre,err]
    entry=['Total',totals]
    List.insert(0,entry)
    return List

def plot_results(results):
    #[PASSED,GREEN YELLOW FAIL,YELLOW FAIL,ORANGE FAIL,RED FAIL,N/A,FAILED,PRECONDITION,ERROR]
    colors='#44C55E','#B2C646','#BFC849','#BD713A','#AE3535','#7A7A7A','#ce93ff','#bffff4','#ffa3fd'
    fig1, (ax) = plt.subplots(3,5)     
    ##Results
    data=results[0]
    ax[0,2].pie(data[1], startangle=90,colors=colors)
    ax[0,2].axis('equal')
    ax[0,2].title.set_text(data[0])
    data=results[1]
    ax[1,0].pie(data[1],  startangle=90,colors=colors)
    ax[1,0].axis('equal')
    ax[1,0].title.set_text(data[0])
    data=results[2]
    ax[1,1].pie(data[1],  startangle=90,colors=colors)
    ax[1,1].axis('equal')
    ax[1,1].title.set_text(data[0])
    data=results[3]
    ax[1,2].pie(data[1],  startangle=90,colors=colors)
    ax[1,2].axis('equal')
    ax[1,2].title.set_text(data[0])
    data=results[4]
    ax[1,3].pie(data[1],  startangle=90,colors=colors)
    ax[1,3].axis('equal')
    ax[1,3].title.set_text(data[0])
    data=results[5]
    ax[1,4].pie(data[1],  startangle=90,colors=colors)
    ax[1,4].axis('equal')
    ax[1,4].title.set_text(data[0])
    data=results[6]
    ax[2,0].pie(data[1],  startangle=90,colors=colors)
    ax[2,0].axis('equal')
    ax[2,0].title.set_text(data[0])
    data=results[7]
    ax[2,1].pie(data[1],  startangle=90,colors=colors)
    ax[2,1].axis('equal')
    ax[2,1].title.set_text(data[0])
    data=results[8]
    ax[2,2].pie(data[1],  startangle=90,colors=colors)
    ax[2,2].axis('equal')
    ax[2,2].title.set_text(data[0])
    data=results[9]
    ax[2,3].pie(data[1],  startangle=90,colors=colors)
    ax[2,3].axis('equal')
    ax[2,3].title.set_text(data[0])
    data=results[10]
    ax[2,4].pie(data[1],  startangle=90,colors=colors)
    ax[2,4].axis('equal')
    ax[2,4].title.set_text(data[0])
    ##Legend
    '''
    lengths=[1,1,1,1,1,1,1,1]
    labels=['Passed','Fail (BI=7)','Fail (BI=6)','Fail (BI=5)','Fail (BI<5)','Not Applicable','Test Failed','Precondition Fail','Error']
    y_pos= np.arange(len(labels))
    ax[0,4].barh(y_pos,height=lengths,width=lengths,align='center')
    ax[0,4].set_yticks(labels)
    ax[0,4].invert_yaxis()
    '''
    
    ax[0,0].axis('off')
    ax[0,1].axis('off')
    ax[0,3].axis('off')
    ax[0,4].axis('off')
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.savefig('C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Fat_Result.png',bbox_inches='tight')
    
##Start
##Unzips and extracts XLS files

def get_fat_results():
    mypath='C:\\Users\\rcreaven'
    all_subdirs = next(os.walk(mypath))[1]
    results=[]
    print all_subdirs
    for filename in all_subdirs:
        if 'RVC' in filename:
            filename=mypath+'\\'+filename
            results.append(filename)
    latest_dir = max(results, key=os.path.getctime)
    name=latest_dir.strip("C:\\Users\\rcreaven\\")
    if os.path.isdir("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results"):
        while True:
            try:
                rmtree("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results")
                mkdir("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results")
                mkdir("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Xls _Results")
                break
            except:
                print 'looping'
                continue
    else:
        while True:
            try:
                mkdir("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results")
                mkdir("C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Xls _Results")
                break
            except:
                print 'looping'
                continue

    dst_dir="C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\\"+str(name)
    print latest_dir
    print dst_dir
    shutil.copytree(latest_dir,dst_dir)
    return name

def zip_file(name):
    root="C:\Users\\rcreaven\Documents\Jenkins_Builds\Results"
    filename=root+"\\"+name
    shutil.make_archive(filename, 'zip', filename)
    
    
    

name=get_fat_results()
get_result_xls(name)
mypath="C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Xls _Results"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

results=[]
for xls in onlyfiles:
    xls=mypath+'\\{}'.format(xls)
    output=pullresults(xls)
    results.append(output)
results=get_total(results)
print results
plot_results(results)

if len(listoffileswithpre)>0:
    print listoffileswithpre
    print 'All of the files in the above brackets have a precondition not met or Errored in some way'



