from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

# Example Equivalent 111
@logged
def add(x, y):
    return x + y

# Example Equivalent 111
def add(x, y):
    return x + y
add = logged(add)


# Example Equivalent 222
@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')

# Example Equivalent 222
def spam():
    print('Spam!')
spam = logged(level=logging.CRITICAL, name='example')(spam)