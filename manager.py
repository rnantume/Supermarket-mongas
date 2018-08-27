import stock_item
class Manager(Users,TillAtendant.StockItem):
    def add_stock_item(self):
         item_name = input("item_name")
         item_code = input("item_code")
         purchase_price = input("purchase_price")
         sale_price = input("sell_price")
        stock_item = StockItem(item_name, item_code, purchase_price, sale_price)
        stock_item.add_item() 
    def update_stock_balance():
        pass      
    