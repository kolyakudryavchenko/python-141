'''
Кудрявченко Микола, 141, lab5
9. Описати функцію Power4 (x, a, ε) дійсного типу (параметри x, a, ε - дійсні, | x | <1; a, ε> 0),
знаходить наближене значення функції (1 + x) a:
(1 + x) a = 1 + a · x + a · (a-1) · x2 / (2!) + ... + a · (a-1) · ... · (a-n + 1) · xn / (n!) + ....
В сумі враховувати всі складові, модуль яких більше ε. За допомогою Power4
знайти наближене значення (1 + x) a для даних x і a при шести даних ε.
'''

import math
print('Введіть число х:')
x = float(input())
print('Введіть число a:')
a = float(input())
print('Введіть число e:')
e = float(input())
if abs(x)>=1 or  e<=0:
    print("| x | <1  ε> 0 ")
    exit(0)

def power4(x, a, e):
    s=0
    for i in range(1, int(a), 1):
        n=float((1+i*a) * x ** i / math.factorial(i))
        if abs(n)>e:
            s+=n
        i+=1
    print(s)

power4(x, a, e)
power4(x, a, e+1)
power4(x, a, e+2)
power4(x, a, e+3)
power4(x, a, e+4)
power4(x, a, e+5)
