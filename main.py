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





def main():
    f1 = Food("Fishball", 5)
    f2 = Food("Kwek-kwek", 10)
    f3 = Food("Tempura", 5)
    f4 = Food("Lumpia", 10)
    f5 = Food("Isaw", 5)
    f6 = Food("Hotdog", 20)
    f7 = Food("Chicken skin", 5)
    f8 = Food("Squid skin", 5)
    f9 = Food("Siomai", 15)

    print("AVAILABLE TODAY:")
    print("\t[1] ", f1.get_name(), "     ..........  ₱", f1.get_price())
    print("\t[2] ", f2.get_name(), "    ..........  ₱", f2.get_price())
    print("\t[3] ", f3.get_name(), "      ..........  ₱", f3.get_price())
    print("\t[4] ", f4.get_name(), "       ..........  ₱", f4.get_price())
    print("\t[5] ", f5.get_name(), "         ..........  ₱", f5.get_price())
    print("\t[6] ", f6.get_name(), "       ..........  ₱", f6.get_price())
    print("\t[7] ", f7.get_name(), " ..........  ₱", f7.get_price())
    print("\t[8] ", f8.get_name(), "   ..........  ₱", f8.get_price())
    print("\t[9] ", f9.get_name(), "       ..........  ₱", f9.get_price())
    print("\n----------")
    order_food = input("Enter your orders:  ")
    order_food = order_food.split()
    print("\n\nORDER SUCCESSFULLY ADDED_")


    # Total ordered foods of each type
    f1_total = 0
    f2_total = 0
    f3_total = 0
    f4_total = 0
    f5_total = 0
    f6_total = 0
    f7_total = 0
    f8_total = 0
    f9_total = 0

    # For this warning, read here: https://stackoverflow.com/questions/51800809/warning-when-python-access-2d-list-with-none-value
    for i in range(len(order_food)):
        order_food[i] = int(order_food[i])         # Convert each item to int type

        if order_food[i] == 1:
            f1_total = f1_total + 1
        elif order_food[i] == 2:
            f2_total = f2_total + 1
        elif order_food[i] == 3:
            f3_total = f3_total + 1
        elif order_food[i] == 4:
            f4_total = f4_total + 1
        elif order_food[i] == 5:
            f5_total = f5_total + 1
        elif order_food[i] == 6:
            f6_total = f6_total + 1
        elif order_food[i] == 7:
            f7_total = f7_total + 1
        elif order_food[i] == 8:
            f8_total = f8_total + 1
        elif order_food[i] == 9:
            f9_total = f9_total + 1

    # Display ordered food
    print("\n\n+ - - - - - - - - - - - - - - - - +")
    print("|                                 |")
    print("|        *** RECEIPT ***          |")
    print("|                                 |")
    print("|                                 |")
    print("|   ", f1_total, f1.get_name(), "    .....  ₱", f1.get_price() * f1_total, "   |")
    print("|   ", f2_total, f2.get_name(), "   .....  ₱", f2.get_price() * f2_total, "   |")
    print("|   ", f3_total, f3.get_name(), "     .....  ₱", f3.get_price() * f3_total, "   |")
    print("|   ", f4_total, f4.get_name(), "      .....  ₱", f4.get_price() * f4_total, "   |")
    print("|   ", f5_total, f5.get_name(), "        .....  ₱", f5.get_price() * f5_total, "   |")
    print("|   ", f6_total, f6.get_name(), "      .....  ₱", f6.get_price() * f6_total, "   |")
    print("|   ", f7_total, f7.get_name(), ".....  ₱", f7.get_price() * f7_total, "   |")
    print("|   ", f8_total, f8.get_name(), "  .....  ₱", f8.get_price() * f8_total, "   |")
    print("|   ", f9_total, f9.get_name(), "      .....  ₱", f9.get_price() * f9_total, "   |")
    print("|                                  |", )
    print("+----------------------------------+")






if __name__ == "__main__":
    main()
