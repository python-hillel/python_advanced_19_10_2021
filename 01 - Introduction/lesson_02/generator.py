
def gen_1(num):
    lst = []
    while num >= 0:
        lst.append(num)
        num -= 1

    return lst


print(gen_1(109))


# yield
def gen_2(num):
    while num >= 0:
        yield num
        num -= 1


print(gen_2(10))

g = gen_2(10)

for i in g:
    print(i, end=' ')
print()

it = gen_2(5)
try:
    while True:
        print(next(it))
except StopIteration:
    print('Finish')
