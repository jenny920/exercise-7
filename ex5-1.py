# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:42:08 2016

@author: root
"""

with open("data.csv", "r") as infile:
    data = infile.read()
    datalist = data.splitlines()

# Create empty lists to store file data
Year = []
Name = 'AA-'
Filename = ''

# Loop over lines in file, append to lists 
for line in datalist:
    splitline = line.split(",")
    Year.append(splitline[5][0:3])
    #Create a varaible that is contains a 
    #character string of the name of the 
    #output file for that year
    Filename = Name+str(Year.append)+'.csv'
    w = open(Filename, 'w')
    with open(Filename, 'w') as w:
        # Write a line of text into that file
        #Write the entire line to that data file
        my_line = splitline
w.write(my_line)