'''class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        pass
    
    def cal_price(self):
        return self.price * self.quantity
    
    def info(self):
        print(f"There are total {self.quantity} {self.name} and total Price of the {self.name} are {self.cal_price()}")
    
    pass


class Phone(Item):
    
    

  
    pass


item1 = Phone("Phone",200, 4)
item2 = Item("laptops", 1000, 6)
#print(f"There are total {item1.quantity} {item1.name} and total Price of the {item1.name} are {item1.cal_price()}")
item2.info()'''




'''x = 5

try:
    if x>0:
      print(x)
except:
    print("An error occurred")
finally:
   print("this is final block")'''


username = input("Enter your Username")


print(F"Your Username is {username}")
