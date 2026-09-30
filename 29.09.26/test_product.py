from models import Products

p = Products(
    id=1,
    name="Йога",
    coach="Ольга Морозова",
    time=60,
    price=1500,
    qty=4,
    picture="yoga.png"
)

print(p.info())
print(f"Со скидкой 25%: {p.price_with_disc(25):.2f} руб.")