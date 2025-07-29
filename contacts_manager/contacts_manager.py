print("Welcome to Ana's Contact Manager!")

contacts = []
if action == "a":
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added successfully!")
elif action == "v":
    print("Your Contacts:")
    for contact in contacts:
        print(f"[contact["name"]}] - {contac["phone"]}")
elif action == "q":
    priny("Goodbye!")
    break
else:
    print("Invalid option. Please try A, V, or Q.")
