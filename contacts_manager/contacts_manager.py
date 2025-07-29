print("Welcome to Ana's Contact Manager!")

action = input("What would you like to do? (A)dd, (V)iew, (Q)uit: ").lower()
contacts = []
if action == "a":
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added successfully!")
elif action == "v":
    print("Your Contacts:")
    for contact in contacts:
        print(f"[{contact['name']}] - {contact['phone']}")
elif action == "q":
    print("Goodbye!")
else:
    print("Invalid option. Please try A, V, or Q.")
