class Order:
    def __init__(self,quantity,price,buy=True):
        self.quantity=quantity
        self.price=price
        self.buy=buy

    def __eq__(self, other):
        return other and self.quantity == other.quantity and self.price == other.price

    def __lt__(self, other):
        return other and self.price < other.price

    def __str__(self):
        return "%s  at  %s" % (self.quantity, self.price)
    
class Book:
    def __init__(self,name,buy_orders,sell_orders):
        self.name=name
        self.buy_orders=buy_orders
        self.sell_orders=sell_orders

    def __str__(self, order_type):
        
    
    def insert_buy(self, quantity, price):
        insert = True
        for i in range(len(sell_orders)):
            if(sell_orders[i] < Order(quantity, price) or sell_orders[i].price == price):
                if(sell_orders[i].quantity > quantity):
                    sell_orders[i].quantity -= quantity
                    insert = False
                elif(sell_orders[i].quantity == quantity):
                    del sell_orders[i]
                    insert = False
                else:
                    quantity -= sell_orders[i].quantity
                    del sell_orders[i]
        if(insert):
            self.buy_orders.append(Order(quantity, price))

    def insert_sell(self, quantity, price):
        insert = True
        for i in range(len(buy_orders)):
            if(buy_orders[i] > Order(quantity, price) or buy_orders[i].price == price):
                if(buy_orders[i].quantity > quantity):
                    buy_orders[i].quantity -= quantity
                    insert = False
                elif(buy_orders[i].quantity == quantity):
                    del buy_orders[i]
                    insert = False
                else:
                    quantity -= buy_orders[i].quantity
                    del buy_orders[i]
        if(insert):
            self.sell_orders.append(Order(quantity, price))

