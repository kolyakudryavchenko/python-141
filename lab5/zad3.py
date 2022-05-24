'''
Кудрявченко Микола, 141, lab5
9. Описати функцію Fib (N) цілого типу, яка обчислює N-й елемент послідовності чисел Фібоначчі FK,
яка описується наступними формулами:
F1 = 1, F2 = 1, FK = FK-2 + FK-1, K = 3, 4, ....
Використовуючи функцію Fib, знайти п'ять чисел Фібоначчі з даними номерами N1, N2, ..., N5.
'''

print('введіть число N:')
n=int(input())

def fib(n):
    f=[0]*(n+5)
    f[0]=1
    f[1]=1
    for i in range(2, n+5, 1):
        f[i]=f[i - 1]+f[i - 2]
        i+=1
    for i in range(n, n+5, 1):
        print(f[i])

print('Отримали числа:')
fib(n)
