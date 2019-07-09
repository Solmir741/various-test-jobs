# -*- coding: utf-8 -*-
"""
Редактор Spyder


"""
import openpyxl, xlrd
import numpy as np
wb = openpyxl.load_workbook(filename = 'requests.xlsx')
i=1
sheet1 = wb["Лист1"]
rb = xlrd.open_workbook('requests.xlsx')
sheet2 = rb.sheet_by_index(0)
i=0
val = sheet1['A' + str(i+1)].value
while sheet1['A' + str(i+1)].value != None:
    val = sheet2.row_values(i)
    perc = np.percentile(val, 90)
    median = np.median(val)
    average = np.average(val)
    max_ = np.max(val)
    min_ = np.min(val)
    print ('90 percentile <' + str(np.round((perc), 2)) + '>')
    print ('median <' + str(np.round((median), 2)) + '>')
    print ('average <' + str(np.round((average), 2)) + '>')
    print ('max <' + str(np.round((max_), 2)) + '>')
    print ('min <' + str(np.round((min_), 2)) + '>')
    #print('median <' + str(median) + '>')
    #print('average <' + str(average) + '>')
    #print('max <' + str(max_) + '>')
    #print('min <' + str(min_) + '>')
    i += 1