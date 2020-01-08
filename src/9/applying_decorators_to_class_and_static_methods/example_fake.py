import time
from functools import wraps
import inspect

def monitor(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end - start)
		return result

	return wrapper

@monitor
def func1():
	print(inspect.currentframe().f_code.co_name + ' begin')
	time.sleep(1.5)
	print(inspect.currentframe().f_code.co_name + ' end')


func1()