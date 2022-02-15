def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:  # O(n)
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    n >= 0

    :param n: number of item
    :return: Fibonacci number

    n-ое число
    """
    if n == 0:  # это первое число фиббоначи
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(n - 1):  # n - 2
        # sum_ = a + b
        # a = b
        # b = sum_
        a, b = b, a + b

    return b


def generator_fib(n):
    """
    Возвращает первые n чисел фибоначи
    :param n:
    :return:
    """
    a = 0
    yield a

    b = 1
    yield b

    for _ in range(n - 2):  # n - 2
        a, b = b, a + b
        yield b

    for _ in range(n - 2):  # n - 2
        a, b = b, a + b
        yield b


# Найти первые n чисел фибоначи
# Функция генератор generator_fib
# Итеративный алгоритм fib_iterative
# N = 10
#
# list_fin_iterative = [fib_iterative(i) for i in range(N)]  # O(n^2)
# list_fin_iterative = []
# for i in range(N):  # O(N)
#     current_number = fib_iterative(i)  # O(N)
#     list_fin_iterative.append(current_number)  # O(1)
#
# list_generator = [num for num in generator_fib(N)]  # O(n)
# generator = generator_fib(N)
# for _ in range(N):
#     current_number = next(generator)  # O(1)
# print(list_fin_iterative)
# print(list_generator)

if __name__ == '__main__':
    fib_recursive(8)