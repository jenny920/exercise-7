# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:56:28 2016

@author: root
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:42:37 2016

@author: root
"""
import os,glob

with open("data.csv", "r") as data:
    data.readline()

    
# Loop over lines in file, append to lists 
for line in data:
    split = line.split(",")
    date = split[5]
    year = date[0:4]
    #Create a varaible that is contains a 
    #character string of the name of the 
    #output file for that year
    filename = 'AA-' + year + '.csv'


