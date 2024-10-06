
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

def add_product(inventory):
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    inventory[product_id] = Product(product_id, name, price, quantity)
    
def update_stock(inventory):
    product_id = input("Enter product ID: ")
    if product_id in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[product_id].set_quantity(new_quantity)
    else:
        print("Product not found.")

def process_sale(inventory):
    product_id = input("Enter product ID for sale: ")
    quantity_sold = int(input("Enter quantity sold: "))
    if product_id in inventory and inventory[product_id].get_quantity() >= quantity_sold:
        product = inventory[product_id]
        product.set_quantity(product.get_quantity() - quantity_sold)
        total_price = quantity_sold * product.get_price()
        print(f"Receipt: {quantity_sold} of {product.get_name()} for ${total_price}")
    else:
        print("Product not found or insufficient quantity")

def main():
    inventory = []
    while True:
        print("\n1. Add Product\n2. Update Stock\n3. Process Sale\n4. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                add_product(inventory)
            elif choice == "2":
                update_stock(inventory)
            elif choice == "3":
                process_sale(inventory)
            elif choice == "4":
                break
            else: print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()