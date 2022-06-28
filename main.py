import random


#
#   CLASS
#
class Food:
    def __init__(self, food_name, food_price, food_stock):
        self.__food_name = food_name
        self.__food_price = food_price
        self.__food_stock = food_stock

    # SETTER METHODS
    def set_name(self, product_name):
        self.__food_name = product_name
    def set_price(self, product_price):
        self.__food_price = product_price
    def set_stock(self, food_stock):
        self.__food_stock = food_stock

    # GETTER METHODS
    def get_name(self):
        return self.__food_name
    def get_price(self):
        return self.__food_price
    def get_stock(self):
        return self.__food_stock





#
#   LIST
#
# Store name and price in a list
food_list = \
    [
        Food("Fishball", 5, random.randint(0, 300)),
        Food("Kwek-kwek", 10, random.randint(0, 300)),
        Food("Tempura", 5, random.randint(0, 300)),
        Food("Lumpia", 10, random.randint(0, 300)),
        Food("Isaw", 5, random.randint(0, 300)),
        Food("Hotdog", 20, random.randint(0, 300)),
        Food("Chicken skin", 5, random.randint(0, 300)),
        Food("Squid skin", 5, random.randint(0, 300)),
        Food("Siomai", 15, random.randint(0, 300))
    ]





#
#   FUNCTIONS
#
def order():
    ordered_food = []          # Store all food and their quantity to be ordered
    i = 0


    # Get total order
    print("How many orders will you make? ", end="")
    total_order = int(input())
    print("")



    while i < total_order:
        # Get order
        order_food = int(input("What is your order? "))



        # Get order quantity
        print("How many", food_list[order_food-1].get_name(), "do you want to order? ", end="")
        order_quantity = int(input())


        if order_quantity > food_list[order_food - 1].get_stock():
            print("\n>> SORRY, WE ONLY HAVE ", food_list[order_food-1].get_stock(), " OF ", food_list[order_food-1].get_name(), "AVAILABLE\n")
        else:
            ordered_food.insert(i, [order_food - 1, order_quantity])         # Add order to list
            print("\n>> ORDER", i + 1, "SUCCESSFULLY ADDED\n")
            i = i + 1



    # Display ordered food
    print("\n\n")
    print("+ -- -- -- -- -- -- -- -- -- -- -- -- -- +")
    print("|                                        |")
    print("|                                        |")
    print("|          ***   RECEIPT   ***           |")
    print("|                                        |")
    print("|                                        |")
    order_total = 0 # this stores total amount of all orders
    for j in range(total_order):
        # calculate amount of current order = price * quantity
        item_total = food_list[ordered_food[j][0]].get_price() * ordered_food[j][1]
        order_total = order_total + item_total
        print("| \t", ordered_food[j][1], food_list[ordered_food[j][0]].get_name(), ".......... ₱", item_total, "      |")
    print("|                                        |")
    print("|                                -----   |")
    print("|\t\t\t\t\t\t\t\t₱", order_total, "  |")
    print("|                                        |")
    print("|                                        |")
    print("|       THANK YOU FOR ORDERING!!!        |")
    print("|                                        |")
    print("+ -- -- -- -- -- -- -- -- -- -- -- -- -- +")





def food_menu():
    # Display menu
    print("Available today:   ")
    for i in range(len(food_list)):
        print("\t[" + str(i + 1) + "] ---", food_list[i].get_name(), "(", food_list[i].get_stock(), "avail.)", "  ..........  ₱",  str(food_list[i].get_price()))
    print("\n==================")


    # Call the order function to get the order/s
    order()





#
#   MAIN
#
if __name__ == "__main__":
    # Call the food_menu function to display the menu
    food_menu()
