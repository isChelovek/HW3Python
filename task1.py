# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from os import system
system("cls")

def GetSummOddPlaces():
    print()
    print("Введите список из нескольких целочисленых чисел разделеннныx запятой или пробел")
    userList  = [int(i) for i in input().split(',')]
    print(f"{userList} -> на нечётных позициях элементы {str(userList[0::2]).replace(', ', ' и ').replace('[', '').replace(']', '')}, ответ: {sum(userList[0::2])}")

GetSummOddPlaces()
