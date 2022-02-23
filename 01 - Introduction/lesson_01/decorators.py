from functools import update_wrapper, wraps


def measure_time(function):
    from datetime import datetime

    @wraps(function)
    def wrapper(*args, **kwargs):
        """
        It's wrapper
        :return:
        """
        start = datetime.now()
        res = function(*args, **kwargs)
        offset = datetime.now() - start
        print(offset)
        return res

    # wrapper.__doc__ = function.__doc__
    # wrapper.__name__ = function.__name__
    # update_wrapper(wrapper, function)
    return wrapper


@measure_time
def gen_list(param):
    """
    List generator

    :return: List
    """
    lst = []

    for i in range(param):
        if i % 2 == 0:
            lst.append(i)

    return lst


print(len(gen_list(10**2)))
print(gen_list.__doc__)
print(type(gen_list))
print(gen_list.__name__)
w = gen_list
print(w.__name__)
# r = w()
# print(len(r))