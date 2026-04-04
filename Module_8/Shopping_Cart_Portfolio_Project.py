from datetime import datetime

class Utility:
    """Utility class for common helper methods."""

    @staticmethod
    def print_line():
        print("-" * 40)

    @staticmethod
    def get_non_empty_string(prompt):
        while True:
            try:
                value = input(prompt).strip()
                if not value:
                    raise ValueError("Input cannot be empty.")
                return value
            except ValueError as e:
                print(f"Error: {e}")

    @staticmethod
    def get_valid_int(prompt, allow_zero=True):
        while True:
            try:
                value = int(input(prompt).strip())
                if not allow_zero and value <= 0:
                    raise ValueError("Value must be greater than 0.")
                if allow_zero and value < 0:
                    raise ValueError("Value cannot be negative.")
                return value
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid integer.")

    @staticmethod
    def get_valid_float(prompt, allow_zero=True):
        while True:
            try:
                value = float(input(prompt).strip())
                if not allow_zero and value <= 0:
                    raise ValueError("Value must be greater than 0.")
                if allow_zero and value < 0:
                    raise ValueError("Value cannot be negative.")
                return value
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid number.")

    @staticmethod
    def get_valid_date(prompt):
        while True:
            user_input = input(prompt)
            try:
                # user input parse karo (expected: MM/DD/YYYY)
                date_obj = datetime.strptime(user_input, "%m/%d/%Y")

                # format karo: April 3, 2026
                formatted_date = date_obj.strftime("%B ") + str(date_obj.day) + date_obj.strftime(", %Y")

                return formatted_date

            except ValueError:
                print("Invalid date format. Please enter date as MM/DD/YYYY")

    @staticmethod
    def pause():
        input("\nPress Enter to continue...")


class ItemToPurchase:
    """Represents a single item in the shopping cart."""

    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.__item_name = item_name
        self.__item_description = item_description
        self.__item_price = item_price
        self.__item_quantity = item_quantity

    # Properties for encapsulation
    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, value):
        if not value.strip():
            raise ValueError("Item name cannot be empty.")
        self.__item_name = value.strip()

    @property
    def item_description(self):
        return self.__item_description

    @item_description.setter
    def item_description(self, value):
        if not value.strip():
            raise ValueError("Item description cannot be empty.")
        self.__item_description = value.strip()

    @property
    def item_price(self):
        return self.__item_price

    @item_price.setter
    def item_price(self, value):
        if value < 0:
            raise ValueError("Item price cannot be negative.")
        self.__item_price = value

    @property
    def item_quantity(self):
        return self.__item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        if value < 0:
            raise ValueError("Item quantity cannot be negative.")
        self.__item_quantity = value

    def print_item_cost(self):
        total_cost = self.__item_price * self.__item_quantity
        # to avoid 3.0 showing if number is whole
        if self.__item_price == int(self.__item_price):
            price_display = int(self.__item_price)
        else:
            price_display = self.__item_price

        if total_cost == int(total_cost):
            total_display = int(total_cost)
        else:
            total_display = total_cost

        print(f"{self.__item_name} {self.__item_quantity} @ ${price_display} = ${total_display}")

    def print_item_description(self):
        print(f"{self.__item_name}: {self.__item_description}")

    @classmethod
    def create_item_from_user(cls):
        """Class method to create an item object from user input."""
        print("ADD ITEM TO CART")
        item_name = Utility.get_non_empty_string("Enter the item name:\n")
        item_description = Utility.get_non_empty_string("Enter the item description:\n")
        item_price = Utility.get_valid_float("Enter the item price:\n")
        item_quantity = Utility.get_valid_int("Enter the item quantity:\n")
        return cls(item_name, item_description, item_price, item_quantity)


class ShoppingCart:
    """Represents the shopping cart."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        if isinstance(item_to_purchase, ItemToPurchase):
            self.cart_items.append(item_to_purchase)
        else:
            raise TypeError("Only ItemToPurchase objects can be added to cart.")

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name.lower() == item_to_purchase.item_name.lower():
                # Only update quantity if provided
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        total = self.get_cost_of_cart()
        if total == int(total):
            total = int(total)
        print(f"\nTotal: ${total}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")


def execute_menu(choice, shopping_cart):
    if choice == 'a':
        print()
        item = ItemToPurchase.create_item_from_user()
        shopping_cart.add_item(item)

    elif choice == 'r':
        print("\nREMOVE ITEM FROM CART")
        item_name = Utility.get_non_empty_string("Enter name of item to remove:\n")
        shopping_cart.remove_item(item_name)

    elif choice == 'c':
        print("\nCHANGE ITEM QUANTITY")
        item_name = Utility.get_non_empty_string("Enter the item name:\n")
        new_quantity = Utility.get_valid_int("Enter the new quantity:\n")

        modified_item = ItemToPurchase(item_name=item_name, item_quantity=new_quantity)
        shopping_cart.modify_item(modified_item)

    elif choice == 'i':
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        shopping_cart.print_descriptions()

    elif choice == 'o':
        print("\nOUTPUT SHOPPING CART")
        shopping_cart.print_total()

    elif choice == 'q':
        print("\nExiting shopping cart program...")

    else:
        print("Invalid option. Please try again.")


def milestone1_demo():
    """Optional demo for milestone 1 style 2-item input."""
    print("Item 1")
    item1_name = Utility.get_non_empty_string("Enter the item name:\n")
    item1_price = Utility.get_valid_float("Enter the item price:\n")
    item1_quantity = Utility.get_valid_int("Enter the item quantity:\n")

    print("\nItem 2")
    item2_name = Utility.get_non_empty_string("Enter the item name:\n")
    item2_price = Utility.get_valid_float("Enter the item price:\n")
    item2_quantity = Utility.get_valid_int("Enter the item quantity:\n")

    item1 = ItemToPurchase(item1_name, "none", item1_price, item1_quantity)
    item2 = ItemToPurchase(item2_name, "none", item2_price, item2_quantity)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    if total == int(total):
        total = int(total)
    print(f"Total: ${total}")


def main():
    try:
        milestone1_demo()

        print("Enter customer's name:")
        customer_name = Utility.get_non_empty_string("")

        print("Enter today's date:")
        current_date = Utility.get_valid_date("")

        print(f"\nCustomer name: {customer_name}")
        print(f"Today's date: {current_date}")

        cart = ShoppingCart(customer_name, current_date)

        choice = ""
        while choice != 'q':
            print_menu()
            choice = input("Choose an option:\n").strip().lower()
            while choice not in ['a', 'r', 'c', 'i', 'o', 'q']:
                print("Invalid option. Please try again.")
                choice = input("Choose an option:\n").strip().lower()

            execute_menu(choice, cart)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
