import databases as db
import db_products
from catalog import _indicator

def test_fields():
    """Проверяет, что все поля на месте."""
    products = db_products.get_all_products()
    print(f"Всего товаров: {len(products)}")


    required_fields = ['id', 'name', 'coach', 'time', 'price', 'qty', 'picture']
    required_count = 6   # минимум полей для макета
    errors = 0

    for p in products:
        existing_fields = [field for field in required_fields if hasattr(p, field)]
        if len(existing_fields) < required_count:
            print(f"❌ Товар id={p[0]}: мало полей ({len(p)})")
            errors += 1

    if errors == 0:
        print("✅ Все товары содержат нужные поля")
    else:
        print(f"❌ Найдено ошибок: {errors}")

def test_prices():
    """Проверяет, что у всех товаров есть цена."""
    products = db_products.get_all_products()
    errors = 0
    for p in products:
        # У объекта Products обращаемся через точку
        if p.price is None or p.price <= 0:
            print(f"❌ Товар id={p.id}: нет цены")
            errors += 1
    if errors == 0:
        print("✅ У всех товаров есть цена")
    else:
        print(f"❌ Найдено товаров без цены: {errors}")


def test_indicator():
    """Прогон тестов для индикатора."""
    test_cases = [
        # (qty, expected, comment)
        (29, "много", "20 > 10"),
        (10, "мало", "10 >= 10 (граница)"),
        (9, "мало", "9 ≤ 10 (граница)"),
        (4, "мало", "4 ≤ 10"),
        (1, "мало", "1 ≤ 10"),
        (0, "мало", "0 ≤ 10"),
        (100, "много", "большое число"),
        (1000, "много", "очень большое число"),
        (50, "много", "среднее число"),
        (10, "мало", "10 >= 10 (граница)"),
        (-1, "мало", "отрицательное число"),
    ]

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ИНДИКАТОРА")
    print("=" * 60)

    passed = 0
    for qty, expected, comment in test_cases:
        result = _indicator(qty)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} qty={qty}: {result} (ожидалось {expected}) — {comment}")

    print("=" * 60)
    print(f"Пройдено: {passed} / {len(test_cases)}")

        


if __name__ == "__main__":
    '''
    test_fields()
    test_prices()
    '''
    test_indicator()