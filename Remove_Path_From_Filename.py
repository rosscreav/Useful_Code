'''
Created on 26 Jun 2019

@author: rcreaven
'''
import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)