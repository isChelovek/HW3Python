# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/yWbkX.)

from os import system
system("cls")
print()

def Get_Num():
    '''Ввод пользователем числа с валидацией'''
    done = True
    while done:
        strUser = input('Введите число - ')
        done    = not strUser.isdigit()
        userNum = int(strUser)
        return userNum

def fibonacci(number):
    '''расчет числа вибоначи'''
    if (number == 0):
        return 0
    if (number == 1):
        return 1
    return fibonacci(number-1) + fibonacci(number-2)

def negaFibonacci(number):
    result = 0
    result = ((-1)**(number+1)) * fibonacci(number)
    return result

def getNegaFibonacci(userNum):
    '''Негафибоначчи'''
    fiblist = []
    negfiblist = []
    count = 0
    for i in range(userNum):
        fiblist.append(fibonacci(i))
        negfiblist.append(negaFibonacci(i))
        count = count + 1
    negfiblist.reverse()
    negfiblist.remove(0)
    negfiblist = negfiblist + fiblist
    return negfiblist

print("Программа выводит Негафибоначчи")
userNum = Get_Num()
print(f'Для k = {userNum} список будет выглядеть так: {getNegaFibonacci(userNum)}')
print()