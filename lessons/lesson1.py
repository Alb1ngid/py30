# OOP - обьектно ориентированное программирование

# def a(s, b):
#     m = s * b
#     print(m)
#
#
# p1 = a(4, 4)
# p2 = a(6, 6)
#
# t = 1
# t2 = 'str'
# t3 = 2.3
# t4 = True
# t5 = ()
# t6 = []
# t7 = {}
# print(type(t5))


class Person:
    head = True  # свойства

    def __init__(self, name, age):  # конструктор
        self.name = name
        self.age = age

    def __str__(self):  # магические методы
        return f'name is {self.name}\n' \
               f'age is {self.age}\n'

    def age2(self):  # метод
        self.age *= 2

    def nameis(self):
        self.name = 'ислам'

    def __len__(self):
        return len(f'{(self.name)} {self.age}')


person = Person('beka', 19)
person2 = Person('Азимбек', "17")
person3 = Person('Руслан', 19)
print(person)
person.age2()
person.age2()
person.age2()
person.nameis()
print(person)
print(person2)
print(person3)

print(len(person2))