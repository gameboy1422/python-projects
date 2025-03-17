class Supermarket:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, quantity):
        if product_id in self.products:
            print("Product ID already exists!")
        else:
            self.products[product_id] = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            print(f"Product '{name}' added successfully!")

    def update_product(self, product_id, name=None, price=None, quantity=None):
        if product_id in self.products:
            if name:
                self.products[product_id]["name"] = name
            if price:
                self.products[product_id]["price"] = price
            if quantity:
                self.products[product_id]["quantity"] = quantity
            print(f"Product ID {product_id} updated successfully!")
        else:
            print("Product ID not found!")

    def view_products(self):
        if not self.products:
            print("No products available!")
        else:
            print("\n--- Product List ---")
            for product_id, details in self.products.items():
                print(f"ID: {product_id}, Name: {details['name']}, Price: ${details['price']}, Quantity: {details['quantity']}")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product ID {product_id} deleted successfully!")
        else:
            print("Product ID not found!")

def main():
    supermarket = Supermarket()
    while True:
        print("\n--- Supermarket Management System ---")
        print("1. Add Product")
        print("2. Update Product")
        print("3. View Products")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            supermarket.add_product(product_id, name, price, quantity)

        elif choice == "2":
            product_id = input("Enter Product ID to update: ")
            name = input("Enter new Name (leave blank to skip): ")
            price = input("Enter new Price (leave blank to skip): ")
            quantity = input("Enter new Quantity (leave blank to skip): ")
            supermarket.update_product(
                product_id,
                name if name else None,
                float(price) if price else None,
                int(quantity) if quantity else None
            )

        elif choice == "3":
            supermarket.view_products()

        elif choice == "4":
            product_id = input("Enter Product ID to delete: ")
            supermarket.delete_product(product_id)

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()