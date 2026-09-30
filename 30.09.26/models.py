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
    
    def indicator(self):
        return "много" if self.qty > 10 else "мало"
    
    def is_avaible(self):
        return self.qty > 0

    def info(self):
        return (
            f"{self.name} ({self.coach}): "
            f"{self.price} руб * {self.qty} = {self.total()} руб. "
            f"Длительность {self.time}."
            f"({self.indicator()})"
        )
        
class Order:
    def __init__(self, id, data, client, product, qty):
        self.id = id
        self.data = data
        self.client = client
        self.product = product
        self.qty = qty
    
    def total(self):
        return self.product.price * self.qty

    def info(self):
        return f"Заказ №{self.id} от {self.data}: {self.client} - {self.product.name} x {self.qty}"