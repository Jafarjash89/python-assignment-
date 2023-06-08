class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, Contact):
        self.contacts.append(Contact)
        print("Contact added successfully.")

    def remove_contact(self, Contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            print("Contact removed successfully.")
        else:
            print("Contact not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Contact found:")
                print(f"Name: {contact.name}")
                print(f"Phone number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print("Contact not found.")

    def display_contacts(self):
        if len(self.contacts) == 0:
            print("Contact book is empty.")
        else:
            print("Contact book:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("--------------")

def menu():
    print("Contact Book Menu")
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Search for a contact")
    print("4. Display all contacts")
    print("5. Quit")

contact_book = ContactBook()

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact = Contact(name, phone_number, email)
        contact_book.add_contact(contact)

    elif choice == '2':
        name = input("Enter contact name to remove: ")
        contact_book.search_contact(name)
        contact_book.remove_contact(Contact)

    elif choice == '3':
        name = input("Enter contact name to search: ")
        contact_book.search_contact(name)

    elif choice == '4':
        contact_book.display_contacts()

    elif choice == '5':
        print("Thank you for using the Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")
