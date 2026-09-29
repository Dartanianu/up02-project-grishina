price = int(input('Введите цену: '))
disc = int(input('Введите скидку (%): '))

print(f'Цена со скидкой {price - ((price * disc) / 100)} руб.')