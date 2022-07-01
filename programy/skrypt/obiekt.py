from math import ceil

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.semestr = 1

    def hello(self):
        return f'{self.first_name} {self.last_name}'

    def go_higher(self):
        self.semestr += 1

    def go_down(self):
        self.semestr -= 1

    def get_year(self):
        return ceil(self.semestr / 2)
       

janek = Student(first_name='janko', last_name='Muzykant')
print('Semestr', janek.semestr)
janek.go_higher()
janek.go_higher()
print('Semestr', janek.semestr)
print('Rok', janek.get_year())