from faker import Faker
# from random import randint

# lst = [expression1 expression2 expression3]
# lst = [randint(10, 50) for _ in range(15)]
# print(lst)
# lst1 = [el for el in lst if el % 2]
# print(lst1)

CM_PER_INCH = 2.54


def get_students_list(cnt):
    f = Faker()
    # lst = [f.name() for i in range(cnt)]
    # for i in range(cnt):
    #     lst.append(f.name())

    return [f.name() for i in range(cnt)]


def inc2cm(value):
    return value * CM_PER_INCH
