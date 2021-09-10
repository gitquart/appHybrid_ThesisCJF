import pandas as pd
import postgresql as db


directory='C:\\Users\\1098350515\\Documents\\thesis_postgresql\\Thesis\\'
excel_name='tbThesis_6_sep_2021_5_PERIOD_copy'
excel=excel_name+'.xlsx'
completePath=directory+excel
excelDF=pd.DataFrame()
print(f'-------Loading excel in RAM for reading : {excel_name} -----------')
excelDF=pd.read_excel(completePath,sheet_name='main')
excelDF.fillna('No value',inplace=True)
print('------------------EXCEL LOADED-----------------------')
rowCount=0
lsField=list()
#Start - Building record
for column in excelDF.columns:
    lsField.append(column)
for index,row in excelDF.iterrows():
    #Start - Check if thesis exists in database before building the record
    id_thesis=None
    heading=None
    id_thesis=row['id_thesis']
    heading=row['heading']
    query=f"select id_thesis from tbthesis where id_thesis={id_thesis} and heading='{heading}'"
    res=None
    res=db.getQuery(query)
    #End - Check if thesis exists in database before building the record
    if len(res)>0:
        print(f'Record already in database. ID {str(id_thesis)}')
    else:
        #Start - Building record 
        lsValue=list()
        for field in lsField:
            strValue=None
            #START- CASES
            #INTEGER CASE
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
            #END - CASES     
            lsValue.append(strValue)
        #End - Building record 
        #Start - Inserting to table 
        #SECOND CLEANING        
        for item in lsValue:        
            if isinstance(item,str):
                lsValue[lsValue.index(item)]="'"+str(item).strip()+"'"
            else:
                lsValue[lsValue.index(item)]=str(item).strip()

        st=None
        fieldQuery=None
        valuesQuery=None
        fieldQuery=','.join(lsField)
        valuesQuery=','.join(lsValue)
        st=f'insert into tbthesis ({fieldQuery}) values ({valuesQuery}) ' 
        res=None
        res=db.executeNonQuery(st) 
        #End - Inserting to table    
        if res:     
            rowCount+=1
            print(f'Row done {str(rowCount)} . ID {str(lsValue[3])}')  
        else:
            print('Something went wrong')   

print(f'--------------------FILE COMPLETE: {excel_name}, TOTAL ROWS : {str(rowCount)}------------------------')               
   