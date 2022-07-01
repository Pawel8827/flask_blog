import win32com.client as win32
import os, schedule, time
excel = win32.Dispatch('Excel.Application')
outlook = win32.Dispatch('Outlook.Application')
wb = excel.Workbooks.Open(os.path.join(os.getcwd(),'lista.xlsx'))


#wb = excel.Workbooks.Add()
#wb.SaveAs(os.path.join(os.getcwd(),'data.xlsx'))
ws_sheet1= wb.Worksheets('Arkusz1')


def szukanie():
    pola= ws_sheet1.Range(
        ws_sheet1.Cells(2,1),
        ws_sheet1.Cells(1000,4)
                ).Value

    for i in pola:
        if i[0] is not None:
            message = outlook.CreateItem(0)
            message.Display()
            message.To = i[1]
            message.Subject = i[2]
            message.Body = i[3]
                
                     
    wb.Close()
    
    
def test():
    name = outlook.GetNameSpace('Mapi')
    acaunt = name.Folders['Pgrabowski@um.warszawa.pl']
    odebrane = acaunt.Folders['Skrzynka odbiorcza']
    cde = odebrane.Folders['helpdesk']
    abc = odebrane.Items[0]
    print(abc.SenderEmailAddress)
    print(abc.Subject)
    
    

test()

