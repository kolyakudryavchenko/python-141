'''
Kudryavchenko Mykola, 141,lab1

14. Обчислити довжину окружності, площу кола та об'єм кулі одного і того ж заданого радіусу.
'''
import math
print("введіть радіус r=")
r=float(input())
l=float(2 * math.pi * r)
s=float(math.pi*r**2)
v=float(4/3*math.pi*r**3)
print("Довжина окружності=",round(l,2))
print("Площа кола=",round(s,2))
print("Об'єм кулі=",round(v,2))

