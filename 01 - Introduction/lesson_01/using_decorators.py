import math


def pre(cond, msg):
    from functools import wraps

    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            # assert condition, message
            assert cond(*args, **kwargs), msg
            return func(*args, **kwargs)
        return inner
    return outer


@pre(lambda a: a >= 0, 'Negative argument')
def check_log(x):
    return math.log(x)


# print(check_log(45))
# print(check_log(-5))


def post(cond, msg):
    from functools import wraps

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            assert cond(res), msg
            return res
        return inner
    return wrapper


@post(lambda x: not math.isnan(x), 'Not A Number')
def something_useful(param=None):
    if param is None:
        return float('nan')     # NaN
    else:
        return float(param)


print(something_useful('4.56'))             # 4.56
print(something_useful())
