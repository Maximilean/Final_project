import tkinter as tk 
from playsound import playsound
from project_button_1 import *
from project_button_2 import *



blank_space = ' '
st = 0


def main():
	'''
	Функция запускающая начальное меню
	'''
	def click_1():
		'''
		Функция для первой кнопки
		'''
		global st
		playsound('click_sound.mp3')
		print('Вы нажали 1 кнопку!')
		st_color = style.get(tk.ANCHOR)
		if st_color == 'CalmBlue':
			st = 1
		else:
			st = 0 
		btn_1(st)


	def click_2():
		'''
		Функция для второй кнопки
		'''
		global st
		playsound('click_sound.mp3')
		print('Вы нажали 2 кнопку!')
		st_color = style.get(tk.ANCHOR)
		if st_color == 'CalmBlue':
			st = 1
		else:
			st = 0 
		btn_2(st)

	root = tk.Tk()

	root.geometry('300x400')
	root['bg'] = '#FFFFE0'
	root.title(8*blank_space + 'Main Window!')
	root.resizable(width = False, height = False)
	root.iconbitmap('Project_icon.ico')

	text = tk.Label(text = 'Выберите режим', bg = '#FFDEAD', font = '28',
					width = 20)
	button_1 = tk.Button(text = "Разложение по степени", width = 25, height = 2,
    					bg = "#FFDB8B", command = click_1)
	button_2 = tk.Button(text = "Разложение по погрешности", width = 25, height = 2,
    					bg = "#FFDB8B", command = click_2)
	text_chose = tk.Label(text = 'Выберите стиль', bg = '#FFDB8B', width = 20)

	style = tk.Listbox(height = 2, justify = 'center')

	text.pack()
	button_1.pack(pady = 10)
	button_2.pack()
	text_chose.pack(pady = 15)
	style.pack()

	for i in ('PalePeach', 'CalmBlue'):
		style.insert(tk.END, i)


	root.mainloop()


if __name__ == "__main__":
	main()
