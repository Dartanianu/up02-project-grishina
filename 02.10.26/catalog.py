import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from config import db_path, color_highlight, font_family
import databases as db


def create_product_card(parent, product):
    qty = product.qty
    bg_color = color_highlight if qty <= 3 else "white"

    # карточка
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # изображение (слева)
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    img_path = product.picture if product.picture else "resources/picture.png"
    if not os.path.exists(img_path):
        img_path = "resources/picture.png"
    
    try:
        img = Image.open(img_path).resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        img_lable = tk.Label(img_frame, image=photo, bg=bg_color)
        img_lable.image = photo
        img_lable.pack()
    except Exception:
        tk.Label(img_frame, text="[ФОТО]", bg=bg_color, width=10, height=5).pack()

    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Тип | тренер
    title = f"{product.name} | {product.coach}"
    tk.Label(text_frame, text=title, font=(font_family, 14, "bold"),
             bg=bg_color, anchor="w").pack(fill="x")

    # Количество
    indicator = "много" if qty >= 10 else "мало"
    bg_color_ind = "#ff8080" if qty < 10 else "white"
    tk.Label(text_frame, text=f"Количество: {indicator} ({qty})",
             font=(font_family, 11), bg=bg_color_ind, anchor="w").pack(fill="x")
    
    # Длительность
    tk.Label(text_frame, text=f"{product.time} минут.",
             font=(font_family, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Цена (справа)
    tk.Label(text_frame, text=f"{product.price} руб.",
             font=(font_family, 14, "bold"),
             bg=bg_color, anchor="e").pack(fill="x")
    
    separator = ttk.Separator(parent, orient="horizontal")
    separator.pack(fill="x", padx=10, pady=2)

    return card

