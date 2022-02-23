from datetime import date
from abc import ABC, abstractmethod


class Student:
    # name = ''
    # age = 0
    # phone = ''
    # school = ''
    PHONE_PREFIX = '+38 '

    # def __new__(cls, *args, **kwargs):
    #     pass

    def __init__(self, name, age, phone, school):
        self.__name = name
        self._age = age
        self.phone = phone
        self.school = school

    def __add__(self, other):
        tmp = Student(
            self.__name + ' ' + other.__name,
            self._age + other._age,
            self.phone + ' ' + other.phone,
            self.school + ' ' + other.school
        )

        return tmp

    def __str__(self):
        return self.__name + ' ' + str(self._age) \
               + ' ' + self.school + ' ' + self.phone

    def get_name(self):
        return self.__name

    @staticmethod
    def func1(x, y):
        return x + y

    @classmethod
    def func2(cls, name, year, phone, school):
        return cls(name, date.today().year - year, phone, school)


# a = b = 5

st1 = Student('Ivan', 15, '4564356', 'Odessa')
st2 = Student('Petr', 10, '43524', 'Kiev')
st3 = Student('Sergey', 11, '34574657', 'Odessa')

# print(st1.name, id(st1.name), id(st1))
# # Student.name = 'Petr'
# print(st1.name, id(st1.name), id(st1))
# print(st2.name, id(st2.name), id(st2))
# print(st3.name, id(st3.name), id(st3))
print(st1.PHONE_PREFIX)
print(st2.PHONE_PREFIX)
st1.PHONE_PREFIX = '56'
print(st1.PHONE_PREFIX)
print(st2.PHONE_PREFIX)


# st1.name = 'Ivan'
# st2.name = 'Petr'
# st3.name = 'Oleg'
# print(st1.name, id(st1.name), id(st1))
# print(st2.name, id(st2.name), id(st2))
# print(st3.name, id(st3.name), id(st3))
#

print(dir(st1))

res = st1 + st2
print(res._Student__name)
print(res.phone)
print(res._age)
print(res.school)

print(st1)

print(st1.get_name())

print(Student.func1(3, 6))
print(st1.func1(6, 2))

st4 = Student.func2('Olga', 1999, '34564534', 'Odessa')
print(st4)


class Scraper(ABC):

    @abstractmethod
    def get_rate(self):
        pass


class S1(Scraper):
    def get_rate(self):
        pass


s1 = S1()
