import win32com.client as win32
import os 
excel = win32.Dispatch('Excel.Application')
outlook = win32.Dispatch('Outlook.Application')
wb = excel.Workbooks.Open(os.path.join(os.getcwd(),'lista.xlsx'))
ws_sheet1= wb.Worksheets('Arkusz1')

asd= ws_sheet1.Range(
    ws_sheet1.Cells(2,1),
    ws_sheet1.Cells(2,4)
).Value

