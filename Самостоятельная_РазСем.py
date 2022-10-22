n = input('Введите строку:')
s = input('Введите подстроку:')
if s in n:
    print('Подстрока', s, 'есть в строке', n)
    x = (3.14 + len(n)) / len(s)
    print('X =', x)
else:
    if len(n) % 2 == 0 and len(n) % 5 == 0:
        print('Подстрока', s, 'отсутствует в строке', n)
        print('Длина строки четна и кратна 5')
        print(n + str(s))
        print(len(n) + len(s))
    elif len(n) % 2 != 0 and len(n) % 3 == 0:
        print('Подстрока', s, 'отсутствует в строке', n)
        print('Длина строки нечетна и кратна 3')
        print('Введите 3 строки:')
        q = input('1 - ')
        w = input('2 - ')
        e = input('3 - ')
        if (len(q) > len(w)) and (len(q) > len(e)):
            print(q, '– наибольшая по длине')
        elif (len(w) > len(q)) and (len(w) > len(e)):
            print(w, '– наибольшая по длине')
        else:
            print(e, '– наибольшая по длине')
    else:
        print('Подстрока', s, 'отсутствует в строке', n)
        print('Exit')
