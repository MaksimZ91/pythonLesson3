# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = 8

def fib(n):
  fib1, fib2, fib3 = 0,1,1
  positivLs = [fib1, fib2, fib3]
  negativLS = [-fib2, -fib3]
  for i in range(2, n):
    positivLs.append(positivLs[i-1] + positivLs[i])
    negativLS.append(fib1 - positivLs[i+1])  
  return list(reversed(negativLS)) + positivLs


print(fib(8))