n = int(input())
total_step = 0
element_step = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            element_step = i * (i + 1)
            total_step += element_step
        else:
            element_step = 0
        print(element_step, end=' ')
    print('')
print('')
print(total_step)
