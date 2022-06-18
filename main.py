class Product:
    def __init__(self, product_name, product_price):
        self._product_name = product_name
        self._product_price = product_price

    # SETTER METHODS
    def set_name(self, product_name):
        self._product_name = product_name
    def set_price(self, product_price):
        self._product_price = product_price

    # GETTER METHODS
    def get_name(self):
        return self._product_name
    def get_price(self):
        return self._product_price




# FUNCTION TO DISPLAY THE FOOD MENU
def main():
    product1 = Product("Fishball", 5)
    product2 = Product("Kwek-kwek", 10)
    product3 = Product("Tempura", 5)
    product4 = Product("Lumpia", 10)
    product5 = Product("Isaw", 5)
    product6 = Product("Hotdog", 20)
    product7 = Product("Chicken skin", 5)
    product8 = Product("Squid skin", 5)
    product9 = Product("Siomai", 15)

    print("AVAILABLE TODAY:")
    print("\t[1] ", product1.get_name(), "     ..........  ₱", product1.get_price())
    print("\t[2] ", product2.get_name(), "    ..........  ₱", product2.get_price())
    print("\t[3] ", product3.get_name(), "      ..........  ₱", product3.get_price())
    print("\t[4] ", product4.get_name(), "       ..........  ₱", product4.get_price())
    print("\t[5] ", product5.get_name(), "         ..........  ₱", product5.get_price())
    print("\t[6] ", product6.get_name(), "       ..........  ₱", product6.get_price())
    print("\t[7] ", product7.get_name(), " ..........  ₱", product7.get_price())
    print("\t[8] ", product8.get_name(), "   ..........  ₱", product8.get_price())
    print("\t[9] ", product9.get_name(), "       ..........  ₱", product9.get_price())


    order()          # Call the order function to get the order of the user





# FUNCTION TO TAKE THE ORDER OF THE USER AND DISPLAY THEM
def order():
    print("\n\n----------")
    order_product = input("Enter your orders:  ")

    order_product = order_product.split()

    for i in range(len(order_product)):
        order_product[i] = int(order_product[i])         # Convert each item to int type
    print('list: ', order_product)


    print("You ordered the following foods:")
    print("\t" )


if __name__ == "__main__":
    main()
