import openpyxl as xl


wb = xl.load_workbook('lista.xlsx')
Arkusz = wb['Arkusz1']
abc = wb.active




assss =[]

def kom2():
    
    for col in Arkusz.iter_rows(min_row=2, max_row=100, min_col=1, max_col=4,
        values_only=True):
        if col[0] is not None and type(col[0])==int:
            print(col[0])
            assss.append(col)

    
kom2()