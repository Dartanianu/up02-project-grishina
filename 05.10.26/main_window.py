import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk
from config import APP_TITLE
from styles import COLOR_SECONDARY_BG, FONT_FAMILY, FONT_SIZE_TITLE, font
import db_products as db
from catalog import create_product_card
from resources import load_image_proportional, PATH_LOGO, PATH_ICON
from error_handler import safe_call


class CatalogWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("900x700")
        
        self.set_icon()
        self.set_app_icon(self.root, PATH_ICON)

        self.build_ui()
        self.load_products()
    
    def set_icon(self):
        import os
        try:
            if os.name == "nt":   # Windows
                self.root.iconbitmap(PATH_ICON)
            else:                  # Linux/Mac
                icon_img = load_image_proportional(
                    PATH_ICON.replace(".ico", ".png"),
                    max_size=(32, 32)
                )
                if icon_img:
                    self.root.iconphoto(True, icon_img)
        except Exception as e:
            print(f"Не удалось установить иконку: {e}")


    def build_ui(self):
        # Заголовок
        header = tk.Frame(self.root, bg=COLOR_SECONDARY_BG, height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        try: 
            pil_logo = Image.open("resources/logo.png").resize((60, 60))
            logo = ImageTk.PhotoImage(pil_logo)
            logo_label = tk.Label(header, image=logo, bg=COLOR_SECONDARY_BG)
            logo_label.image = logo
            logo_label.pack(side="left", padx=15)
        except FileNotFoundError:
            tk.Label(header, text="[ЛОГОТИП]",
                     bg=COLOR_SECONDARY_BG).pack(side="left", padx=15)


        tk.Label(header, text="КАТАЛОГ ТОВАРОВ",
                 font=(FONT_FAMILY, 16, "bold"),
                 bg="#D2F6E7").pack(pady=15)

        # Область с прокруткой
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical",
                                   command=self.canvas.yview)
        self.catalog_frame = tk.Frame(self.canvas, bg="white")
        self.catalog_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.catalog_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def set_app_icon(self, root, icon_path):
        import os
        from resources import load_image_proportional
        
        try:
            if os.name == "nt":
                if os.path.exists(icon_path):
                    root.iconbitmap(icon_path)
                else:
                    png_path = icon_path.replace(".ico", ".png")
                    icon_img = load_image_proportional(png_path, max_size=(32, 32))
                    if icon_img:
                        root.iconphoto(True, icon_img)
                        root._icon_photo = icon_img   # сохраняем ссылку
        except Exception as e:
            print(f"Не удалось установить иконку: {e}")


    def load_products(self):
        products = db.get_all_products()
        for p in products:
            safe_call(create_product_card, self.catalog_frame, p)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    CatalogWindow().run()
