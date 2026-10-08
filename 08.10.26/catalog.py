import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_FAMILY, FONT_SIZE_NORMAL, FONT_SIZE_HEADER, COLOR_ACCENT, font
)
from config import DB_PATH
from resources import get_product_image
import databases as db


def _open_view(parent, product, refresh=None):
    from view_form import ViewForm
    ViewForm(parent, product, on_add_to_order=refresh)


def create_product_card(parent, product, refresh=None):
    qty = product.qty
    bg_color = _get_card_color(qty)

    # карточка
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)
    card.bind("<Button-1>", lambda e: _open_view(parent, product, refresh))
    
    _add_image(card, product, bg_color)
    _add_text_info(card, product, bg_color, qty)
    
    def _bind_recursive(widget):
        widget.bind("Button-1", lambda e: _open_view(parent, product, refresh))
        for child in widget.winfo_children():
            _bind_recursive(child)
    
    _bind_recursive(card)
    
    return card
    

def _get_card_color(qty):
    return COLOR_HIGHLIGHT if qty <= 5 else COLOR_MAIN_BG


def _add_image(card, product, bg_color):
    # изображение (слева)
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    photo = get_product_image(product.picture, size=(100,100))
    if photo:
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo
        img_label.pack()
    else:
        tk.Label(img_frame, text="[НЕТ ФОТО]", bg=bg_color, width=10, height=5).pack()


def _add_text_info(card, product, bg_color, qty, on_view=None):
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    
    name = product.name if product.name else "[Без названия]"
    coach = product.coach if product.coach else "[Без тренера]"
    time = product.time if product.time else "[Без времени]"
    price = product.price if product.price is not None else 0


    indicator = _indicator(qty)
    _add_label(text_frame, f"{name} | {coach}",bg_color, bold=True, size=FONT_SIZE_HEADER)
    _add_label(text_frame, f"Длительность: {time} мин.", bg_color)
    _add_label(text_frame, f"Количество: {indicator} ({qty})", bg_color)
    _add_label(text_frame, f"{price} руб.",bg_color, bold=True, size=FONT_SIZE_HEADER, align="e")


def _add_label(parent, text, bg_color, bold=False, size=FONT_SIZE_NORMAL, align="w"):
    tk.Label(parent, text=text, font=font(size, bold=bold),
             bg=bg_color, anchor=align).pack(fill="x")


def _indicator(qty):
    return "много" if qty > 10 else "мало"

