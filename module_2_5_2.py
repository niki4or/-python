from random import randint


def trap(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\nВХОДИТЕ'
n = int(input(" введи число и если оно будет кратно сумме каждой пары то двери откроются "))

indiana_jones = trap(n)
print(indiana_jones)