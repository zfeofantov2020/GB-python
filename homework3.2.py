# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def product_pairs(lst):
  # Инициализируем список для хранения результата
  result = []
  # Обходим список с помощью цикла for
  for i in range(len(lst) // 2):
    # Находим индексы пар элементов
    first_index = i
    second_index = -(i + 1)
    # Находим значения элементов
    first = lst[first_index]
    second = lst[second_index]
    # Перемножаем элементы и добавляем результат в список
    result.append(first * second)
  # Возвращаем результат
  return result

lst = [2, 3, 5, 6]
result = product_pairs(lst)
print(result)  # должно вывести [12, 15]

lst = [2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8]
result = product_pairs(lst)
print(result)  # должно вывести [12, 15]




