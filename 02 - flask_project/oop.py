import inspect


class Student:
    PHONE_NUMBER = '+38'

    def __init__(self, name):
        self.name = name


st = Student('Ivan')
st1 = Student('Petr')

st.PHONE_NUMBER = '+40'


def show_attr(obj):
    print('Type:', type(obj))
    # print('Name:', end=' ')
    if inspect.isclass(obj):
        print(obj.__name__)
    else:
        print(obj.__class__.__name__)
    print('-' * 10, 'ATTR', '-' * 10)
    for attr_name in dir(obj):
        value = getattr(obj, attr_name)
        print(f'{attr_name}: {value}')
    print('-' * 10, 'ATTR', '-' * 10)
    print()


show_attr(st)
show_attr(st1)
print()
show_attr(Student)

print(id(st.PHONE_NUMBER))
print(id(st1.PHONE_NUMBER))
