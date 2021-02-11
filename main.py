from compare import compare
from fib_funcs import *

FIB_NUM = 30

if __name__ == '__main__':
    compare([fib3, fib2, fib1], list(range(FIB_NUM)))
