# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:42:37 2016

@author: Jinxiu Liu
"""

import os

# define result directory
result_dir = "/home/geo"

### Part 1 
#open data file
with open("data.csv", "r") as infile:
    data = infile.read()
    datalist = data.splitlines()


# Loop over lines in file, append to lists 
for i in range(2,len(datalist)):
    # go over the header
   line = datalist[i]
   splitline = line.split(",")
   date = splitline[5]
   # create year from date
   year = date[0:4]
   filename = 'AA-'+ year +'.csv'
   # create file path for each year file 
   output = os.path.join(result_dir, filename)
   with open(output, 'a') as w:
    # Write and append lines into that file
       w.write(line + "\n")



# part 2

import glob

summer = "/home/geo/summer.csv"
winter = "/home/geo/winter.csv"
path = glob.glob(result_dir + "/AA*.csv")

with open(summer,'w') as s:
    with open(winter,'w') as w:
        for fp in path:
            s_temp = []
            w_temp = []
            with open(fp,'r') as f:
                for line in f:
                    split = line.split(',')
                    date = split[5]
                    year = date[0:4]
                    month = date[4:6]
                    if month == '01' or month == '02':
                        temp = float(split[6])
                        # append the temperature to winter file
                        w_temp.append(temp)
                    elif month == '07' or month == '08':
                        temp = float(split[6])
                        # append the temperature to summer file
                        s_temp.append(temp)
                avg_s_temp = sum(s_temp)/len(s_temp)
                avg_w_temp = sum(w_temp)/len(w_temp)
                s.write(year + "," + "{:.2f}".format(avg_s_temp) + "\n")
                w.write(year + "," + "{:.2f}".format(avg_w_temp) + "\n")
                    
            