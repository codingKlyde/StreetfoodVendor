class Product:
    def __init__(self, product_name, product_type, product_price):
        self._product_name = product_name
        self._product_type = product_type
        self._product_price = product_price



    # GETTER METHODS
    def get_name(self):
        return self._product_name
    def get_type(self):
        return self._product_type
    def get_price(self):
        return self._product_price



    # SETTER METHODS
    def set_name(self, product_name):
        self._product_name = product_name
    def set_name(self, product_type):
        self._product_type = product_type
    def set_name(self, product_price):
        self._product_price = product_price





def main():
    print("AVAILABLE TODAY:")
    print("\t[1] ")
    print("\t[2] ")
    print("\t[3] ")
    print("\t[4] ")
    print("\t[5] ")
    print("\t[6] ")


if __name__ == "__main__":
    main()
