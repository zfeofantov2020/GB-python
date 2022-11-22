# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁  - or
# ⋀ - and
# ¬ - not

# ¬ (1 or 0 or 0) = ¬ (1 and 0 and 0)

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
        print(a)
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


numbers = inputNumbers(3)


if checkPredicate(numbers) == True:
    print(f"Утверждение истинно" )
else:
    print(f"Утверждение ложно")




