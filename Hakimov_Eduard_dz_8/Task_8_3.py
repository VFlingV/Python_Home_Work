

from functools import wraps


def type_logger():

    def logger(func):

        @wraps(func)
        def decor(*argv, **kwargs):

            args = list(argv) + list(kwargs.values())
            result = func(args[0])
            print(", ".join([f"{x}:{type(x)}" for x in args]))
            #print(f"{func.__name__}:{type(func)}")
            #print(f"{func.__name__}({all_args[0]}):{type(norm_res)}")

            return result

        return decor

    return logger


@type_logger()
def calc_cube(x):
    """ cube of args """
    return x ** 3


a = calc_cube(6.5, 10, 7, 1, 5.1, 1, 6, 3)
#print(a)
