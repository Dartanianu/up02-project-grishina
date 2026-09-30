class Products:
    def __init__(self, id, name, coach, time, price, qty, picture):
        self.id = id
        self.name = name
        self.coach = coach
        self.time = time
        self.price = price
        self.qty = qty
        self.picture = picture

    def total(self):
        return self.price * self.qty

    def price_with_disc(self, disc_percent):
        return self.price * (1 - disc_percent / 100)

    def indicator(self):
        return "много" if self.qty > 5 else "мало"

    def info(self):
        return (
            f"{self.name} ({self.coach}): "
            f"{self.price} руб * {self.qty} = {self.total()} руб. "
            f"Длительность {self.time}."
            f"({self.indicator()})"
        )       