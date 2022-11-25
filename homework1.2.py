# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и 
# Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int (input("Input X > 0 or X < 0 , but =!0  'X':" ))
y = int (input("Input Y > 0 , or Y < 0 , but != 0 'Y':" ))
while x == 0 or y == 0 :
    print("You entered X or Y == 0 , try one more time")
    x = int (input("Input 'X':" ))
    y = int (input("Input 'Y':" ))
if x >= 1 and y >= 1 :
    print(' "I" , You Input X:', x , 'And Y:',y)
elif x <= 1 and y >= 1 :
    print(' "II" , You Input X:', x , 'And Y:',y)
elif x <= 1 and y <= 1 :
     print(' "III" , You Input X:', x , 'And Y:',y)
else :
    print(' "IV" , You Input X:', x , 'And Y:',y)





