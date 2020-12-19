import tkinter as tk
from tkinter import messagebox as mb
from playsound import playsound
import project_calc_1 as pc

blank_space = ' '
title_color = ['#FFDB8B', '#87CEEB']
bg_color = ['#FFFACD', '#B0C4DE']


def btn_1(f=0):
	def click_btn_use_1():
		'''
		Срабатывает при нажатии на кнопку "Применить"
		'''
		playsound('click_sound.mp3')
		function_get = function.get()
		power_get = power.get()
		point_get = point.get()
		left_get = left.get()
		right_get = right.get()
		if function_get == '':
			mb.showerror('Ошибка', 'Введите функцию!')
		elif power_get == '':
			mb.showerror('Ошибка', 'Введите степень!')
		elif point_get == '':
			mb.showerror('Ошибка', 'Введите точку!')
		elif left_get == '':
			mb.showerror('Ошибка', 'Введите левую границу!')
		elif right_get == '':
			mb.showerror('Ошибка', 'Введите правую границу!')
		elif float(power_get) < 0:
			mb.showerror('Ошибка ввода', 'Неверное значение степени!')
		elif float(left_get) >= float(right_get):
			mb.showerror('Ошибка ввода', 'Неверно указаны границы!')
		else:
			if (float(point_get) <= float(left_get)) or (float(right_get) <= float(point_get)):
				mb.showwarning('Предупреждение', 'Желательно, чтоб точка находилась внутри границ.')

			answer = mb.askyesno('Проверьте введенные данные!', 'Вы уверенны, что ввели данные верно?')
			if answer:
				pc.calc_1(function_get, point_get, power_get, left_get, right_get)
				print('Функция - ' + function_get)
				print('Степень - ' + power_get)
				print('Точка разложения - ' + point_get)
				print('Левая граница - ' + left_get)
				print('Правая граница - ' + right_get)
				print('Use!')


	def click_btn_tyk_1():
		'''
		Срабатывает при нажатии на кнопку "Кнопка"
		'''
		playsound('click_sound.mp3')
		mb.showinfo('Тык-кнопка', 'Тык!')
	

	screen_1 = tk.Tk()
	screen_1.geometry('640x400')
	screen_1['bg'] = bg_color[f%2]
	screen_1.title(80*blank_space + 'Mode №_1')
	screen_1.resizable(width = False, height = False)
	screen_1.iconbitmap('Project_icon.ico')

	# Виджеты
	Title = tk.Label(screen_1, text = 'Настройте параметры', bg = title_color[f%2], font = '32')
	text_warning = tk.Label(screen_1, text = 'Функция от аргумента u !!!', font = '32', bg = title_color[f%2])
	text_func = tk.Label(screen_1, text = 'Введите функцию f(u)', font = '28', bg = '#FFFFFF')
	function = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	text_power = tk.Label(screen_1, text = 'Введите степень', font = '28', bg = '#FFFFFF')
	power = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	text_point = tk.Label(screen_1, text = 'Точка разложения', font = '28', bg = '#FFFFFF')
	point = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	text_border = tk.Label(screen_1, text = 'Введите левую и правую границы', font = '28', bg = '#FFFFFF')
	left = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	right = tk.Entry(screen_1, bg = '#FFFFFF', justify = 'center')
	btn_use = tk.Button(screen_1, text = 'Применить', command = click_btn_use_1)
	btn_tyk = tk.Button(screen_1, text = 'Кнопка', command = click_btn_tyk_1)


	# Упаковка всех виджетов
	Title.pack(anchor = 'n', padx = 5, pady = 5)

	text_warning.pack(anchor = 'n', side = tk.RIGHT, padx = 10, pady = 5)

	btn_tyk.pack(anchor = 'w', side = tk.BOTTOM, padx = 10, pady = 10)
	btn_use.pack(anchor = 'w', side = tk.BOTTOM, padx = 10)

	text_func.pack(anchor = 'w', padx = 5, pady = 5)
	function.pack(anchor = 'w', padx = 5, pady = 5)

	text_power.pack(anchor = 'w', padx = 5, pady = 5)
	power.pack(anchor = 'w', padx = 5, pady = 5)

	text_point.pack(anchor = 'w', padx = 5, pady = 5)
	point.pack(anchor = 'w', padx = 5, pady = 5)
	
	text_border.pack(anchor = 'w', padx = 5, pady = 5)
	left.pack(anchor = 'w', side = tk.LEFT, padx = 5, pady = 5)
	right.pack(anchor = 'w', side = tk.LEFT, padx = 5, pady = 5)


	screen_1.mainloop()


if __name__ == "__main__":
    print("This module is not for direct call!")