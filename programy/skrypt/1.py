import shutil, datetime
def wpisz_informacje(**kwargs):
    for klucz in kwargs:
        print(f' Pod klucz {klucz} znajduje się {kwargs[klucz]}')

wpisz_informacje( imie='pawel', nazwisko='grabowski')

shutil.copy('haslo.txt', 'tests.txt')

x = datetime.datetime.now()
print(x.strftime("%Y"))
