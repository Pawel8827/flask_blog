from abc import abstractmethod
import win32com.client as win32
import os 
excel = win32.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(os.path.join(os.getcwd(),'lista.xlsx'))

#wb = excel.Workbooks.Add()
#wb.SaveAs(os.path.join(os.getcwd(),'data.xlsx'))
ws_sheet1= wb.Worksheets('Arkusz1')
a=[]
def szukanie():
    for x in range(2,1000):
        for y in range(1, 5):
            abc = ws_sheet1.Cells(x, y).Value
            if abc is not None:
                print(abc)
                


szukanie()
print(a)

#wb.Save()
wb.Close()

