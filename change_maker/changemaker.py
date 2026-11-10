import json
def get_bill():
    while True:
        try:
            bill = round(float(input("your bill: ")) * 100)
            if bill < 0:
                print("Oops: number must be positive")
                continue
        except ValueError:
            print("invalid entry")
            continue
        return bill
def get_amount():
    while True:
        try:
            amount = round(float(input("amount paid: "))* 100)      
            if amount < 0:
                print("Oops: number must be positive")
                continue
                    
        except ValueError:
            print("invalid entry")
            continue
        return amount
def show_result(bill, amount):
    if bill > amount:
        print(f"you still owe: ${(bill - amount) / 100:.2f}")
            
    elif bill < amount:
        print(f"your balance is ${(amount - bill) / 100:.2f}")
    elif bill == amount:
        print("everything up to date")
def save_ticket(tickets):
    with open("tickets.json", "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent = 4)
def load_tickets():
    try:
        with open("tickets.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
            return []
def main():
    print("=" * 23)
    print("WELCOME TO CHANGE MAKER")
    print("=" * 23)
    tickets = load_tickets()
    while True:
        print("MAIN MENU")
        print("1. Make your calculation")
        print("2. view all tickets")
        print("3. search tickets")
        print("4. Exit")
        try:
            information = int(input("please select a number: "))
        except ValueError:
            print("invalid entry")
            continue
        if information == 1:
            bill = get_bill()
            amount = get_amount()
            show_result(bill, amount)
            if bill > amount:
                status = "owing"
            elif bill < amount:
                status = "needs balance"
            elif bill == amount:
                status = "equilibrium"
            ticket_number = len(tickets) + 1
            ticket = {"number": ticket_number, "bill": bill, "amount": amount, "status": status}
            tickets.append(ticket)
            save_ticket(tickets)
        if information == 3:
            try:
                number = int(input("Enter Ticket Number: "))
            except ValueError:
                print("Oops: invalid entry")
                continue
            found = False
            for ticket in tickets:
                if ticket['number'] == number:
                    print(f"Ticket {ticket['number']}")
                    print(f"bill: ${ticket['bill'] / 100:.2f}")
                    print(f"amountpaid: ${ticket['amount'] / 100:.2f}")
                    print(f"status: {ticket['status']}")
                    print("-" * 23)
                    break     
            if not found:
                print("ticket not found")
        if information == 2:
            for ticket in tickets:
                print(f"Ticket {ticket['number']}")
                print(f"bill: ${ticket['bill'] / 100:.2f}")
                print(f"amountpaid: ${ticket['amount'] / 100:.2f}")
                print(f"status: {ticket['status']}")
                print("-" * 23)
            if not tickets:
                print(" No Ticket Yet")
        if information == 4:
            print("goodbye")
            break
        elif information < 1 or information > 4:
            print("Oops: number must be within 1 or 4")
main()