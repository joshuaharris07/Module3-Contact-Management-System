import re
import os

def add_contact(contact_list):
    while True:
        phone_entry = input("Please enter the 10 digit phone number: ")
        try:
            if validate_phone(phone_entry):
                valid, phone = validate_phone(phone_entry)   # Pulls the phone number out of the function for use
            else:
                print(f"{phone_entry} is not a valid phone number. Returning to the menu.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        if phone in contact_list:
            print(f"That phone number is already associated with {contact_list[phone]["name"]} in your contacts. Returning to the menu.")
            break
        name = input("Please enter the name of the new contact: ")
        email = input("Please enter their email address: ")
        try:
            if validate_email(email):
                print("Thank you.")
            else:
                print(f"{email} is not a valid email. Returning to the menu.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        address = input("Please enter their full address: ")
        contact_to_add = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        print(contact_to_add) # will remove before finalizing
        try: 
            contact_list[phone] = contact_to_add
        except:
            print("An error occurred adding that contact. Returning to the menu.")
        else: 
            print(f"Contact has been successfully added. Returning to the menu.")
        finally:
            break

def edit_contact(contact_list):
    while True:
        phone_entry = input("Please enter the 10 digit phone number: ")
        try:
            if validate_phone(phone_entry):
                valid, phone = validate_phone(phone_entry)   # Pulls the phone number out of the function for use
            else:
                print(f"{phone_entry} is not a valid phone number. Returning to the menu.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        if phone not in contact_list:
                print(f"That phone number is not currently in your contacts. Returning to the menu.")
                break
        action = input("What would you like to edit?\n1. Name\n2. Email Address\n 3. Address\n4. Delete the contact\n")
        if action == "1":
            name_change = input("Please enter the new name: ")
            contact_list[phone]["name"] = name_change
            print(f"The name has successfully been changed to: {name_change}\nReturning to the menu.")
            break
        elif action == "2":
            email_change = input("Please enter the new email address: ")
            contact_list[phone]["email"] = email_change
            print(f"The email address has successfully been changed to: {email_change}\nReturning to the menu.")
            break
        elif action == "3":
            address_change = input("Please enter the new address: ")
            contact_list[phone]["address"] = address_change
            print(f"The address has successfully been changed to: {address_change}\nReturning to the menu.")
            break
        elif action == "4":
            delete_contact()
        else:
            print("That is not a valid selection.")

def delete_contact(contact_list):
    while True:
        phone_entry = input("Please enter the 10 digit phone number: ")
        try:
            if validate_phone(phone_entry):
                valid, phone = validate_phone(phone_entry)   # Pulls the phone number out of the function for use
            else:
                print(f"{phone_entry} is not a valid phone number. Returning to the menu.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        if phone in contact_list:
            confirmation = input(f"Are you sure you want to delete the contact for {contact_list[phone]["name"]}? (yes/no):\n").lower()
            if confirmation == "yes":
                del contact_list[phone]
                print("That contact has successfully been deleted. Returning to the menu.")
                break
        else:
            print(f"That phone number is not currently in your contacts. Returning to the menu.")
            break

def search_contact(contact_list):
    while True:
        phone_entry = input("Please enter the 10 digit phone number: ")
        try:
            if validate_phone(phone_entry):
                valid, phone = validate_phone(phone_entry)   # Pulls the phone number out of the function for use
            else:
                print(f"{phone_entry} is not a valid phone number. Returning to the menu.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        if phone in contact_list:
            print(f"Name: {contact_list[phone]["name"]}\nPhone: {contact_list[phone]["phone"]}\nEmail Address: {contact_list[phone]["email"]}\nAddress: {contact_list[phone]["address"]}")
        else:
            print("That contact was not found.")
        print("Returning to the menu.")
        break

def display_contacts(contact_list):
    for contact in contact_list.values():
        print(f"Name: {contact["name"]}, Phone number: {contact["phone"]}, Email address: {contact["email"]}, Address: {contact["address"]}")

def export_contacts(contact_list):
    with open("my_contact_list.txt", "w") as file:
        for contact in contact_list.values():
            file.write(f"\nName: {contact["name"]}\nPhone number: {contact["phone"]}\nEmail address: {contact["email"]}\nAddress: {contact["address"]}\n")
        

def import_contacts():
    pass

def validate_email(email):
    pattern = r"^[a-zA-Z0-9.-_%+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_phone(phone_entry):
    phone_list = []
    for char in phone_entry:
        if char.isnumeric():
            phone_list.append(char)
    phone = "".join(phone_list)
    pattern = r"\d{10}"
    if re.match(pattern, phone):
        return True, phone
    else:
        return False

contact_list = {
    "9999999999": {"name": "John Smith", "phone": "9999999999", "email": "email@email.com", "address": "123 main dr. Denver, CO 80221"},
    "7202755650": {"name": "Josh Harris", "phone": "7202755650", "email": "joshua.harris07@gmail.com", "address": "10570 Adams Cir Northglenn, CO 80233"},
}

print("Welcome to the Contact Managements System!")
while True:
    menu_action = input("""\nMenu\n
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Exit
""")

    if menu_action == "1":
        add_contact(contact_list)
    elif menu_action == "2":
        edit_contact(contact_list)
    elif menu_action == "3":
        delete_contact(contact_list)
    elif menu_action == "4":
        search_contact(contact_list)
    elif menu_action == "5":
        display_contacts(contact_list)
    elif menu_action == "6":
        export_contacts(contact_list)
    elif menu_action == "7":
        import_contacts()
    elif menu_action == "8":
        print("Thank you for using the Contact Management System, have a good day!")
        break
    else:
        print("Please enter a number to select an option.")