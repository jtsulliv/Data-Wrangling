# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 13:52:02 2016

@author: jsullivan
"""

# Reading CSV with the CSV Module

import csv 
import pprint

DATAFILE = "beatles-diskography.csv"

''' This piece of code opens the file, reads each line in as a dictionary
and then appends the list 'data' with each dictionary'''

def parse_csv(filename):
    data = []
    n = 0 
    with open(filename,'rb') as f_in:
        r = csv.DictReader(f_in) 
        '''DictReader class reads data in as dictionaries
        and also assumes that the first row is the header row
        and those are the names we want to use for fields'''
        
        for line in r:
            data.append(line)
    return data
    

'''This piece of code prints 'data' out in 
an easy to read format'''
def pretty_print(filename):
    d = parse_csv(filename)
    pprint.pprint(d)
    
pretty_print(DATAFILE)
    

