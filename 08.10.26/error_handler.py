from tkinter import messagebox

def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except FileNotFoundError as e:
        messagebox.showerror("Ошибка", f"Файл не найден:\n{e}")
    except ConnectionError as e:
        messagebox.showerror("Ошибка", f"Ошибка подключения к БД:\n{e}")
    except ValueError as e:
        messagebox.showerror("Ошибка", f"Неправильное значение:\n{e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")
    return None
      
        
def validate_positive_int(value, field_name):
    try:
        number = int(value)
    except ValueError:
        return (False, f"{field_name} должно быть целым числом!")

    if number <= 0:
        return (False, f"{field_name} должно быть больше нуля")

    return (True, number)