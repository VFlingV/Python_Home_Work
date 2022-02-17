

from functools import wraps


def val_checker(func_new):

    def checker(func):

        @wraps(func)
        def wrap(x):

            if func_new(x):
                return func(x)

            raise ValueError(f'err {x}')

        return wrap

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
try:
    a = calc_cube(5)
    print(help(calc_cube))
except(ValueError, TypeError) as err:
    print(err)