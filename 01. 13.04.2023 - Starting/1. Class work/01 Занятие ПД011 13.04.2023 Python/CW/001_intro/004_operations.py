# Арифметические операции
# + - * /                    5 / 2 = 2.5
# // - целочисленное деление 5 // 2 = 2
# %  - взятие остатка от деления
# ** - возведение в степень
# += -= *= /= //= %= **=

a = 6
b = 4

c = a + b
print(f'{a} + {b} = {c}')

c = a - b
print('{0} - {1} = {2}'.format(a, b, c))

c = a * b
print('{0} * {1} = {2}'.format(a, b, c))

c = a / b
print('{0} / {1} = {2}'.format(a, b, c))

c = a // b
print(f'{a} // {b} = {c}')

c = a % b
print('{0} % {1} = {2}'.format(a, b, c))

c = a ** b
print('{0} ** {1} = {2}'.format(a, b, c))

# Логические операции
print('\nЛогические операции')
# < <= == != >= >
r = a > b
print('{0} > {1} = {2}'.format(a, b, r))

r = a >= b
print('{0} >= {1} = {2}'.format(a, b, r))

r = a == b
print('{0} == {1} = {2}'.format(a, b, r))

r = a != b
print('{0} != {1} = {2}'.format(a, b, r))

r = a <= b
print('{0} <= {1} = {2}'.format(a, b, r))

r = a < b
print('{0} < {1} = {2}'.format(a, b, r))

# Еще логические операции
# not and or
r = 0 <= a and a % 2 == 0
print('{0} >= 0 and {0} % 2 == 0 --> {1}'.format(a, r))

# то же, что и предыдущий вариант, но без and
r = 0 <= a % 2 == 0
print('{0} >= 0 and {0} % 2 == 0 --> {1}'.format(a, r))

r = b % 2 != 0 or a % 2 != 0
print('{0} % 2 != 0 or {1} % 2 != 0 --> {2}'.format(b, a, r))
