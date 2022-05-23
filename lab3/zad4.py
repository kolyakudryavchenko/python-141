'''
Кудрявченко Микола, 141, lab3
4.Дано ціле n> 2. Вивести всі прості числа з діапазону [2, n].
'''

print('введіть ціле число n(>2)')
n=int(input())

def func(n):
    for i in range(2,n,1):
        k=0
        for j in range(1,i-1,1):
            if i % j==0:
                k+=1
        if k<2:
            print(i)
func(n)

