import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import *

# Вычисление многочлена Тейлора
f = input('f(u) = ')
u0 = float(input('u0 = '))
u = sp.Symbol('u')
n = int(input('n = '))
u1 = float(input('Введите левую границу - '))
u2 = float(input('Введите правую границу - '))
z=0
g=0
p=1
digit = n-1 # Кол-во знаков после запятой в округлении
Dif=[]
while (z<=n):
	Dif.append(sp.Derivative(f, u, z).doit().subs({u:u0}))
	z+=1
z=0
while (z<=n):
	if (z==0):
		g = g + round(float(Dif[z]), digit)
	else:
		p=p*z
		g = g + round(float(Dif[z]/p), digit)*((u-u0)**z)
	z+=1
print(g)

U = np.arange(u1, u2, 0.01)

def calc_f(u):
	global f
	return eval(f)

def calc_g(u):
	global g
	return eval(str(g))

y_f = np.array([calc_f(i) for i in U])
y_g = np.array([calc_g(i) for i in U])


plt.figure(figsize=(14, 8))

plt.plot(U, y_f, label=f)
plt.plot(U, y_g, label=r'$P(u) - Многочлен Тейлора$')

plt.legend(loc='best', fontsize=14)
plt.grid(True)
plt.show()