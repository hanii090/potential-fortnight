# Define a class for the vending machine
class VendingMachine:
    # Initialize the vending machine with products and balance
    def _init_(self):
        # Dictionary to store product information
        self.products = {
            "1": {"name": "Soda", "price": 1.50, "quantity": 10},
            "2": {"name": "Chips", "price": 1.00, "quantity": 8},
            "3": {"name": "Chocolate", "price": 0.75, "quantity": 15},
        }
        self.balance = 0.0

    # Display available products and their details
    def display_products(self):
        print("\nAvailable Products:")
        for code, product in self.products.items():
            print(f"{code}: {product['name']} - ${product['price']} - {product['quantity']} left")

    # Insert money into the vending machine
    def insert_money(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance:.2f}")

    # Purchase a product using the provided code
    def purchase_product(self, code):
        if code in self.products:
            product = self.products[code]
            if product["quantity"] > 0 and self.balance >= product["price"]:
                self.balance -= product["price"]
                product["quantity"] -= 1
                print(f"Enjoy your {product['name']}!")
                print(f"Remaining balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance or product out of stock.")
        else:
            print("Invalid product code.")

    # Return change to the user
    def return_change(self):
        change = self.balance
        self.balance = 0
        print(f"Change returned: ${change:.2f}")

    # Start the vending machine simulation
    def start(self):
        while True:
            print("\nWelcome to the Vending Machine!")
            self.display_products()
            print("Enter 'q' to quit.")
            
            # Get user input for product selection
            choice = input("Select a product by entering its code: ")
            if choice == "q":
                self.return_change()
                break
            elif choice.isdigit():
                self.purchase_product(choice)
            else:
                print("Invalid input. Please enter a valid code or 'q' to quit.")


# Entry point of the program
if _name_ == "_main_":
    # Create an instance of the vending machine class
    vending_machine = VendingMachine()
    # Start the vending machine simulation
    vending_machine.start()