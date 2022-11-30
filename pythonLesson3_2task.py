# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

newList  = [2, 3, 4, 5, 6]
print(len(newList))

def sum(ls):
    result = []   
    for i in range(len(ls)):
        result.append(ls[i] * ls[len(ls)-1-i])
    return result

print(sum(newList))  