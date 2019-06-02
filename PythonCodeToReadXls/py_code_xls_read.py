# purpose : Code to read and sum a specific column  from all the xlsx file present in folder
# usage : python py_code_xls_read.py Folder_Path
# author : Pranjali Vakil
# library : xlrd

#import library
import xlrd
import os
import sys

#Create empty filelist
files = []
sum_list = []
final_all_files_sum = 0

for file_name in os.listdir(sys.argv[1]):
    if file_name.endswith('.xlsx'):
        files.append(open(file_name))
	#read file
	workbook = xlrd.open_workbook(file_name,"rb")

	#read sheet names in file
	sheets = workbook.sheet_names()

	#create empty list of data
	required_data = []
	sum = 0

	#read sheets one by one
	for sheet_name in sheets:
    	    sh = workbook.sheet_by_name(sheet_name)
    	
	#read iteration by rows
	for i in range(1, sh.nrows):                  #-->select range of rows here
    		columns = []
		#read iteration by columns
    		for j in range(8,9):                  #-->Select Column Number here
    		    columns.append(sh.cell(i, j).value)

		#Append data in List final
    		required_data.append(columns)

	#print the list i.e. Column data
	for data in required_data:
		sum = sum + data[0]

	sum_list.append(sum)
	#print sum for each file
	print file_name + "sum -> " + str(sum)

#Add sum of all files
for element in sum_list:
	#print element
	final_all_files_sum = final_all_files_sum + element

#Print Final Sum of All files
print "Sum of All files			:" + str(final_all_files_sum)
