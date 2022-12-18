def ar(s):
    alpha = 0
    betta = 0
    print('Символы:', len(s))
    print('Слова:', sum(1 for w in s.lower().split()))
    print('Буквы:', sum(c != ' ' for c in s))
    for i in s:
        if i.isdigit():
            alpha += 1
    print('Цыфры:', alpha)
    for i in s:
        if not (i.isalnum()):
            betta += 1
    print('Спецсимволы:', betta)


while True:
    s = input()
    ar(s)
    if s == ' ':
        break
