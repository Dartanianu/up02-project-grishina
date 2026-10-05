from catalog import _indicator

def test_indicator():
    test_cases = [
        (12, "много", "12 > 10"),
        (11, "много", "11 > 10"),
        (5, "мало", "5 <= 10"),
        (4, "мало", "4 <= 10"),
        (0, "мало", "0 <= 10"),
        (100, "много", "100 <= 10"),
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
    
if __name__ == "__main__":
    test_indicator()