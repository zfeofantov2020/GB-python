# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Пример:


numbers = [1.1, 1.2, 3.1, 10.01]
min_decimal = min(numbers, key=lambda x: x % 1) % 1
max_decimal = max(numbers, key=lambda x: x % 1) % 1
difference = max_decimal - min_decimal
print(difference)