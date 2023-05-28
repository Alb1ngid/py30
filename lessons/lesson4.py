# множественное наследование

class A:#супер класс
    def __init__(self, a):
        self.a = a

    def runrun(self):
        self.run()

    def run(self):
        print('run')

class B:
    def __init__(self, a):
        self.b = a

    def run(self):
        print('fly')


class C(B, A):# Dочерний класс
    def __init__(self, a,b):
        B.__init__(self,b)
        A.__init__(self,a)


    def run(self):
        print('aaaaaaaaaaaaa')


# MRO-method resolution order
# порядок выполнения методов

c = C('a','b')
c.run()



class Grand:...

class Father(Grand):...

class Son(Father,Grand):...

c11=Grand
print(c11)
print(Son.mro())
print(object)