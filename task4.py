# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from os import system
system("cls")

def Get_Num():
    done = True
    while done:
        strUser = input('Введите число - ')
        done = not strUser.isdigit()
        userNum = int(strUser)
        return userNum

def decToBool(x):
    '''Функция перевода десятичного целого числа в двоичное'''
    binList = []
    count = 0
    while x > 0:
        binList.append((x % 2))
        count = count + 1
        x = int(x / 2)
    return(binList)

print()
print('Программа преобразует целое десятичное число в двоичное.')
print(f"{str(decToBool(Get_Num())).replace(',', '').replace('[', '').replace(']', '')}") #лень