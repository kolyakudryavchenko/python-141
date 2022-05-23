'''
Кудрявченко Микола, 141, lab3
10.Дано ціле число N (> 0). Знайти значення виразу 1.1 - 1.2 + 1.3 - ...
(N доданків, знаки чергуються). Умовнийоператорневикористовувати.
'''

def func():
    print('Введіть N(>0)')
    n=int(input())
    return n

def func_2():
    n=func()
    m=(1.0+float(1/10))
    i=1
    while i<n:
        a=(1.0+(float(i+1)/10))
        b1=i%2==0
        b2=i%2!=0
        while b1:
            m=m+a
            i+=1
            b1=i%2==0
        while b2:
            m=m-a
            i+=1
            b2=i%2 != 0
    return round(m,3)


res=func_2()
print('Значення виразу',res)
