import os, sys
import datetime
path = 'D:\pulpit\Desktop'
wiek = 1
dzisiaj = datetime.datetime.now()
class licz:
    for files in os.listdir(path):
         if files.endswith('xlsx'):
            files_path=os.path.join(path,files)
            file_create= datetime.datetime.fromtimestamp(os.path.getatime(files_path))
            print(files_path,dzisiaj-file_create)
            dif_days = (dzisiaj-file_create).days
            print(dif_days)
            if dif_days >= wiek:
                os.remove(files_path)

sys.exit()
print(licz)