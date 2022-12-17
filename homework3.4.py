# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_binary(num):
  return bin(num)[2:]

# тестирование функции
print(decimal_to_binary(45))  # 101101
print(decimal_to_binary(3))   # 11
print(decimal_to_binary(2))   # 10

# ////////////////////////////////////////////

# def decimal_to_binary(num):
#   if num > 1:
#     decimal_to_binary(num // 2)
#   print(num % 2, end='')

# # тестирование функции
# decimal_to_binary(45)
# print()
# decimal_to_binary(3)
# print()
# decimal_to_binary(2)


