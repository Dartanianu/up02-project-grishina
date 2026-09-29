catalog = [
    {'name': 'Кроссовки', 'price': 8500, 'qty': 3},
    {'name': 'Ботинки', 'price': 15000, 'qty': 1},
    {'name': 'Туфли', 'price': 12000, 'qty': 5},
    {'name': 'Сандалии', 'price': 4500, 'qty': 8},
    {'name': 'Кеды', 'price': 6000, 'qty': 2}
]

total = 0
print('Каталог товаров:')
for i, item in enumerate(catalog, 1):
    cost = item["price"] * item["qty"]
    total += cost
    print(f'{i}. {item["name"]:12} - {item["price"]} * {item["qty"]} = {cost} руб')

print('-'*40)
print(f'Итого: {total} руб')