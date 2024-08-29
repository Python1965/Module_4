
from math import inf

def true_divide(first, second):
    if second == 0: return inf
    else: return first / second

def test():
    print(true_divide(10, 5))
    print(true_divide(1, 0))

if __name__ == '__main__':
    test()
