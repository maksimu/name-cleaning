__author__ = 'Maksim Ustinov'

import sys, getopt, xlrd, xlwt, csv, argparse
from nameparser import HumanName
from xlutils.copy import copy
from xlrd import *

## Before running make sure all dependencies are installed: pip install nameparser xlutils

parser = argparse.ArgumentParser(description='Script to break up single string name into different part of the name. .')
parser.add_argument('-f','--fncol', type=int, help='Column number where the First name will be placed',required=True)
parser.add_argument('-l','--lncols', type=int, help='Column number where the Last name will be placed', required=True)
parser.add_argument('-m','--mncol', type=int, help='Column number where the Middle name will be placed', required=False, default=-1)
parser.add_argument('-s','--sncol', type=int, help='Column number where the Suffix will be placed', required=False, default=-1)
parser.add_argument('-wn','--worksheetname',help='Name of a Worksheet that will be used to extract a string name and also used to write extracted name parts. '
                                                 '\nNOTE: Strings that contain spaces inside will need to be surrounded with quotation marks', required=True)
parser.add_argument('-if','--inputfile', help='Input Excel file to read', required=True)
parser.add_argument('-of','--outputfile', help='Output duplicated Excel file to write extracted parts of the name ', required=True)
args = parser.parse_args()

worksheet_name = args.worksheetname     #'Merged Final'
inputFile = args.inputfile              #"CISCO-99-working.xlsx"
output_file = args.outputfile

# where to place converted names
first_name_row_num = args.fncol
last_name_row_num = args.lncols
middle_name_row_num = args.mncol
suffix_name_row_num = args.sncol

workbook_to_write = copy(open_workbook(inputFile))
workbook = xlrd.open_workbook(inputFile)

worksheet = workbook.sheet_by_name(worksheet_name)

num_rows = worksheet.nrows - 1
curr_row = -1

#start looping through rows of data
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    cell = worksheet.cell(curr_row, 1)
    orig_name = cell.value
    clear_name = HumanName(orig_name)
    print "--> " ,clear_name
    worksheet_to_write = workbook_to_write.get_sheet(1)

    if first_name_row_num != -1:
        if curr_row == 0:
            worksheet_to_write.write(curr_row, first_name_row_num, "Extracted First Name")
        else:
            print("clear_name.first = " + clear_name.first)
            worksheet_to_write.write(curr_row, first_name_row_num, clear_name.first)

    if last_name_row_num != -1:
        if curr_row == 0:
            worksheet_to_write.write(curr_row, last_name_row_num, "Extracted Last Name")
        else:
            print("clear_name.last = " + clear_name.last)
            worksheet_to_write.write(curr_row, last_name_row_num, clear_name.last)

    if middle_name_row_num != -1:
        if curr_row == 0:
            worksheet_to_write.write(curr_row, middle_name_row_num, "Extracted Middle Name")
        else:
            print("clear_name.middle = " + clear_name.middle)
            worksheet_to_write.write(curr_row, middle_name_row_num, clear_name.middle)

    if suffix_name_row_num != -1:
        if curr_row == 0:
            worksheet_to_write.write(curr_row, suffix_name_row_num, "Extracted Suffix")
        else:
            print("clear_name.suffix = " + clear_name.suffix)
            worksheet_to_write.write(curr_row, suffix_name_row_num, clear_name.suffix)

workbook_to_write.save(output_file)

print "Done. See final output in ", output_file