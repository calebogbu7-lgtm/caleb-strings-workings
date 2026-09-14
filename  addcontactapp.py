# Create an empty list to store all contacts
contacts = []

# Keep looping forever until the user chooses to exit
while True:
    # Display the menu options
    print("1.Add contact")
    print("2.view all contacts")
    print("3.search for a contact")
    print("4.delete contact")
    print("5.Exit")

    # Ask the user to pick an option (always returns a string)
    number = input("select a number ")

    # Check if the user wants to exit
    if number == "5":
        print("goodbye")
        break  # stops the while True loop, ending the program

    # Handle "Add contact"
    elif number == "1":
        contact_number = (input("enter number "))   # ask for phone number
        contact_name = input("enter name ")           # ask for name
        contact_email = input("enter email ")          # ask for email

        # Bundle all three pieces into one dictionary and add it to the list
        contacts.append({"phone number": contact_number, "name": contact_name, "email": contact_email})

        print("contact detailes added")  # confirm to the user

    # Handle "View all contacts"
    elif number == "2":
        # Loop through every valid index position in the contacts list
        for x in range(len(contacts)):
            # Print that specific contact's phone, name, and email
            print(f"phone number: {contacts[x]['phone number']}, name: {contacts[x]['name']}, email: {contacts[x]['email']}")

    # Handle "Search for a contact"
    elif number == "3":
        search_name = input("search name: ")  # ask what name to search for

        # Loop through each contact dictionary directly (don't need the index here)
        for contact in contacts:
            # Check if this contact's name matches what was searched
            if contact["name"] == search_name:
                # Print the matching contact's details
                print(f"phone number: {contact['phone number']}, name: {contact['name']}, email: {contact['email']}")

    # Handle "Delete contact"
    elif number == "4":
        delete_name = input("Enter name to delete: ")  # ask what name to delete

        # Loop through contacts, getting both the position (i) and the contact itself
        for i, contact in enumerate(contacts):
            # Check if this contact's name matches what should be deleted
            if contact["name"] == delete_name:
                del contacts[i]  # remove that specific contact from the list entirely
                print("Contact deleted!")  # confirm to the user

    # Catch-all for any input that isn't 1-5
    else:
        print("please choose a valid number")