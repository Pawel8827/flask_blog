import string, random, pyqrcode

aaa = string.digits
print(aaa)
ilosc = 10
field = input("tu wpisz text ")
haslo = "".join(random.sample(aaa,ilosc))
img = pyqrcode.create(haslo)
img.png(field + '.png', scale = 6)

print(haslo)