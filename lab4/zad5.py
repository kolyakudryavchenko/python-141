'''
Кудрявченко Микола, 141, lab4
10. Дано рядки S, S1 і S2. Замінити в рядку S останнє входження рядка S1 на рядок S2.
'''

def vvod():
    print('Введіть рядок s:')
    s=str(input())
    print('Введіть рядок s1:')
    s1=str(input("S1 = "))
    print('Введіть рядок s2:')
    s2=str(input("S2 = "))
    return s, s1, s2


def func_1(s, s1, s2):
    res=s.replace(s1, s2)
    return res


def func_2():
    s, s1, s2=vvod()
    result=func_1(s, s1, s2)
    return result


result=func_2()
print(result)
