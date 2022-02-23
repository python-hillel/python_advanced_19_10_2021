import datetime


def sec2dt(seconds):
    return datetime.datetime.fromtimestamp(seconds)


def hello():
    print('Hello World!')


def main():
    # sec = 34842
    # print(sec2dt(348654836))
    #
    # h = sec // 3600
    # m = (sec - h * 3600) // 60
    # s = (sec - h * 3600) - m * 60
    #
    # print(h, m, s)
    hello()


if __name__ == '__main__':
    main()
