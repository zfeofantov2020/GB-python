# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def sum_odd_indexed_elements(lst):
  sum = 0
  for i, x in enumerate(lst):
    if i % 2 == 1:
      sum += x
  return sum

lst = [2, 3, 5, 9, 3]
result = sum_odd_indexed_elements(lst)
print(result) # должно вывести 12