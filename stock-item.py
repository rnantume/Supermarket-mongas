import datetime
items = []
class StockItem:
    def ___init__(self,item_name, item_code, purchase_price, sale_price, quantity, time_stamp):
        self.item_name = input("enter item name")
        self.item_code = input("enter item code")
        self.purchase_price = input("enter purchase price")
        self.sale_price = input("enter sale_price")
        self.quantity = input("enter quantity")
        self.time_stamp = datetime.datetime.now()

    def add_item(self):
        item = {
            "item_name": self.item_name,
            "item_code": self.item_code,
            "purchase_price": self.purchase_price,
            "sale_price": self.sale_price,
            "quantity": self.quantity,
            "time_stamp": self.time_stamp
        }
        items.append(item)
    @staticmethod   
    def sale_item(item_name, sale_qty):
        for item in items:
            if item['item_name']==item_name:
                new_quantity = item['quantity']- sale_qty
                return new_quantity
            else:
                return("Item not available")   

        
        
