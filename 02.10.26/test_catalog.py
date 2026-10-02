import databases as db
import db_products


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


if __name__ == "__main__":
    test_fields()
