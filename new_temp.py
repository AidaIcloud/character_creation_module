from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')
messagelast = ('Мы вычислили квадратный корень из введённого вами'
               'числа.Это будет:')


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень из числа."""
    return sqrt(Number)


def calc(your_number):
    """Вычисляет квадратный корень из заданного числа."""
    if your_number <= 0:
        return None
    else:
        square_root = CalculateSquareRoot(your_number)
        return print(messagelast, square_root)


print(message)
calc(25.5)
