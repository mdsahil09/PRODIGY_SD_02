import json

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact added: {contact.name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

    def edit_contact(self):
        self.view_contacts()
        if not self.contacts:
            return

        try:
            index = int(input("Enter the index of the contact you want to edit: ")) - 1
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                print(f"\nEditing contact: {contact.name}")
                contact.name = input("Enter new name: ")
                contact.phone_number = input("Enter new phone number: ")
                contact.email = input("Enter new email address: ")
                print("Contact updated successfully.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

    def delete_contact(self):
        self.view_contacts()
        if not self.contacts:
            return

        try:
            index = int(input("Enter the index of the contact you want to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                deleted_contact = self.contacts.pop(index)
                print(f"\nContact deleted: {deleted_contact.name}")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

    def save_contacts_to_file(self, filename):
        with open(filename, 'w') as file:
            contacts_data = [{'name': contact.name, 'phone_number': contact.phone_number, 'email': contact.email}
                             for contact in self.contacts]
            json.dump(contacts_data, file)
            print(f"Contacts saved to {filename}")

    def load_contacts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                self.contacts = [Contact(contact['name'], contact['phone_number'], contact['email'])
                                 for contact in contacts_data]
                print(f"Contacts loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty contact list.")

def contact_management():
    contact_manager = ContactManager()
    file_name = "contacts.json"  # Change the filename as needed

    # Load contacts from file if available
    contact_manager.load_contacts_from_file(file_name)

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            new_contact = Contact(name, phone_number, email)
            contact_manager.add_contact(new_contact)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.edit_contact()
        elif choice == "4":
            contact_manager.delete_contact()
        elif choice == "5":
            contact_manager.save_contacts_to_file(file_name)
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_management()
