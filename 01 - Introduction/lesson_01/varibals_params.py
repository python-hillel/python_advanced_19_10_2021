# *args, **kwargs


# def func(b, c):
#     a = b + c
#     return a


def func1(*args):
    print(args)
    print(*args)


def func2(**kwargs):
    print(kwargs)
    print(dict(**kwargs))


def func3(**kwargs):
    print(kwargs)
    func2(**kwargs)


func1(1, 2, 3, 4)
func2(a=1, b=2, c=3)
func3(v=7, h=8, e=6)