from datetime import datetime, timedelta
from discount import apply_discount_to_best_seller, apply_discount_to_any_orders


class Testing:
    def __init__(self, id, name, price, qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

class Order:
    def __init__(self, product_id, date):
        self.product_id = product_id
        self.date = date


CURRENT = datetime(2024, 6, 15)
MAY_START = datetime(2024, 5, 1)
MAY_END = datetime(2024, 5, 31, 23, 59)
APRIL = datetime(2024, 4, 15)
JUNE = datetime(2024, 6, 5)


def print_test_report(passed, total):
    print("=" * 40)
    print("ОТЧЁТ О ТЕСТИРОВАНИИ")
    print(f"Пройдено: {passed} / {total}")
    if passed == total:
        print("Результат: ✅ УСПЕХ")
    else:
        print("Результат: ❌ НЕУДАЧА")
    print("=" * 40)
        

def run_test():
    test_cases = [
        # 1.
        (
            [
                Testing(1, "Йога", 1000, 50),
                Testing(2, "Кроссфит", 9000, 3),
            ],
            "Йога", 1000, 750
        ),

        # 2.
        (
            [
                Testing(3, "Бокс", 10000, 1),
                Testing(4, "Плавание", 500, 30),
                Testing(5, "Пилатес", 8000, 2),
            ],
            "Плавание", 500, 375
        ),

        # 3. Максимум по количеству в середине списка
        (
            [
                Testing(6, "Йога", 9000, 5),
                Testing(7, "Танцы", 100, 99),
                Testing(8, "Кроссфит", 7000, 10),
            ],
            "Танцы", 100, 75
        ),

        # 4. Максимум по количеству в конце списка
        (
            [
                Testing(9, "Йога", 5000, 1),
                Testing(10, "Бокс", 4000, 2),
                Testing(11, "Стретчинг", 300, 100),
            ],
            "Стретчинг", 300, 225
        ),

        # 5. Все количества равны — берётся первый
        (
            [
                Testing(12, "Йога", 1000, 10),
                Testing(13, "Кроссфит", 9000, 10),
                Testing(14, "Пилатес", 500, 10),
            ],
            "Йога", 1000, 750
        ),

        # 6. Две одинаковые максимальные количества — берётся первый
        (
            [
                Testing(15, "Аэробика", 200, 25),
                Testing(16, "Плавание", 8000, 25),
                Testing(17, "Бокс", 300, 5),
            ],
            "Аэробика", 200, 150
        ),

        # 7. Дорогая и популярная одновременно — но критерий только количество
        (
            [
                Testing(18, "Кроссфит", 10000, 40),
                Testing(19, "Йога", 500, 39),
            ],
            "Кроссфит", 10000, 7500
        ),

        # 8. Разница в 1 занятие
        (
            [
                Testing(20, "Пилатес", 100, 49),
                Testing(21, "Танцы", 9000, 50),
            ],
            "Танцы", 9000, 6750
        ),

        # 9. Одна тренировка
        (
            [
                Testing(22, "Йога", 3000, 7),
            ],
            "Йога", 3000, 2250
        ),

        # 10. Две тренировки — побеждает вторая по количеству
        (
            [
                Testing(23, "Бокс", 5000, 3),
                Testing(24, "Стретчинг", 200, 8),
            ],
            "Стретчинг", 200, 150
        ),

        # 11. Очень большая разница в количестве
        (
            [
                Testing(25, "Плавание", 9999, 2),
                Testing(26, "Йога", 100, 1000),
            ],
            "Йога", 100, 75
        ),

        # 12. Нулевое количество у самой дорогой
        (
            [
                Testing(27, "Кроссфит", 50000, 0),
                Testing(28, "Пилатес", 3000, 5),
            ],
            "Пилатес", 3000, 2250
        ),

        # 13. Максимум по количеству с минимальной ценой
        (
            [
                Testing(29, "Йога", 8000, 4),
                Testing(30, "Танцы", 6000, 6),
                Testing(31, "Аэробика", 50, 500),
            ],
            "Аэробика", 50, 37.5
        ),

        # 14. Все цены равны — решает количество
        (
            [
                Testing(32, "Йога", 1000, 3),
                Testing(33, "Кроссфит", 1000, 10),
                Testing(34, "Бокс", 1000, 7),
            ],
            "Кроссфит", 1000, 750
        ),

        # 15. Максимум по количеству — предпоследний
        (
            [
                Testing(35, "Йога", 100, 2),
                Testing(36, "Плавание", 200, 3),
                Testing(37, "Танцы", 9000, 77),
                Testing(38, "Пилатес", 300, 4),
            ],
            "Танцы", 9000, 6750
        ),
    ]
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ ДЛЯ ТРЕНИРОВОК")
    print("=" * 60)

    passed = 0

    for trainings, expected_name, expected_old, expected_new in test_cases:
        training, old_price, new_price = apply_discount_to_best_seller(trainings, 25)

        status = "✅" if (
            training is not None
            and training.name == expected_name
            and old_price == expected_old
            and new_price == expected_new
        ) else "❌"

        if status == "✅":
            passed += 1

        print(
            f"{status} Ожидалось: {expected_name}, "
            f"старая цена {expected_old}, новая цена {expected_new} | "
            f"Получено: {training.name if training else 'None'}, "
            f"старая цена {old_price}, новая цена {new_price}"
        )

    print_test_report(passed, len(test_cases))

def run_test_orders():
    test_cases = [
        # 1.
        (
            [
                Testing(1, "Йога", 1000, 50),
                Testing(2, "Кроссфит", 9000, 3),
            ],
            [Order(1, datetime(2024, 5, 10))],
            "Кроссфит", 9000, 6750
        ),
        # 2.
        (
            [
                Testing(3, "Бокс", 10000, 1),
                Testing(4, "Плавание", 500, 30),
            ],
            [Order(3, datetime(2024, 6, 5))],
            "Плавание", 500, 375
        ),

        # 3. Заказ в апреле (не прошлый месяц) не исключает
        (
            [
                Testing(5, "Пилатес", 8000, 20),
                Testing(6, "Танцы", 100, 5),
            ],
            [Order(5, datetime(2024, 4, 15))],
            "Пилатес", 8000, 6000
        ),

        # 4. Все товары заказаны в прошлом месяце — None
        (
            [
                Testing(7, "Йога", 1000, 10),
                Testing(8, "Бокс", 2000, 20),
            ],
            [
                Order(7, datetime(2024, 5, 1)),
                Order(8, datetime(2024, 5, 31, 23, 59)),
            ],
            None, None, None
        ),

        # 5. Граница прошлого месяца: 1 мая 00:00 — исключает
        (
            [
                Testing(9, "Йога", 1000, 10),
                Testing(10, "Бокс", 2000, 20),
            ],
            [Order(9, datetime(2024, 5, 1, 0, 0))],
            "Бокс", 2000, 1500
        ),

        # 6. Граница прошлого месяца: 31 мая 23:59 — исключает
        (
            [
                Testing(11, "Йога", 1000, 10),
                Testing(12, "Бокс", 2000, 20),
            ],
            [Order(11, datetime(2024, 5, 31, 23, 59))],
            "Бокс", 2000, 1500
        ),

        # 7. Граница текущего месяца: 1 июня 00:00 — НЕ исключает
        (
            [
                Testing(13, "Йога", 1000, 10),
                Testing(14, "Бокс", 2000, 20),
            ],
            [Order(13, datetime(2024, 6, 1, 0, 0))],
            "Йога", 1000, 750
        ),

        # 8. Пустой список заказов — выбирается максимальный qty
        (
            [
                Testing(15, "Йога", 1000, 10),
                Testing(16, "Бокс", 2000, 30),
                Testing(17, "Танцы", 300, 20),
            ],
            [],
            "Бокс", 2000, 1500
        ),

        # 9. Пустой список товаров — None
        (
            [],
            [Order(1, datetime(2024, 5, 10))],
            None, None, None
        ),

        # 10. Заказ на несуществующий product_id — игнорируется
        (
            [
                Testing(18, "Йога", 1000, 10),
                Testing(19, "Бокс", 2000, 20),
            ],
            [Order(999, datetime(2024, 5, 10))],
            "Бокс", 2000, 1500
        ),

        # 11. Несколько заказов в прошлом месяце — исключаются все
        (
            [
                Testing(20, "Йога", 1000, 100),
                Testing(21, "Бокс", 2000, 80),
                Testing(22, "Танцы", 300, 50),
            ],
            [
                Order(20, datetime(2024, 5, 5)),
                Order(21, datetime(2024, 5, 20)),
            ],
            "Танцы", 300, 225
        ),

        # 12. Один и тот же товар заказан несколько раз в прошлом месяце
        (
            [
                Testing(23, "Йога", 1000, 100),
                Testing(24, "Бокс", 2000, 10),
            ],
            [
                Order(23, datetime(2024, 5, 1)),
                Order(23, datetime(2024, 5, 15)),
                Order(23, datetime(2024, 5, 31)),
            ],
            "Бокс", 2000, 1500
        ),

        # 13. Скидка 0% — цена не меняется
        (
            [
                Testing(25, "Йога", 1000, 10),
                Testing(26, "Бокс", 2000, 20),
            ],
            [],
            "Бокс", 2000, 2000
        ),
    ]

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ ДЛЯ ТРЕНИРОВОК, КОТОРЫХ НЕ БЫЛО В ЗАКАЗАХ ПРОШЛОГО МЕСЯЦА")
    print("=" * 60)

    passed = 0
    discount = 25 # Фиксированная скидка

    for products, orders, expected_name, expected_old, expected_new in test_cases:
        import copy
        products_copy = copy.deepcopy(products)

        result = apply_discount_to_any_orders(
            products_copy, orders, discount, current_date=CURRENT
        )

        # result — это кортеж (best, old_price, new_price)
        best, old_price, new_price = result if result else (None, None, None)

        ok = (
            (best is None and expected_name is None)
            or (
                best is not None
                and expected_name is not None
                and best.name == expected_name
                and old_price == expected_old
                and new_price == expected_new
            )
        )

        status = "✅" if ok else "❌"
        if ok:
            passed += 1

        print(
            f"{status} Ожидалось: {expected_name}, "
            f"старая {expected_old}, новая {expected_new} | "
            f"Получено: {best.name if best else 'None'}, "
            f"старая {old_price}, новая {new_price}"
        )

    print_test_report(passed, len(test_cases))


if __name__ == "__main__":
    run_test_orders()