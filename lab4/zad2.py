'''
Кудрявченко Микола, 141, lab4
14. Дано два упорядкованих за спаданням списки. Об'єднайте їх в новий упорядкований за спаданням список.
'''
print('Дано два списки:a = [263, 35, 22, 5, 1] і b = [134, 68, 12, 2]')
def func():
    a = [263, 35, 22, 5, 1]
    b = [134, 68, 12, 2]
    s = a + b
    s.sort(reverse=True)
    print(s)

print('Рядок,обєднаний з двух списків')
func()