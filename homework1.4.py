# Напишите программу, которая принимает на 
# вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from cmath import sqrt
import math

xa = int (input ('XA :'))
ya = int (input ('YA :'))
xb = int (input ('XB :'))
yb = int (input ('YB :'))

d = (math.sqrt((xb-xa)**2+(yb-ya)**2))

print(d)
