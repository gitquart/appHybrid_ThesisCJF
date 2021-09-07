from numpy import nan
import pandas as pd
import openpyxl as excelpy


directory='C:\\Users\\1098350515\\Documents\\thesis_postgresql\\Thesis\\'
excel_name='tbThesis_6_sep_2021_ALL_PERIOD'
excel=excel_name+'.xlsx'
completePath=directory+excel
excelDF=pd.DataFrame()
print('-------Loading excel in RAM for reading...-----------')
excelDF=pd.read_excel(completePath,sheet_name='main')
print('------------------EXCEL LOADED-----------------------')
rowCount=0
lsField=list()
for column in excelDF.columns:
    lsField.append(column)
for index,row in excelDF.iterrows():
    lsValue=list()
    for field in lsField:
        strValue=None
        if field=='id_thesis' or field=='period_number':
            strValue=int(row[field])
        elif field=='lst_precedents':
            #For this case, it adds a list to the current lsValue and it continues
            strValue=str(row[field]).replace('[','').replace(']','').replace("'",'')
        elif field=='multiple_subjects':
            strValue=bool(row[field])
        else:        
            #String case
            strValue=row[field] 
        if strValue==nan:
            strValue=''    
        lsValue.append(strValue)
    rowCount+=1
    print(f'Row done {str(rowCount)}')    
   