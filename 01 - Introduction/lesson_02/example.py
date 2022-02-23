def func(x):
    return x * x, 'Test msg'
    # print('Test msg')


while True:
    number = int(input('Please enter a number: '))
    if number == 0:
        break

    res = func(number)
    print(res[0])
    print(res[1])
    print()
