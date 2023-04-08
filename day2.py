# Recreate your shopping cart program with OOP:
# The user should be able to :
# add items,
# delete items,
# check their cart, 
# quit
# When the user selects quit it should break our of the program and display the items in their cart.

#need an __init__ function - add contents that will remain in __init__
# 4 individual functions named methods add(quantity, options), remove(quantity, item), view(show cart, displaying cart), quit(break exiting cart).
# create a runner outside oF class(example (while True))
# Welcome user with an Input(what would you like to do
from IPython.display import clear_output as clear
class Cart():
 pass
def __init__(self):
    self.items = {}

def add_item(self):
   clear()
   new_item = input("What would you like to add?(Dairy products, Canned Food, Frozen Food, Snacks?)")
   quantity = input("how much {new_item} would you like? Input an amount please")
   if new_item not in self.items():
      self.items[new_item] = quantity
   else:
        self.items[new_item] += quantity
        print(f"{quantity} {new_item} has been added to your cart")
def remove_item():
    clear()
    discard = input("what would you like to remove")
    quantity = input("how much would you like to remove?")
    try:
       self.items[discard] -= quantity
       if self.item[discard] <= 0:
          del self.item[discard]
       print(f"{quantity} {discard} have been reomoved")
    except:
       print(f"{discard} was not in your cart please select another option!")
def show(self):
    print("your cart has the following items!")
    for item, quantity, in self.items.items():
      print(f"{item} / quanity {quantity}")
def checkout():
    if not self.items:
      print("please buy something dont be cheap!!")
    else:
      print("Thanks for shopping with us thank you for your time my friend!!")
      self.show()

class Main:
    def show_instructions():
      print("""
      welcome to Food_mart where food is Avg!!
      [1] Show Cart
      [2] Add Item
      [3] Remove
      [4] Checkout
      [5] Show Instructions
      """)
    def run():
       Main.show_instructions()
       my_cart = Cart()

       while True:
          Choice = input("what would you like to do")
          if Choice == '1':
            if my_cart.items == {}:
                print("your cart is empty")
            else:
                my_cart.show()
          elif Choice == '2':
             my_cart.add_item()
          elif Choice == '3':
            if my_cart == {}:
                print("your cart is empy")
            else:
                my_cart.remove_item()
          elif Choice == '4':
             my_cart.checkout()
             break
          elif Choice == '5':
            Main.show_instructions()
          else:
             print("this is an invalid output please try again Thank you!!")
        
Main.run()