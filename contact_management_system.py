import re
import os

def add_contact():
    # while True:
    name = input("Please enter the first and last name of the new contact: ")
    phone = input("Please enter their 10 digit phone number (numbers only): ")
    try:
        if validate_phone(phone):
            print("Thank you.")
        else:
            print("Please only enter the ten digits of the phone number, no spaces or dashes.")
    except:
        print(f"{phone} is not a valid phone.")
    email = input("Please enter their email address: ")
    try:
        if validate_email(email):
            print("Thank you.")
        else:
            print(f"{email} is not valid.")
    except Exception as e:
        print(f"An error occurred: {e}")
    address = input("Please enter their full address: ")
    contact_to_add = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    print(contact_to_add) # will remove before finalizing
    try: 
        contact_list[phone] = contact_to_add
    except:
        print("It didn't work.")
    else: 
        print("It worked!")
        print(f" New contact list: {contact_list}")

def edit_contact():
    pass

def delete_contact():
    pass
    # Which contact do you want to delete? Please enter their name: 
    # Display all contact info, is this the contact you wish to delete? (yes/no)
    # if confirmation == "yes":
    # delete contact

def search_contact():
    search_option = input("Would you like to search by:\n1. Name\n2. Phone number\n3. Email address\n4. Address\n")
    if search_option == "1":
        pass
    elif search_option == "2":
        pass
    elif search_option == "3":
        pass
    elif search_option == "4":
        pass
    else:
        print("That is not a valid selection, returning to the menu.")

def display_contacts(contact_list):
    for contact in contact_list: # (might need.values())
        for name, phone, email, address in contact.values():
            print(f"Name: {name}, Phone number: {phone}, Email address: {email}, Address: {address}")

def export_contacts():
    pass

def import_contacts():
    pass

def validate_email(email):
    pattern = r"^[a-zA-Z0-9.-_%+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_phone(phone):
    pattern = r"\d{10}"
    if re.match(pattern, phone):
        return True
    else:
        return False

contact_list = {"9999999999": 
                {"name": "John Smith", "phone": "9999999999", "email": "email@email.com", "address": "123 main dr. Denver, CO 80221"}
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
        add_contact()
    elif menu_action == "2":
        edit_contact()
    elif menu_action == "3":
        delete_contact()
    elif menu_action == "4":
        search_contact()
    elif menu_action == "5":
        display_contacts()
    elif menu_action == "6":
        export_contacts()
    elif menu_action == "7":
        import_contacts()
    elif menu_action == "8":
        break
    else:
        print("Please enter a number to select an option.")