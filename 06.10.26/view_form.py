import tkinter as tk
from tkinter import ttk, messagebox

from styles import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, FONT_SIZE_TITLE, FONT_FAMILY, font
)
from resources import load_image, get_product_image
from error_handler import validate_positive_int

from order_manager import (
    add_order_to_db, 
    update_product_quantity, 
    get_product_quantity
)



class ViewForm:
    def __init__(self, parent, product, on_add_to_order=None):
        self.product = product
        self.on_add_to_order = on_add_to_order
        
        self.window = tk.Toplevel(parent)
        self.window.title(f"Просмотр — {product.name}")
        self.window.geometry("700x600")
        self.window.configure(bg=COLOR_MAIN_BG)
        
        self.build_ui()
    
    def build_ui(self):
        """Строит интерфейс формы."""
        # Шапка — ГОТОВО
        header = tk.Frame(self.window, bg=COLOR_SECONDARY_BG, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text="КАРТОЧКА ТОВАРА",
                 font=font(FONT_SIZE_TITLE, bold=True),
                 bg=COLOR_SECONDARY_BG).pack(pady=15)
        
        # Основная область — ГОТОВО
        main = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        main.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Изображение — ГОТОВО
        img_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        img_frame.pack(side="left", padx=10)
        
        photo = get_product_image(self.product.picture, size=(200, 200))
        if photo:
            img_label = tk.Label(img_frame, image=photo, bg=COLOR_MAIN_BG)
            img_label.image = photo
            img_label.pack()
        

        info_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        info_frame.pack(side="left", fill="both", expand=True, padx=20)
        
        #Информация
        self._add_field(info_frame, "Тип", self.product.name)
        self._add_field(info_frame, "Тренер", self.product.coach)
        self._add_field(info_frame, "Длительность", self.product.time)
        self._add_field(info_frame, "Количество", self.product.qty)
        self._add_field(info_frame, "Цена", self.product.price)
        
        #поле ввода кол-ва
        qty_frame = tk.Frame(info_frame, bg=COLOR_MAIN_BG)
        qty_frame.pack(fill="x", pady=(10, 0))
        
        tk.Label(qty_frame, text="Количество тренировок:", font=font(FONT_SIZE_HEADER, bold=True), bg=COLOR_MAIN_BG, width=25, anchor="w").pack(side="left")
        
        self.qty_var = tk.StringVar(value="1")
        qty_entry = tk.Entry(qty_frame, textvariable=self.qty_var, font=font(FONT_SIZE_NORMAL), width=10)
        qty_entry.pack(side="left")
        
        #КНОПКИ:
        
        #карточка
        btn_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", pady=10)
        
        #Добавить
        btn_add = tk.Button(btn_frame, text="Добавить в заказ", command=self.add_to_order, bg=COLOR_ACCENT, fg="white", font=font(FONT_SIZE_NORMAL), padx=15, pady=5)
        btn_add.pack(side="left", padx=20)

        #назад
        btn_back = tk.Button(btn_frame, text="Назад", command=self.window.destroy,bg=COLOR_ACCENT, fg="white", font=font(FONT_SIZE_NORMAL), padx=15, pady=5)
        btn_back.pack(side="left", padx=20)
    
    def _add_field(self, parent, label, value):
        row = tk.Frame(parent, bg=COLOR_MAIN_BG)
        row.pack(fill="x", pady=3)
        
        label_txt = tk.Label(row, text=f"{label}:", font=font(FONT_SIZE_NORMAL, bold=True), width=15, anchor="w", bg=COLOR_MAIN_BG).pack(side="left")
        
        value_txt = tk.Label(row, text=str(value), font=font(FONT_SIZE_NORMAL),
        anchor="w", justify="left", wraplength=300, bg=COLOR_MAIN_BG)
        value_txt.pack(side="left", fill="x", expand=True)
    
    def add_to_order(self):
        ok, result = validate_positive_int(self.qty_var.get(), "Количество")
        if not ok:
            messagebox.showerror("Ошибка ввода", result)
            return
        qty = result
        
        if not self.product:
            messagebox.showerror("Ошибка", "Товар не выбран")
            return
        
        try:
            product_id = self.product.id
            qty_now = get_product_quantity(product_id)

            if qty_now < 1:
                messagebox.showwarning("Внимание", "Товар закончился")
                return
            if qty > qty_now:
                messagebox.showwarning("Внимание", f"В наличии только {qty_now} шт.")
                return
            
            new_qty = qty_now - qty
            add_order_to_db("Иванов Иван Иванович", product_id, 1)
            update_product_quantity(product_id, new_qty)
            
            messagebox.showinfo("Успех", "Заказ оформлен")
            
            if self.on_add_to_order:
                self.on_add_to_order()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось оформить заказ{e}")