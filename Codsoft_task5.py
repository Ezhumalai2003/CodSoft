import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts = load_contacts()
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    save_contacts(contacts)

    print("\nContact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")

# Search for a contact
def search_contact():
    query = input("Enter Name or Phone Number to search: ").lower()
    contacts = load_contacts()
    found_contacts = [c for c in contacts if query in c["Name"].lower() or query in c["Phone"]]

    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n")
    else:
        print("\nNo matching contacts found.")

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            print("\nEnter new details (leave blank to keep the same):")
            contact["Phone"] = input(f"New Phone ({contact['Phone']}): ") or contact["Phone"]
            contact["Email"] = input(f"New Email ({contact['Email']}): ") or contact["Email"]
            contact["Address"] = input(f"New Address ({contact['Address']}): ") or contact["Address"]

            save_contacts(contacts)
            print("\nContact updated successfully!")
            return
    
    print("\nContact not found.")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    
    contacts = [contact for contact in contacts if contact["Name"].lower() != name.lower()]
    save_contacts(contacts)

    print("\nContact deleted successfully!" if len(contacts) < len(load_contacts()) else "\nContact not found.")

# Main menu
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
