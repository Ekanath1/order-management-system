
class FoodOrderingSystem:
    def __init__(self):
        self.cart = []
        self.foods = [
            {"Burger": 120},
            {"Vegetable Pups": 50},
            {"Chinese Food": 100},
            {"Egg Pups": 50}
        ]
        self.display_menu()

    def display_menu(self):
        print("\n--- Menu ---")
        for item in self.foods:
            for food, price in item.items():
                print(f"{food} --> {price}")
        print("------------")


    def add_items(self):
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
                print(f" {itm} is not available.")

            inp = input("Do you want to add more food? (yes/no): ").strip().lower()
            if inp == 'no':
                break

    def display_bill(self):
        if not self.cart:
            print(" Your cart is empty.")
            return

        print("\n--- Bill ---")
        total_price = 0
        for item in self.cart:
            for food, price in item.items():
                print(f"{food}: {price}")
                total_price += price
        print(f"Total Amount: {total_price}")
        print("------------")

    def delete_item(self):
        item1 = input("Enter the name of the item you want to delete from menu: ").title()
        for food in self.foods:
            if item1 in food:
                self.foods.remove(food)
                print(f" {item1} has been removed from the menu.")
                return
        print("Item not found in the menu.")


# Usage
food_ordering_system = FoodOrderingSystem()
food_ordering_system.add_items()
food_ordering_system.display_bill()
food_ordering_system.delete_item()
