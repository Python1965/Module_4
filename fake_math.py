def fake_divide(first, second):
    if second == 0: return "Ошибка"
    else: return first / second


def test():
    print(fake_divide(10, 5))
    print(fake_divide(1, 0))

if __name__ == '__main__':
    test()