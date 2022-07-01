import win32com.client as win32
import os 
excel = win32.Dispatch('Excel.Application')
outlook = win32.Dispatch('Outlook.Application')
wb = excel.Workbooks.Open(os.path.join(os.getcwd(),'ttprzelew.xlsx'))
ws_sheet1= wb.Worksheets('Arkusz1')



pola= ws_sheet1.Range(
        ws_sheet1.Cells(3,1),
        ws_sheet1.Cells(100,7)
                ).Value

for i in pola:
        if i[0] is not None:
            print(i)

wb.Close()