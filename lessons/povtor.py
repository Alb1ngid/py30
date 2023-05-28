class Car:
    motor = True  # свойство

    def __init__(self, model, color, age):  # конструктор класса
        self.model = model
        self.color = color
        self.age = age

    def __str__(self):
        return f"{self.model} {self.age} ,{self.color} " \
               f"{self.motor}"


c = 1

c2 = Car('bmw', 'color', 2015)
c3 = Car('kia', 'red', 2020)
c4 = Car('fit', 'blue', 2010)

print(c2.model, c2.age, c2.motor, c2.color)
print(c2)


# парадигмы ооп
# наследование
# полиморфизм
class Car2(Car):

    def __init__(self, model, color, age, fly):
        super().__init__(model, color, age)
        self.fly = fly

    def flying(self):
        print('fly is', self.fly)

    def run(self):
        return f'it is {self.model}'


car = Car2('Ferrari', 'red', 2020, True)
car.flying()


# инкапсуляция
# публичный
# защищенный
# скрытый

class AA:
    def __init__(self, name, age, money):
        self.name = name
        self._age = age
        self.__money = money

    def __str__(self):
        return f"{self.name} {self._age} {self.__money}\n" \
               f"#####################################"


a = AA('Бека', 19, 1_000_000_000)
print(a._age)
a.name = 'Бегимай'
a._age = 111
a._AA__money = 0
print(a)

print(dir(a))