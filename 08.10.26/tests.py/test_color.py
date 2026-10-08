from catalog import _get_card_color
from styles import COLOR_HIGHLIGHT, COLOR_MAIN_BG

def test_color():
    test_cases = [
        (20, COLOR_MAIN_BG, "20 > 5"),
        (10, COLOR_MAIN_BG, "10 > 5"),
        (6, COLOR_MAIN_BG, "6 > 5"),
        (5, COLOR_HIGHLIGHT, "5 <= 5(граница)"),
        (4, COLOR_HIGHLIGHT, "4 < 5"),
        (2, COLOR_HIGHLIGHT, "2 < 5"),
        (100, COLOR_MAIN_BG, "100 > 5"),
        (-1, COLOR_HIGHLIGHT, "-1 < 5"),
    ]
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ПОДСВЕТКИ")
    print("=" * 60)

    passed = 0
    for qty, expected, comment in test_cases:
        result = _get_card_color(qty)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} qty={qty}: {result} "
              f"(ожидалось {expected}) — {comment}")

    print("=" * 60)
    print(f"Пройдено: {passed} / {len(test_cases)}")


if __name__ == "__main__":
    test_color()
