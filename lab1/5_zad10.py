'''
Kudryavchenko Mykola, 141,lab1

10. Даний розмір файла в байтах. Використовуючи операцію ділення без залишку, знайти кількість
повних кілобайтів, які займає даний файл (1 кілобайт = 1024 байта).
'''

print("введіть розмір файла в байтах:")
a=int(input())
k=int(a//1024)
print("кількість цілих кілобайтів:", k)


