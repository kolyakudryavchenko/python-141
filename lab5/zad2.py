'''
Кудрявченко Микола, 141, lab5
9. Описати функцію Even (K) логічного типу, яка повертає True, якщо цілий параметр K є парним,
і False в іншому випадку. З її допомогою знайти кількість парних чисел в наборі з 10 цілих чисел.
'''

print('Введіть число К:')
k=int(input())
n=list(range(k, k+10))

def even(n):
    count=0
    for i in range(0, 10, 1):
        if n[i]%2==0:
            count+=1
        i+=1
    print(count)
    return count

even(n)
