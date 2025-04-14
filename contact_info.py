
class ContactInfo:
    def __init__(self):
        self.contact = [
            {"Govinda_B": 8951171629},
            {"Eknath_B": 9731213720},
            {"Ramesh_Kumar": 9030998811},
            {"Swati_Reddy": 8922001244},
            {"Root": 4000332899},
            {'Mark': 5003322119}
        ]

    def search_contact(self, name):
        for cont in self.contact:
            if name in cont:
                return [name, cont[name]]
        return []

    def delete_contact(self, name):
        for cont in self.contact:
            if name in cont:
                self.contact.remove(cont)
                return 'Contact removed'
        return 'No info found'

    def add_info(self, info):
        self.contact.append({info[0]: int(info[1])})
        return 'Contact added'

    def update_info(self, upd):
        for cont in self.contact:
            if upd[0] in cont:
                cont[upd[0]] = int(upd[1])
                return 'Record updated'
        return 'Contact not present'


# Create object outside loop so it retains data
obj = ContactInfo()

while True:
    print("\n--- Contact Info Menu ---")
    print("1. Search Contact")
    print("2. Delete Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    try:
        inp = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if inp == 1:
        search = input("Enter name to search: ").title()
        result = obj.search_contact(search)
        print(result if result else "Contact not found.")
    elif inp == 2:
        delete = input("Enter name to delete: ").title()
        print(obj.delete_contact(delete))
    elif inp == 3:
        add = input("Enter name and number (e.g., John 9876543210): ").split()
        if len(add) == 2:
            if len(add[1]) == 10:
                print(obj.add_info(add))
            else:
                print("mobile number should be ten digit ")
        else:
            print("Invalid input format.")
    elif inp == 4:
        update = input("Enter name and new number (e.g., John 1234567890): ").split()
        if len(update) == 2:
            if len(update[1]) == 10:
                print(obj.update_info(update))
            else:
                print("mobile number should be ten digit  ")
        else:
            print("Invalid input format.")
    elif inp == 5:
        print("\nContacts:")
        for contact in obj.contact:
            for name, number in contact.items():
                print(f"{name}: {number}")
    elif inp == 6:
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")