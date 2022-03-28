'''
Kudryavchenko Mykola, 141,lab1

4. Дано катети прямокутного трикутника a і b. Знайти його гіпотенузу c і периметр
P: c=(a2+b2)1/2,P=a+b+c.
'''
print("введіть катет а:")
a=int(input())
print("введіть катет b:")
b=int(input())
c=float((a**2+b**2)**1/2)
P=float(a+b+c)
print("катет с=",c)
print("периметр P=",P)
