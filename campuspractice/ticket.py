import json
import os
def save_tickets(tickets):
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)
def load_tickets():
    try:
        with open("tickets.json", "r") as file:
            tickets = json.load(file)
            return tickets
    except FileNotFoundError:
        return []

def create_ticket ():
    print("\n---- CREATE TICKET----")
    while True:
        title = input("enter your title: ")

        if not title.strip() or title.isdigit():
            print("Error: Enter a valid title")
            continue
        break    
    while True:
        category = input("enter your category( network, software, hardware, others): ").strip().lower()
     
        if category  in ("network", "software", "hardware", "others"):
            break
        else:
            print("error: enter a valid category")
        
    while True:
        urgency = input("enter your urgency(low, meiudm, high): ").strip().lower()
       
        if urgency  in ("low", "medium", "high"):
            break
        else:
            print("enter a valid urgency")
    while True:
        try:
            affected_user = int(input("number of affected user: "))

            if affected_user < 1:
                print("Error: number must atleast be 1")
            
            else:
                break


        except ValueError:
            print("Error: Enter a valid whole number")
            continue
        
    if urgency == "high" and affected_user >= 10:
        priority = ("critical")
    elif urgency == "high" or affected_user >= 10:
        priority = ("high")
    elif urgency == "medium" or affected_user >= 3:
        priority = ("medium")
    else:
        priority = ("low")

    ticket = { 
        "title": title,
    "category": category,
    "urgency": urgency,
    "affected user": affected_user,
    "priority": priority
    }
    tickets = load_tickets()
    tickets.append(ticket)
    save_tickets(tickets)

    print("\n---CREATED TICKET---:")
    for key, value in ticket.items():
        print (f"{key}: {value}")
        
    print("ticket created sucessfully")
create_ticket()