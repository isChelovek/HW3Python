# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from os import system
system("cls")

print()
print("Введите список из нескольких вещественных чисел разделеннныx запятой или пробел")
userList  = [float(i) for i in input().split(',')]

def getFractionalPart(userList):
    '''Удаляет целую часть от вещественного числа'''   
    result = []
    count = 0
    for i in userList:
        tempStr = str(i)
        resultSTR =('0' + tempStr[tempStr.find('.')::1])
        result.append(float(resultSTR))
    return result

def fractionalDifference(result):
    '''Возвращает разницу между максимальным и минимальным элементом массива''' 
    return(max(result)- min(result))

print(round(fractionalDifference(getFractionalPart(userList)), 10))