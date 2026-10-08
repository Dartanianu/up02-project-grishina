from catalog import _indicator

def test_indicator():
    test_cases = [
        (12, "много", "12 > 10"),
        (11, "много", "11 > 10"),
        (5, "мало", "5 <= 10"),
        (4, "мало", "4 <= 10"),
        (0, "мало", "0 <= 10"),
        (100, "много", "100 > 10"),
        (1, "мало", "мин > 0"),
        (-1, "мало", "отриц число(крайний случай"),
    ]
    
    print("=" * 60)
    print("Тестирование индикатора")
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
    
    print("=" * 60)
    print("Тесты индикатора")
    print("=" * 60)
    
    ind_cases = [
        (None,      "None — не число"),
        ("10",      "строка вместо числа"),
        (0.5,       "дробное число"),
    ]
    
    for qty, comment in ind_cases:
        try:
            result = _indicator(qty)
            print(f"⚠️  qty={qty!r}: вернул {result!r} — {comment}")
        except Exception as e:
            print(f"❗ qty={qty!r}: выброшено {type(e).__name__}: {e} — {comment}")
        
if __name__ == "__main__":
    test_indicator()