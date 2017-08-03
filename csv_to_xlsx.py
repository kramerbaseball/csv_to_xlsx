import csv
import glob
import openpyxl
import os, sys
import pandas as pd
import xlsxwriter as xlwr

def main():

	list_of_files = []
	names = []
	for csv_file in glob.glob(os.path.join('.', '*.csv')):
		bleh = csv_file[2:]
		name = bleh[:-4]
		names.append(name)
		df = pd.read_csv(csv_file, index_col=None, header=0, encoding='utf-8')
		list_of_files.append(df)
	
	writer = pd.ExcelWriter('non_concussed_game_logs.xlsx')
	for n, df in enumerate(list_of_files):
		df.to_excel(writer, '%s' % names[n])
	writer.save()


if __name__ == "__main__":
    main()