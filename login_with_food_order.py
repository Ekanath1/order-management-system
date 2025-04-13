import json
import os


class FoodOrderingSystem:
    def __init__(self):
        self.users_file = "users.json"
        self.orders_file = "orders.json"
        self.users = self.load_data(self.users_file)
        self.orders = self.load_data(self.orders_file)
        self.logged_in_user = None
        self.cart = []
        self.foods = [
            {"Burger": 120},
            {"Vegetable Pups": 50},
            {"Chinese Food": 100},
            {"Egg Pups": 50}
        ]

    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def display_menu(self):
        print("\n--- Menu ---")
        for item in self.foods:
            for food, price in item.items():
                print(f"{food} --> {price}")
        print("------------")

    def register(self):
        username = input("Create a username: ")
        if username in self.users:
            print("Username already exists.")
            return self.register()
        password = input("Create a password: ")
        self.users[username] = password
        self.orders[username] = []
        self.save_data(self.users_file, self.users)
        self.save_data(self.orders_file, self.orders)
        print("Registration successful!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.users.get(username) == password:
            self.logged_in_user = username
            print(f"Welcome, {username}!")
        else:
            print("Invalid credentials.")
            return self.login()

    def add_items(self):
        self.cart = []
        self.display_menu()
        while True:
            itm = input("Which food would you like to add? ").title()
            found = False
            for food in self.foods:
                if itm in food:
                    self.cart.append(food)
                    print(f"{itm} added to cart.")
                    found = True
                    break
            if not found:
                print(f"{itm} is not available.")

            inp = input("Do you want to add more food? (yes/no): ").strip().lower()
            if inp == 'no':
                break

    def display_bill(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\n--- Bill ---")
        total_price = 0
        for item in self.cart:
            for food, price in item.items():
                print(f"{food}: ₹{price}")
                total_price += price
        print(f"Total Amount: ₹{total_price}")
        print("------------")

        # Save order to user's history
        if self.logged_in_user:
            self.orders[self.logged_in_user].append({
                "items": self.cart.copy(),
                "total": total_price
            })
            self.save_data(self.orders_file, self.orders)

    def view_order_history(self):
        if self.logged_in_user and self.orders.get(self.logged_in_user):
            print(f"\nOrder history for {self.logged_in_user}: ")
            for idx, order in enumerate(self.orders[self.logged_in_user], start=1):
                print(f"\nOrder #{idx}: ")
                for item in order["items"]:
                    for food, price in item.items():
                        print(f"  {food}: ₹{price}")
                print(f"  Total: ₹{order['total']}")
        else:
            print("No past orders found.")

    def delete_item_from_menu(self):
        item1 = input("Enter the name of the item to delete from menu: ").title()
        for food in self.foods:
            if item1 in food:
                self.foods.remove(food)
                print(f"{item1} has been removed from the menu.")
                return
        print("Item not found in the menu.")

    def start(self):
        print("Welcome to the Food Ordering System")
        while True:
            action = input("Do you want to Register or Login? (r/l): ").lower()
            if action == 'r':
                self.register()
                self.login()
                break
            elif action == 'l':
                self.login()
                break
            else:
                print("Invalid option.")

        while True:
            print("\n1. View Menu\n2. Add Items\n3. View Bill\n4. Order History\n5. Delete Item From Menu\n6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.add_items()
            elif choice == '3':
                self.display_bill()
            elif choice == '4':
                self.view_order_history()
            elif choice == '5':
                self.delete_item_from_menu()
            elif choice == '6':
                print("Thank you! Come again.")
                break
            else:
                print("Invalid choice.")


# Start the system
food_ordering_system = FoodOrderingSystem()
food_ordering_system.start()
