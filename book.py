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
        
    def __str__():
        affichage="Book on %s" %(self.name)
        for i in range(len(self.sell_orders)):
            affichage+="\n\tSELL %s id=%d" %(Order(quantity,price),i)
        for j in range (len(self.buy_orders)):
            affichage+="\n\tBUY %s id=%d" %(Order(quantity,price),j)

    
    def insert_buy(self, quantity, price):
        insert = True
        print ("Insert BUY %s id=%d on %s" %(Order(quantity,price),len(self.buy_orders)+1,self.name))
        for i in range(len(sell_orders)):
            if(sell_orders[i] < Order(quantity, price) or sell_orders[i].price == price):
                if(sell_orders[i].quantity > quantity):
                    sell_orders[i].quantity -= quantity
                    insert = False
                    print ("Execute %s on %s" %(Order(quantity,price),self.name))
                elif(sell_orders[i].quantity == quantity):
                    del sell_orders[i]
                    insert = False
                    print ("Execute %s on %s" %(Order(quantity,price),self.name))
                else:
                    executed_quantity=quantity
                    quantity -= sell_orders[i].quantity
                    del sell_orders[i]
                    print ("Execute %s on %s" %(Order(executed_quantity,price),self.name))
        if(insert):
            self.buy_orders.append(Order(quantity, price))
        print(str(Book(self.name,self.buy_orders,self.sell_orders)))



    def insert_sell(self, quantity, price):
        insert = True
        print ("Insert SELL %s id=%d on %s" %(Order(quantity,price),len(self.sell_orders)+1,self.name))
        for i in range(len(buy_orders)):
            if(buy_orders[i] > Order(quantity, price) or buy_orders[i].price == price):
                if(buy_orders[i].quantity > quantity):
                    buy_orders[i].quantity -= quantity
                    insert = False
                    print ("Execute %s on %s" %(Order(quantity,price),self.name))
                elif(buy_orders[i].quantity == quantity):
                    del buy_orders[i]
                    insert = False
                    print ("Execute %s on %s" %(Order(quantity,price),self.name))
                else:
                    executed_quantity=quantity
                    quantity -= buy_orders[i].quantity
                    del buy_orders[i]
                    print ("Execute %s on %s" %(Order(executed_quantity,price),self.name))
        if(insert):
            self.sell_orders.append(Order(quantity, price))
        print(str(Book(self.name,self.buy_orders,self.sell_orders)))




