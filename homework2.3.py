# Задайте список из n чисел последовательности 
# (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input("Введите число : "))
sequence = []
for i in range(1, n + 1):
  value = (1 + 1/i)**i
  sequence.append(value)
sum = 0
for value in sequence:
  sum += value
print(sum)
