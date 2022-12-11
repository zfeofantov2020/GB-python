# Задайте список из N элементов, заполненных 
# числами из промежутка [-N, N].
# Найдите произведение элементов на указанных 
# индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input("Введите число : "))
numbers = []

for i in range(-n, n + 1):
  numbers.append(i)

indexes_str = input("Введите индексы: ")

print (indexes_str)

indexes = [int(i) for i in indexes_str.split()]
product = 1

for index in indexes:
  product *= numbers[index]
print(product)
