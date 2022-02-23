class A:
    def __init__(self):
        print('A')

    def func(self):
        pass


class B(A):
    def __init__(self):
        super().__init__()
        print('B')

    def func(self):
        pass


class C(A):
    def __init__(self):
        super().__init__()
        print('C')

    def func(self):
        pass


class D(C, B):
    def __init__(self):
        super().__init__()
        print('D')
        self.dd = 0         # public
        self._bb = 99       # protected
        # self.__cc = 88      # private

    def func(self):
        # self.__cc = 66
        pass


d = D()
print(d.dd)
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]


a1 = A()
b1 = B()
c1 = C()
d1 = D()
lst = [a1, b1, c1, d1]
for el in lst:
    el.func()

print(dir(d1))
# print(d1.__cc)
print(d1._D__cc)
