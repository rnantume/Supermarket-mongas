import stock_item
class Manager(Users, TillAtendant, StockItem):
    def add_stock_item(self):
        item_name = input("item_name")
        item_code = input("item_code")
        purchase_price = input("purchase_price")
        sale_price = input("sell_price")
        stock_item = StockItem()
        stock_item.add_item(item_name, item_code, purchase_price, sale_price) 
    def update_stock_balance(self):
        item_name = input("item_name")
        item_code = input("item_code")
        purchase_price = input("purchase_price")
        sale_price = input("sell_price")
        update_item = StockItem()
        update_item.update_item(item_name, item_code, purchase_price, sale_price)
    def search(self):
        till_attendant = TillAtendant()
        till_attendant.search_items()
    def sell(self):
        till_attendant = TillAtendant()
        till_attendant.sell_item_to_customers()


    