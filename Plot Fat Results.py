'''
Created on 6 Jun 2019

@author: rcreaven
'''

import os
from os.path import isfile, join
from os import listdir,mkdir
from shutil import copyfile, rmtree 
import xlrd
import matplotlib.pyplot as plt
import shutil
from matplotlib.patches import Wedge

listoffileswithpre=[]

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
    ##Loop Through all X results
    for x in results:
        if x=='N/A':
            N_A=N_A+1
        elif x.lower()=='FAIL'.lower():
            failed=failed+1
        elif x=='PRE' or x=='ERR':
            listoffileswithpre.append(xlsname)
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
    results=[passed,green_yellow_fail,yellow_fail,orange_fail,red_fail,N_A,failed]
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
    for x in List:
        data=x[1]
        passed=passed+data[0]
        green_yellow_fail=green_yellow_fail+data[1]
        yellow_fail=yellow_fail+data[2]
        orange_fail=orange_fail+data[3]
        red_fail=red_fail+data[4]
        N_A=N_A+data[5]
        failed=failed+data[6]
    totals=[passed,green_yellow_fail,yellow_fail,orange_fail,red_fail,N_A,failed]
    entry=['Total',totals]
    List.insert(0,entry)
    return List

def plot_results(results):
    #[PASSED,GREEN YELLOW FAIL,YELLOW FAIL,ORANGE FAIL,RED FAIL,N/A]
    colors='#44C55E','#B2C646','#BFC849','#BD713A','#AE3535','#7A7A7A','#ce93ff'
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
   
    ax[0,0].axis('off')
    ax[0,1].axis('off')
    ax[0,3].axis('off')
    ax[0,4].axis('off')
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.savefig('C:\Users\\rcreaven\Documents\Jenkins_Builds\Results\Fat_Result.png',bbox_inches='tight')
















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
print listoffileswithpre