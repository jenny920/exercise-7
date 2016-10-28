# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:42:37 2016

@author: root
"""

with open("data.csv", "r") as infile:
    data = infile.read()
    datalist = data.splitlines()
    
Year = []
Name = 'AA-'
Filename = ''

# Loop over lines in file, append to lists 
for line in datalist:
    splitline = line.split(",")
    Year.append(splitline[5][0:4])
    #Create a varaible that is contains a 
    #character string of the name of the 
    #output file for that year
    Filename = Name+str(Year.append)+'.csv'

date = splitline[5]
print(date)
print(date[0:3])
print(splitline[5][0:3])
print(splitline[5][0:4])
print(splitline[5][1:4])
