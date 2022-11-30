# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
number = 45

def convert(num): 
  result = []
  while num != 0:
    result.append(1) if num % 2 else result.append(0)
    num = num // 2
  result = int("".join(map(str, reversed(result))))
  return result  

print(convert(number))