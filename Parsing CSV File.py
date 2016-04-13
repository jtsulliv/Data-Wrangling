# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:34:43 2016

@author: JSULLIVAN
"""

# LESSON 1 
#
# Parsing CSV files in Python
# CSV to Python dictionary

# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!


DATAFILE = "beatles-diskography.csv"        # CSV file name to read in



def parse_file(datafile):
    data = []
    N = 10 # only want the first 10 rows (excluding the header where the labels are)
    with open(datafile, "r") as f:
        next(f)
        head = [next(f) for x in xrange(N)] # This piece of code skips the first line
        for line in head:
            split_line = line.strip('\n') # removing the next line '\n' character
            split_line = split_line.split(",") # splitting the line on ',' 

            d = {}                              # need to start with empty dic for each line
            d['Title'] = split_line[0]          # putting in the first element into 'Title' of the dictionary
            d['Released'] = split_line[1]
            d['Label'] = split_line[2]
            d['UK Chart Position'] = split_line[3]
            d['US Chart Position'] = split_line[4]
            d['BPI Certification'] = split_line[5]
            d['RIAA Certification'] = split_line[6]
            data.append(d)
    return data # need to return the list of dictionaries 


# This function cleans the 'data' from above
# Python seems to interpret '-' as some weird character, so I needed to fix that
def clean_data():
    x = parse_file(DATAFILE) # reading in data from function above
    for i in x:
        if i['US Chart Position'] == '\xe2\x80\x94': 
            i['US Chart Position'] = '-' 
    return x
            

        
# Function to test the program     
def test():
    # a simple test of your implemetation
    d = clean_data()
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()
print 'test passed'


