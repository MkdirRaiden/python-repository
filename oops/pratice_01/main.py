from operator import itemgetter
from item import Item
Item.instantiate_from_csv()
print(Item.all)
item1 = Item('tablet', 30, 2)
item1.incremet_price(0.2)
print(item1.price)
item1.send_email()