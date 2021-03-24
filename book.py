class Order:
    #Constructor
    def __init__(self,quantity,price,id,buy=True):
        self.quantity=quantity
        self.price=price
        self.buy=buy
        self.id = id

    def __eq__(self, other):
        return other and self.quantity == other.quantity and self.price == other.price

    def __lt__(self, other):
        return other and self.price < other.price

    def __str__(self):
        return "%s at %s" % (self.quantity, self.price)
    
class Book:
    #Constructor
    def __init__(self,name):
        self.name=name
        self.buy_orders = []
        self.sell_orders = []
        self.compteur = 0
    
    #basic display
    '''
    def Book_display(self):
        affichage="Book on %s" %(self.name)
        for i in range(len(self.sell_orders)):
            affichage+="\n\tSELL %s id=%d" %(self.sell_orders[i],self.sell_orders[i].id)
        for j in range (len(self.buy_orders)):
            affichage+="\n\tBUY %s id=%d" %(self.buy_orders[j],self.buy_orders[j].id)
        return affichage + "\n--------------------------------------"'''

    #tabular display
    def Book_display(self):
        df_buy = pandas.DataFrame(self.buy_orders, columns=["BUY"])
        df_sell = pandas.DataFrame(self.sell_orders, columns=["SELL"])
        final_df = pandas.concat([df_buy, df_sell], axis = 1).fillna("           ")
        return(final_df.to_markdown())

    #We sort the buy orders list in decreasing order
    def sortBuyOrders(self): 
        self.buy_orders.sort(key=lambda x : x.price, reverse= True)
    
    #We sort the buy orders list in increasing order
    def sortSellOrders(self):
        self.sell_orders.sort(key=lambda x : x.price, reverse= False)

    def insert_buy(self, quantity, price):
        self.compteur += 1   #order's id
        insert = True
        Book.sortSellOrders(self)
        print ("Insert BUY %s id=%d on %s" %(Order(quantity,price,self.compteur),self.compteur,self.name))
        if(len(self.sell_orders) != 0):
            while quantity > 0:
                #We check if there is at least one sell order less than or equal to the buy order 
                if(self.sell_orders[0] < Order(quantity, price, self.compteur) or self.sell_orders[0].price == price):
                    #if we have enough sell orders, we just execute the order and reduce the quantity. We don't insert the buy order since the quantity is 0
                    if(self.sell_orders[0].quantity > quantity):
                        self.sell_orders[0].quantity -= quantity
                        insert = False
                        print ("Execute %s on %s" %(Order(quantity,self.sell_orders[0].price, self.compteur),self.name))
                        break
                    #if the quantities of the sell and buy order are equal, we execute the order and delete the sell order (quantity = 0)
                    elif(self.sell_orders[0].quantity == quantity):
                        del self.sell_orders[0]
                        insert = False
                        print ("Execute %s on %s" %(Order(quantity,self.sell_orders[0].price, self.compteur),self.name))
                        break
                    #if the sell order's quantity is not great enough, we delete the sell order and check if there is another one we can execute
                    else:
                        quantity -= self.sell_orders[0].quantity
                        print ("Execute %s on %s" %(Order(self.sell_orders[0].quantity,self.sell_orders[0].price, self.compteur),self.name))
                        del self.sell_orders[0]
                else:
                    break
        if(insert):
            #We add the buy order if we didn't find any correponding sell order or if there still left quantity
            self.buy_orders.append(Order(quantity, price, self.compteur))
        Book.sortBuyOrders(self)
        print(Book.Book_display(self), "\n\n")

    def insert_sell(self, quantity, price):
        self.compteur += 1    #order's id
        insert = True
        Book.sortBuyOrders(self)
        print ("Insert SELL %s id=%d on %s" %(Order(quantity,price,self.compteur),self.compteur,self.name))
        if(len(self.buy_orders) != 0):
            while quantity > 0:
                #We check if there is at least one buy order more than or equal to the sell order 
                if(self.buy_orders[0] > Order(quantity, price, self.compteur) or self.buy_orders[0].price == price):
                    #if we have enough buy orders, we just execute the order and reduce the quantity. We don't insert the sell order since the quantity is 0
                    if(self.buy_orders[0].quantity > quantity):
                        self.buy_orders[0].quantity -= quantity
                        insert = False
                        print ("Execute %s on %s" %(Order(quantity,self.buy_orders[0].price, self.compteur),self.name))
                        break
                    #if the quantities of the sell and buy order are equal, we execute the order and delete the buy order (quantity = 0)
                    elif(self.buy_orders[0].quantity == quantity):
                        del self.buy_orders[0]
                        insert = False
                        print ("Execute %s on %s" %(Order(quantity,self.buy_orders[0].price, self.compteur),self.name))
                        break
                     #if the buy order's quantity is not great enough, we delete the buy order and check if there is another one we can execute
                    else:
                        quantity -= self.buy_orders[0].quantity
                        print ("Execute %s on %s" %(Order(self.buy_orders[0].quantity,self.buy_orders[0].price, self.compteur),self.name))
                        del self.buy_orders[0]
                else:
                    break
        if(insert):
            #We add the sell order if we didn't find any correponding buy order or if there still left quantity
            self.sell_orders.append(Order(quantity, price, self.compteur))
        Book.sortSellOrders(self)
        print(Book.Book_display(self), "\n\n")




