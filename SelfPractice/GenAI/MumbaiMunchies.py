class Snack:
    def __init__(self, id, name, price, available):
        self.id = id
        self.name = name
        self.price = price
        self.available = available

class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, id, name, price, available):
        snack = Snack(id, name, price, available)
        self.inventory.append(snack)
        print(f"Snack added: {name}")

    def remove_snack(self, id):
        snack = next((snack for snack in self.inventory if snack.id == id), None)
        if snack:
            self.inventory.remove(snack)
            print(f"Snack removed: {snack.name}")
        else:
            print("Snack not found.")

    def update_availability(self, id, availability):
        snack = next((snack for snack in self.inventory if snack.id == id), None)
        if snack:
            snack.available = availability
            print(f"Availability updated for snack: {snack.name}")
        else:
            print("Snack not found.")

    def record_sale(self, id):
        snack = next((snack for snack in self.inventory if snack.id == id), None)
        if snack:
            if snack.available:
                self.sales_records.append(snack)
                print(f"Sale recorded for snack: {snack.name}")
            else:
                print("Snack is unavailable.")
        else:
            print("Snack not found.")

    def display_inventory(self):
        print("Snack Inventory:")
        for snack in self.inventory:
            print(f"ID: {snack.id}, Name: {snack.name}, Price: {snack.price}, Available: {snack.available}")

    def display_sales(self):
        print("Sales Records:")
        for snack in self.sales_records:
            print(f"Sold: {snack.name}, Price: {snack.price}")

# Main Program
canteen = Canteen()

while True:
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Availability")
    print("4. Record Sale")
    print("5. Display Inventory")
    print("6. Display Sales")
    print("7. Exit")
    option = int(input("Choose an option: "))

    if option == 1:
        id = input("Enter Snack ID: ")
        name = input("Enter Snack Name: ")
        price = float(input("Enter Snack Price: "))
        available = input("Is Snack Available (yes/no): ").strip().lower() == 'yes'
        canteen.add_snack(id, name, price, available)
    elif option == 2:
        id = input("Enter Snack ID to remove: ")
        canteen.remove_snack(id)
    elif option == 3:
        id = input("Enter Snack ID to update availability: ")
        available = input("Is Snack Available (yes/no): ").strip().lower() == 'yes'
        canteen.update_availability(id, available)
    elif option == 4:
        id = input("Enter Snack ID to record sale: ")
        canteen.record_sale(id)
    elif option == 5:
        canteen.display_inventory()
    elif option == 6:
        canteen.display_sales()
    elif option == 7:
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")
