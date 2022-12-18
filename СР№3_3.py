def f(s):
    with open('qwe.txt', encoding='utf-8', mode='r') as output:
        g = output.read().splitlines()
    print(g.pop(s))


f(s=int(input()))
