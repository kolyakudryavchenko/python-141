'''
Кудрявченко Микола, 141, lab1
4. Для даного дійсного x знайти значення наступної функції f, що приймає дійсні значення:
f (x) = 2 • sin (x), якщо x> 0; 6 - x, якщо x ≤ 0.
'''
import math
print('Введіть x:')
x=int(input())
if x>0:
    f=2*(math.sin(x))
elif x<=0:
    f=6-x
else: f=str('error')
print('значення функції f:',round(f,2))


