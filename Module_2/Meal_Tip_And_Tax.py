user_input = input("Enter charge for the food: ")

# Check empty value
if user_input.strip() == "":
    print("Error: Input cannot be empty.")
else:
    # Check characters value
    if any(char.isalpha() for char in user_input):
        print("Error: No letters allowed. Enter numbers only.")
    else:
        user_charge = float(user_input)

        # Check negative value
        if user_charge < 0:
            print("Error: Charge cannot be negative.")
        else:
            tip_percent = 0.18
            tax_sales_percent = 0.07

            tip = user_charge * tip_percent
            tax = user_charge * tax_sales_percent
            total = user_charge + tax + tip

            print('--------------------------------')
            print(f'             SUBTOTAL: ${user_charge:.2f}')
            print(f'             TAX: ${tax:.2f}')
            print(f'             GRATUITY: ${tip:.2f}')
            print('--------------------------------')
            print(f'             TOTAL DUE: ${total:.2f}')
            print('--------------------------------')
            print(' THANK YOU FOR DINING WITH US ! ')
            print('      PLEASE COME AGAIN         ')
