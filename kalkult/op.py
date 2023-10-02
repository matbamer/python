import math


def Panelka():
    oper = int(input(
        "1 - Сумма\n" "2 - Вычитание\n" "3 - Произведение\n" "4 - Частность\n" "5 - Возвести в степень\n" "6 - Найти квадратный корень\n" "7 - Факториал\n""8 - Косинус\n""9 - Синус\n" "10 - Тангенс\n""0 - Выйти\n "))

    if oper == 1:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        Sum(a, b)

    if oper == 2:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        Sub(a, b)

    if oper == 3:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        Multiply(a, b)

    if oper == 4:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        Del(a, b)

    if oper == 5:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        Cub(a, b)
    if oper == 6:
        a = int(input("Введите первое число: "))
        Square(a)
    if oper == 7:
        a = int(input("Введите первое число: "))
        factorial(a)
    if oper == 8:
        a = int(input("Введите первое число: "))
        sine(a)
    if oper == 9:
        a = int(input("Введите первое число: "))
        cosine(a)
    if oper == 10:
        a = int(input("Введите первое число: "))
        tangent(a)
    if oper == 0:
        exit


def PrintToConsole(result):
    print("Ответ:", result)
    Panelka()


def Sum(a, b):
    result = a + b
    PrintToConsole(result)


def Sub(a, b):
    result = a - b
    PrintToConsole(result)


def Multiply(a, b):
    result = a * b
    PrintToConsole(result)


def Del(a, b):
    result = a / b
    PrintToConsole(result)
    if b != 0:
        return a / b
    else:
        return "Ошибка"


def Cub(a, b):
    result = pow(a, b)
    PrintToConsole(result)


def Square(a):
    result = math.sqrt(a)
    PrintToConsole(result)


def factorial(a):
    result = math.factorial(a)
    PrintToConsole(result)


def sine(a):
    result = math.sin(a)
    PrintToConsole(result)


def cosine(a):
    result = math.cos(a)
    PrintToConsole(result)


def tangent(a):
    result = math.tan(a)
    PrintToConsole(result)


if __name__ == "__main__":
    Panelka()