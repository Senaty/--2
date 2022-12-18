import math

x1 = float(input('Введите первое значение x1:'))
x2 = float(input('Введите второе значение х2:'))
h = float(input('Введите шаг смещения по оси x:'))
m = int((max(x1, x2) - min(x1, x2)) // h)
x = min(x1, x2)
y = []
n = []
for i in range(0, m):
    y.append((round((x ** 3 + math.sqrt(x)) / ((math.e + math.atan(x)) ** 2), 3), ', при х =', round(x, 3)))
    n.extend(y)
    print(y)
    y.clear()
    x += h
print(n)