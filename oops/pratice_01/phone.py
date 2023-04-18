from item import Item
class phone(Item):
    pay_rate=0.5
    def __init__(self, name: str, price: float, quantity: int, broken_phone=0):
        super().__init__(name, price, quantity)
        assert broken_phone>=0, f"broken phone={broken_phone}, invalid number" 
        self.broken_phone = broken_phone