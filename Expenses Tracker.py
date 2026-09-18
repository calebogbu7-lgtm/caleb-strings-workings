transactions = []
while True:
    print("1. Add transaction")
    print("2. view all transaction")
    print("3. search transactions")
    print("4. delete transaction")
    print("5. view balanace")
    print("6. Exit")
    choice = input("select a number ")
    if choice == "6":
        print("goodbye")
        break
    elif choice == "1":
        description = input("describe your transaction ")
        while True:
            status = input("i or e ")
            if status == "i" or status == "e":
                break
            else:
                print("enter exactly i or e")
        while True:
            try:
                amount = int(input("state amount "))
                print("amount added!")
                break
            except:
                print("please enter a valid number ")
        transactions.append({"description": description, "status": status, "amount": amount})
    elif  choice == "2":
        for x in range(len(transactions)):
            print(f"Trans: {transactions[x]['description']} Inc or Exp: {transactions[x]['status']}  amt: {transactions[x]['amount']}")
    elif choice == "3":
        search_trans = input("search transaction ")
        for transaction in transactions:
            if transaction["description"] == search_trans:
                print(f"Trans: {transaction['description']} Inc or Exp: {transaction['status']} amt: {transaction['amount']}")
    elif choice == "4":
        delete_trans = input("delete transaction ")
        for i, y in enumerate(transactions):
            if y["description"] == delete_trans:
                del transactions[i]
                print("Transaction deleted!")
    elif choice == "5":
        balance = 0
        for f in transactions: 
            if f["status"] == "i":
                balance = balance + f["amount"]
            else:
                balance = balance - f["amount"]
        print(f"current balance : {balance}")                                        
    else:
            print("please enter a  valid input")