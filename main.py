import math
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

d = b**2 - 4*a*c

if d == 0:
    print("Уравнение имеет один корень.")

    x = -(b/2*a)
    print("Корень равен:",x)

elif d < 0:
    print("Уравнение не имеет корней.")

else:
    print("Уравнение имеет 2 корня.")

    x1 = -((b+math.sqrt(d))/2*a)
    x2 = -((b-math.sqrt(d))/2*a)
    print("первый корень равен:",x1)
    print("второй корень равен:",x2)