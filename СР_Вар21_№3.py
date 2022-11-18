import math

x1 = float(input('Введите первое значение x1:'))
x2 = float(input('Введите второе значение х2:'))
h = float(input('Введите шаг смещения по оси x:'))
m = int((max(x1, x2) - min(x1, x2)) // h)
print(m)
x = min(x1, x2)
for i in range(0, m):
    print((1-(x**2/2)*math.cos(x)-((x/2)*math.sin(x)), ', при х =', x))
    x += h
