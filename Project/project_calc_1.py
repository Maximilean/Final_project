import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import *


# Вычисление многочлена Тейлора
def calc_1(f, u0, n, u1, u2):
	u = sp.Symbol('u')
	u0 = float(u0)
	n = int(n)
	u1 = float(u1)
	u2 = float(u2)
	z=0
	g=0
	p=1
	delta = 0.002 # Шаг
	area_f = 0
	area_g = 0
	Dif=[]
	while (z<=n):
		Dif.append(sp.Derivative(f, u, z).doit().subs({u:u0}))
		z+=1
	z=0
	while (z<=n):
		if (z==0):
			g = g + Dif[z]
		else:
			p=p*z
			g = g + Dif[z]/p*((u-u0)**z)
		z+=1
	print(g)

	U = np.arange(u1, u2+delta, delta)

	def calc_f(u):
		return eval(f)

	def calc_g(u):
		return eval(str(g))

	y_f = np.array([calc_f(i) for i in U])
	y_g = np.array([calc_g(i) for i in U])
	subtrac = np.array([abs(calc_f(i) - calc_g(i)) for i in U])

	D = np.array([delta for i in U])

	area_f = round(np.dot(y_f, D.T), 3)
	print('Площадь f', area_f)
	area_g = round(np.dot(y_g, D.T), 3)
	print('Площадь g', area_g)

	# Средняя ошибка приближение
	error = round(np.dot(subtrac, D.T)/(u2+delta-u1), 3)

	print('Погрешность - ', error)


	plt.figure(figsize=(14, 8))

	plt.plot(U, y_f, label=f)
	plt.plot(U, y_g, label=r'$P(u) - Многочлен Тейлора$')
	plt.plot(u0, Dif[0], label='Погрешность = '+str(error))

	plt.legend(loc='best', fontsize=12)
	plt.grid(True)
	plt.show()

if __name__ == "__main__":
    print("This module is not for direct call!")