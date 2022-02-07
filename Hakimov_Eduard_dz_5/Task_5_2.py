

def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    generator = (i for i in range(1, number + 1, 2))
    return generator



n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
#print(type(generator))
