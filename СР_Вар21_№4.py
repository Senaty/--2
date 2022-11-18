n = int(input('от:'))
m = int(input('и до:'))
s = 0
for i in range(n, m + 1):
    s += 1/(n**2+4)
print('S =', s)
