class Food:
    def __init__(self, food_name, food_price):
        self.__food_name = food_name
        self.__food_price = food_price

    # SETTER METHODS
    def set_name(self, product_name):
        self.__food_name = product_name
    def set_price(self, product_price):
        self.__food_price = product_price

    # GETTER METHODS
    def get_name(self):
        return self.__food_name
    def get_price(self):
        return self.__food_price





# Store name and price in a list
food_list = \
    [
        Food("Fishball", 5),
        Food("Kwek-kwek", 10),
        Food("Tempura", 5),
        Food("Lumpia", 10),
        Food("Isaw", 5),
        Food("Hotdog", 20),
        Food("Chicken skin", 5),
        Food("Squid skin", 5),
        Food("Siomai", 15)
    ]





def order():
    food_name = ""
    food_price = 0
    order_total = 0
    total = 2

    for i in range(total):
        # Get order from the user
        order_food = int(input("What it is your order?   "))

        # Determine the order
        for j in range(order_food):
            food_list[i].get_name()
            food_list[i].get_price()

        order_total = int(input("How many do you want to order?   "))


    # Display ordered food
    print("\n\n")
    print("+ -- -- -- -- -- -- -- -- -- -- -- -- -- +")
    print("|                                        |")
    print("|          ***   RECEIPT   ***           |")
    print("|                                        |")
    print("|                                        |")
    for i in range(total):
        print("| \t", order_total, food_list[i].get_name(), ".......... ₱", food_list[i].get_price() * order_total, "     |")
    print("|                                        |")
    print("+ -- -- -- -- -- -- -- -- -- -- -- -- -- +")





def food_menu():
    # Display menu using loop
    print("AVAILABLE TODAY:: ")
    for i in range(len(food_list)):
        print("\t[", str(i + 1), "] ", food_list[i].get_name(), " .......... ₱",  str(food_list[i].get_price()))
    print("\n=========")

    # Call the order() after displaying the menu
    order()





#
if __name__ == "__main__":
    food_menu()
