# # # from auth import AuthSystem
# # # from product import Product
# # # from inventory import Inventory

# # # # Your main code goes here
# # # if __name__ == "__main__":
# # #     print("Inventory Management System")
# # #     # Initialize auth system and inventory
# # #     auth_system = AuthSystem()
# # #     inventory = Inventory()
# # #     # Your main program logic...



# # from auth import AuthSystem
# # from product import Product
# # from inventory import Inventory

# # def main():
# #     print("Welcome to the Inventory Management System!")
    
# #     # Initialize auth system and inventory
# #     auth_system = AuthSystem()
# #     inventory = Inventory()

# #     # Add some products to the inventory
# #     inventory.add_product(Product(1, "Laptop", "Electronics", 1000, 10))
# #     inventory.add_product(Product(2, "Phone", "Electronics", 500, 20))

# #     # Ask for user login
# #     username = input("Enter username: ")
# #     password = input("Enter password: ")

# #     # Authenticate user
# #     user = auth_system.login(username, password)
# #     if user is None:
# #         print("Login failed!")
# #         return
    
# #     print(f"Logged in as {user.username} with role {user.role}")

# #     # Display inventory options based on user role
# #     if user.role == "Admin":
# #         print("Welcome, Admin! You can manage products.")
# #         print("1. View Inventory")
# #         print("2. Add Product")
# #         print("3. Edit Product")
# #         print("4. Delete Product")
        
# #         choice = input("Choose an option (1-4): ")
        
# #         if choice == '1':
# #             inventory.view_products()
# #         elif choice == '2':
# #             product_id = int(input("Enter product ID: "))
# #             name = input("Enter product name: ")
# #             category = input("Enter product category: ")
# #             price = float(input("Enter product price: "))
# #             stock = int(input("Enter product stock quantity: "))
# #             inventory.add_product(Product(product_id, name, category, price, stock))
# #             print(f"Product {name} added!")
# #         # Implement options 3 and 4 here (Edit, Delete)
    
# #     elif user.role == "User":
# #         print("Welcome, User! You can only view the inventory.")
# #         inventory.view_products()

# # if __name__ == "__main__":
# #     main()

# class User:
#     def __init__(self, username, password, role):
#         self.username = username
#         self.password = password
#         self.role = role  # Either 'Admin' or 'User'

# class AuthSystem:
#     def __init__(self):
#         # Add your test credentials here
#         self.users = {
#             "admin": User("admin", "admin123", "Admin"),
#             "user": User("user", "user123", "User"),
#             "mujahid": User("mujahid", "12345", "User")  # Add 'mujahid' user
#         }

#     def login(self, username, password):
#         user = self.users.get(username)
#         if user and user.password == password:
#             print(f"Welcome, {username}!")
#             return user
#         else:
#             print("Invalid username or password.")
#             return None

# class Product:
#     def __init__(self, product_id, name, category, price, stock_quantity):
#         self.product_id = product_id
#         self.name = name
#         self.category = category
#         self.price = price
#         self.stock_quantity = stock_quantity

# class Inventory:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def view_products(self):
#         if not self.products:
#             print("No products in inventory.")
#         else:
#             print("Inventory:")
#             for product in self.products:
#                 print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Stock: {product.stock_quantity}")

# def main():
#     print("Welcome to the Inventory Management System!")
    
#     # Initialize auth system and inventory
#     auth_system = AuthSystem()
#     inventory = Inventory()

#     # Add some products to the inventory
#     inventory.add_product(Product(1, "Laptop", "Electronics", 1000, 10))
#     inventory.add_product(Product(2, "Phone", "Electronics", 500, 20))

#     # Ask for user login
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     # Authenticate user
#     user = auth_system.login(username, password)
#     if user is None:
#         print("Login failed!")
#         return
    
#     print(f"Logged in as {user.username} with role {user.role}")

#     # Display inventory options based on user role
#     if user.role == "Admin":
#         print("Welcome, Admin! You can manage products.")
#         print("1. View Inventory")
#         print("2. Add Product")
#         print("3. Edit Product")
#         print("4. Delete Product")
        
#         choice = input("Choose an option (1-4): ")
        
#         if choice == '1':
#             inventory.view_products()
#         elif choice == '2':
#             product_id = int(input("Enter product ID: "))
#             name = input("Enter product name: ")
#             category = input("Enter product category: ")
#             price = float(input("Enter product price: "))
            
#             # Handle stock quantity input with validation
#             while True:
#                 try:
#                     stock = int(input("Enter product stock quantity: "))
#                     break  # Exit loop if input is valid
#                 except ValueError:
#                     print("Invalid input for stock quantity. Please enter a valid integer.")
            
#             inventory.add_product(Product(product_id, name, category, price, stock))
#             print(f"Product {name} added!")
#         # Implement options 3 and 4 here (Edit, Delete)
    
#     elif user.role == "User":
#         print("Welcome, User! You can only view the inventory.")
#         inventory.view_products()

# if __name__ == "__main__":
#     main()

















class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # Role is either 'Admin' or 'User'


class AuthSystem:
    def __init__(self):
        # Predefined users for login
        self.users = {
            "admin": User("admin", "admin123", "Admin"),
            "user": User("user", "user123", "User"),
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            print(f"Welcome, {username}!")
            return user
        else:
            print("Invalid username or password.")
            return None


class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Product {product.name} added successfully!")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} deleted successfully!")
        else:
            print(f"Product with ID {product_id} not found.")

    def edit_product(self, product_id):
        if product_id in self.products:
            product = self.products[product_id]
            print(f"Editing product {product.name} (ID: {product_id})")
            product.name = input(f"Enter new name (current: {product.name}): ") or product.name
            product.category = input(f"Enter new category (current: {product.category}): ") or product.category
            product.price = float(input(f"Enter new price (current: {product.price}): ") or product.price)
            
            while True:
                try:
                    product.stock_quantity = int(input(f"Enter new stock quantity (current: {product.stock_quantity}): ") or product.stock_quantity)
                    break
                except ValueError:
                    print("Invalid input for stock quantity. Please enter a valid integer.")
            print(f"Product {product_id} updated successfully!")
        else:
            print("Product not found.")

    def view_inventory(self):
        if self.products:
            print("Inventory:")
            for product in self.products.values():
                print(product)
        else:
            print("No products in inventory.")

    def search_by_name(self, name):
        results = [product for product in self.products.values() if name.lower() in product.name.lower()]
        if results:
            for product in results:
                print(product)
        else:
            print("No products found with that name.")

    def filter_by_stock(self, min_stock):
        filtered_products = [product for product in self.products.values() if product.stock_quantity >= min_stock]
        if filtered_products:
            for product in filtered_products:
                print(product)
        else:
            print(f"No products found with stock greater than or equal to {min_stock}.")

    def alert_low_stock(self, threshold):
        for product in self.products.values():
            if product.stock_quantity <= threshold:
                print(f"Alert: {product.name} has low stock! Only {product.stock_quantity} left.")


def main():
    print("Welcome to the Inventory Management System!")

    # Initialize auth system and inventory
    auth_system = AuthSystem()
    inventory = Inventory()

    # Preload some sample products
    inventory.add_product(Product(1, "Laptop", "Electronics", 1000, 10))
    inventory.add_product(Product(2, "Phone", "Electronics", 500, 5))
    inventory.add_product(Product(3, "Shirt", "Clothing", 20, 50))

    # User login
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = auth_system.login(username, password)
    if not user:
        print("Login failed!")
        return
    
    print(f"Logged in as {username} with role {user.role}")

    # Main loop based on role
    if user.role == "Admin":
        while True:
            print("\nAdmin Menu:")
            print("1. View Inventory")
            print("2. Add Product")
            print("3. Edit Product")
            print("4. Delete Product")
            print("5. Search Product by Name")
            print("6. Filter by Stock")
            print("7. Alert for Low Stock")
            print("8. Logout")

            choice = input("Choose an option (1-8): ")
            if choice == '1':
                inventory.view_inventory()
            elif choice == '2':
                try:
                    product_id = int(input("Enter product ID: "))
                    name = input("Enter product name: ")
                    category = input("Enter product category: ")
                    price = float(input("Enter product price: "))
                    stock_quantity = int(input("Enter product stock quantity: "))
                    inventory.add_product(Product(product_id, name, category, price, stock_quantity))
                except ValueError:
                    print("Invalid input for price or stock quantity.")
            elif choice == '3':
                try:
                    product_id = int(input("Enter product ID to edit: "))
                    inventory.edit_product(product_id)
                except ValueError:
                    print("Invalid input.")
            elif choice == '4':
                try:
                    product_id = int(input("Enter product ID to delete: "))
                    inventory.delete_product(product_id)
                except ValueError:
                    print("Invalid input.")
            elif choice == '5':
                name = input("Enter product name to search: ")
                inventory.search_by_name(name)
            elif choice == '6':
                try:
                    min_stock = int(input("Enter minimum stock level: "))
                    inventory.filter_by_stock(min_stock)
                except ValueError:
                    print("Invalid input.")
            elif choice == '7':
                try:
                    threshold = int(input("Enter low stock threshold: "))
                    inventory.alert_low_stock(threshold)
                except ValueError:
                    print("Invalid input.")
            elif choice == '8':
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")
    
    elif user.role == "User":
        while True:
            print("\nUser Menu:")
            print("1. View Inventory")
            print("2. Logout")

            choice = input("Choose an option (1-2): ")
            if choice == '1':
                inventory.view_inventory()
            elif choice == '2':
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
