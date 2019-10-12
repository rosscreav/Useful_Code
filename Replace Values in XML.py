'''
Created on 23 May 2019

@author: rcreaven
'''
'''List of XML variables to be assigned###
FALOC=Location of the FA file
TALLOC=Location of the TAL file
PDXLOC=Location of PDX file
ENTRYTICKET=Location of ek6 file
NAME=RVC-Vers
FPR=Location for fpr
'''
import xml.etree.ElementTree as ET
##Writes the input values into the XML##
def XML_Write(fa_loc,talloc,pdxloc,ek6loc,name,fprloc):
    tree=ET.parse("Custom_FAT.xml")
    root=tree.getroot()
    xmlstr = ET.tostring(root, encoding='utf8', method='xml')
    print xmlstr
    xmlstr=xmlstr.replace("%FALOC%", fa_loc)
    xmlstr=xmlstr.replace("%TALLOC%", talloc)
    xmlstr=xmlstr.replace("%PDXLOC%", pdxloc)
    xmlstr=xmlstr.replace("%ENTRYTICKET%", ek6loc)
    xmlstr=xmlstr.replace("%NAME%", name)
    xmlstr=xmlstr.replace("%FPR%", fprloc)
    print xmlstr
    tree = ET.ElementTree(ET.fromstring(xmlstr))
    tree.write('C:\Users\\rcreaven\Documents\Jenkins_Builds\Config\FAT_TEST.xml', encoding='utf8', method='xml')