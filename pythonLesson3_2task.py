# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

newList  = [2, 3, 4, 5, 6]

def sum(ls):
    result = [] 
    halsLs = math.ceil(len(ls) / 2)
    for i in range(halsLs):
        result.append(ls[i] * ls[len(ls)-1-i])
    return result

print(sum(newList))

