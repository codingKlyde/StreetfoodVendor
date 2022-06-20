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



def food_menu():
    # Display menu using loop
    print("AVAILABLE TODAY:")
    for i in range(len(food_list)):
        print("\t[", str(i + 1), "] ", food_list[i].get_name(), " .......... ₱",  str(food_list[i].get_price()))
    print("\n\n----------")





def order(food_list):
    # Get orders of the user
    order_food = input("Enter your orders: ")
    order_food = order_food.split()

    order_food = food_list()
    # Total ordered foods of each type
    food_total = [0] * len(food_list)

    # Loop to get the total of each food type
    for i in range(len(order_food)):
        # Convert each item to int type
        order_food[i] = int(order_food[i])

        if order_food[i] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            food_total[order_food[i] - 1] += 1


    # Display ordered food
    print("\n\n*** RECEIPT ***")
    for i in range(len(food_list)):
        print("\t ", str(food_total[i]), food_list[i].get_name(), " ( ₱ ", str(food_list[i].get_price() * food_total[i]), ")")
    print("----------")
    print("TOTAL PRICE: ", )
    print("----------")

    return food_list





if __name__ == "__main__":
    food_menu()
    order(food_list)
