def area():
	enter = input('Треугольник, прямоугольник, круг: ')
	if enter.lower() == "треугольник":
		a = float(input('Длина стороны: '))
		b = float(input('Длина стороны: '))
		c = float(input('Длина стороны: '))
		p = ((a + b + c) / 2)
		print('Площадь треугольника: ', (p*(p - a)*(p - b)*(p - c))**0.5)
	elif enter.lower() == "прямоугольник":
		a = float(input('Длина стороны: '))
		b = float(input('Длина стороны: '))
		print('Площадь прямоугольника: ', a*b)
	elif enter.lower() == "круг":
		a = float(input('Радиус: '))
		p = 3.14
		print('Площадь круга: ', p * (a**2))
	else:
		return print('Введите еще раз: ')
	return print('Спасибо за любовь к площадям!')


while True:
	area()
