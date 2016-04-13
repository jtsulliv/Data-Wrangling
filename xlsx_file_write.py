'''This script finds all of the xlsm files in a directory and 
then writes them all to one master xlsx file
'''

from pyexcel_xlsx import get_data
import pyexcel as pe
from pyexcel.ext import xlsx

import numpy as np
import glob


# Finding all of the file names in a directory

def find_excel_files():
    x = glob.glob("*.xlsm")
    return x
    

# Wrting the files to one excel file

def read_write():
    files = find_excel_files()
    print type(files)
    print type(files[0])
    content = {}
    for i in files:
        data = pe.get_sheet(file_name = i)
        name = i[0:(i.find('.'))]
        content[name] = data
    book = pe.get_book(bookdict = content)
    book.save_as('output.xlsx')


       
read_write()

