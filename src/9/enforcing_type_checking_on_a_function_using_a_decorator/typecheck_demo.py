from functools import wraps


def typecheck(*argsOut):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            assert argsOut[0] == type(args[0])
            func(*args, **kwargs)

        return wrapper

    return decorate


@typecheck(int)
def func1(a, b):
    return a + b


func1("20", "30")