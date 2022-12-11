# Напишите программу, которая принимает на 
# вход вещественное число
# и показывает сумму его цифр.
# Пример:

# 0,56 -> 11

def sum_of_digits_after_comma(num):
  num_str = str(num)
  decimal_pos = num_str.find(".")
  if decimal_pos == -1:
    return 0
  digits_str = num_str[decimal_pos+1:]
  sum_of_digits = 0
  for digit in digits_str:
    sum_of_digits += int(digit)
  return sum_of_digits

# Test the function with some numbers
print(sum_of_digits_after_comma(0.56))  # should print 11
print(sum_of_digits_after_comma(2.34))  # should print 7
print(sum_of_digits_after_comma(3.14))  # should print 5
print(sum_of_digits_after_comma(3.144))  # should print 9

