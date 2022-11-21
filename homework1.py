# Напишите программу, которая принимает 
# на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

x = int (input("Input day of the week from 1-7" ))
if x > 5 < 7 :
    print('Wekends')
elif x > 8 :
    print("Don't have this day of the week")
elif x < 1 :
    print("Don't have this day of the week")
else :
    print("Working days")