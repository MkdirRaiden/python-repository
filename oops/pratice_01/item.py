import csv
from logging import raiseExceptions
class Item:
    all = []
    pay_rate = 0.8
    def __init__(self, name:str, price:float, quantity:int):
        self.__name = name
        self.__price = price 
        self.quantity = quantity
        assert price>=0, "Invalid price number"
        assert quantity>=0, "Invalid quantity number"
        Item.all.append(self)
    @property
    def price(self):
        return self.__price    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate  
    def incremet_price(self, increment_value):
        self.__price=self.__price*self.__price*increment_value        
    @property
    def name(self):
        return self.__name 
    @name.setter
    def name(self, value):
        if len(value) >10:
            raise Exception("Your name is too long")
        else:
            self.__name = value       
    def calculate_total_price(self):
        return self.__price * self.quantity
    @classmethod
    def instantiate_from_csv(cls):
        with open('file_item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            ) 
    @staticmethod
    def check_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name, self.price, self.quantity})"   
    def __connect(self, smpt_server):
        pass
    def __body_email(self):
        return " "
    def __send(self):
        pass
    def send_email(self):
        self.__connect('')
        self.__body_email()
        self.__send()
