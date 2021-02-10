from compare import compare
from fib_funcs import *

FIB_NUM = 800

if __name__ == '__main__':
    compare([fib2, fib3], list(range(FIB_NUM)))
