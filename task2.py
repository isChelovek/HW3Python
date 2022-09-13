# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from os import system
system("cls")

print()
print("Введите список из нескольких целочисленых чисел разделеннныx запятой или пробел")
userList  = [int(i) for i in input().split(',')]

def GetMultSide(userList):
    result = []
    for i in range(int(len(userList)/2)):
        result.append(userList[i] * userList[len(userList)-(i+1)])
    if (len(userList)%2):
        result.append(userList[int(len(userList)/2)]*userList[int(len(userList)/2)])
    return result

print(f'{userList} => {GetMultSide(userList)}')
print()

