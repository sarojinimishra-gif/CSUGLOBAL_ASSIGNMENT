# Utility Functions (Reusability)
def get_valid_string(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("Input cannot be empty. Try again.")
        else:
            return value

def get_valid_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a number.")

def format_number(num):
    if num.is_integer():
        return str(int(num))
    else:
        return f"{num:.2f}"

# Class: ItemToPurchase
class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity

        print(f"{self.item_name} {self.item_quantity} @ ${format_number(self.item_price)} = ${format_number(total_cost)}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

# Class: ShoppingCart
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        item_found = False

        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():
                self.cart_items.remove(item)
                item_found = True
                break

        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        item_found = False

        for item in self.cart_items:
            if item.item_name.lower() == ItemToPurchase.item_name.lower():
                item_found = True

                if ItemToPurchase.item_description != "none":
                    item.item_description = ItemToPurchase.item_description

                if ItemToPurchase.item_price != 0:
                    item.item_price = ItemToPurchase.item_price

                if ItemToPurchase.item_quantity != 0:
                    item.item_quantity = ItemToPurchase.item_quantity

                break

        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        total = self.get_cost_of_cart()

        print()
        print(f"Total: ${format_number(total)}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    choice = ' '

    while choice != 'q':
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        choice = input("Choose an option:\n").lower()

        while choice not in ['a', 'r', 'c', 'i', 'o', 'q']:
            print("Invalid option. Try again.")
            choice = input("Choose an option:\n").lower()

        if choice == 'a':
            print("ADD ITEM TO CART")
            item = ItemToPurchase()
            item.item_name = get_valid_string("Enter the item name:\n")
            item.item_description = get_valid_string("Enter the item description:\n")
            item.item_price = get_valid_number("Enter item price:\n")
            item.item_quantity = int(get_valid_number("Enter item quantity:\n"))
            ''' 
            If user want to edit description and price.
            print("Enter new description or press enter to skip:")
            new_description = input()
            if new_description.strip() != "":
                item.item_description = new_description

            print("Enter new price or press enter to skip:")
            new_price = get_valid_number()
            if new_price.strip() != "":
                item.item_price = new_price
            '''
            print()

            cart.add_item(item)

        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = get_valid_string("Enter name of item to remove:\n")
            print()

            cart.remove_item(item_name)

        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item = ItemToPurchase()
            item.item_name = get_valid_string("Enter the item name:\n")
            item.item_quantity = int(get_valid_number("Enter new quantity:\n"))
            print()

            cart.modify_item(item)

        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            print()

        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
            print()


def main():
    # Milestone Part 1
    '''
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = get_valid_string("Enter the item name:\n")
    item1.item_price = get_valid_number("Enter item price:\n")
    item1.item_quantity = int(get_valid_number("Enter item quantity:\n"))
    print()

    print("Item 2")
    item2 = ItemToPurchase()
    item2.item_name = get_valid_string("Enter the item name:\n")
    item2.item_price = get_valid_number("Enter item price:\n")
    item2.item_quantity = int(get_valid_number("Enter item quantity:\n"))
    print()

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print()
    print(f"Total: ${format_number(total)}")
    print()
    '''

    # Milestone Part 2
    customer_name = get_valid_string("Enter customer's name:\n")
    current_date = get_valid_string("Enter today's date:\n")
    print()

    print("Customer name:", customer_name)
    print("Today's date:", current_date)
    print()

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
