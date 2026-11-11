# Change Maker

A command-line cashier tool written in Python. It compares an item's bill
with the amount paid, reports what is owed or the balance to give back,
and keeps a numbered ticket for every payment.

## Features

- Main menu with input validation (bad or negative input asks again)
- Money handled in whole cents internally, so calculations are exact
- A status for every payment: `owing`, `needs balance`, or `equilibrium`
- Tickets saved to `tickets.json` and loaded when the program starts
- Handles a missing or damaged `tickets.json` without crashing
- View all tickets, shown in dollars
- Unique ticket numbers
- Search a ticket by number, with a "not found" message

## Requirements

- Python 3.8 or newer (developed on Python 3.12)
- No extra packages needed

## How to run

```bash
python3 changemaker.py
```

## How to use

```text
MAIN MENU
1. Make your calculation
2. view all tickets
3. Search a ticket
4. Exit
```

1. **Make your calculation:** enter the bill, then the amount paid. The
   program shows what is still owed or the balance, and saves a ticket.
2. **View all tickets:** prints every saved ticket.
3. **Search a ticket:** enter a ticket number to see that ticket.
4. **Exit:** ends the program.

## Example

```text
your bill: 4.35
amount paid: 5
your balance is $0.65
```

## How it works

| Function | Job |
|---|---|
| `get_bill()` | Asks for the bill until it is valid, returns cents |
| `get_amount()` | Asks for the amount paid until it is valid, returns cents |
| `show_result(bill, amount)` | Prints owed, balance, or exact |
| `save_tickets(tickets)` | Writes the ticket list to `tickets.json` |
| `load_tickets()` | Reads tickets back, returns `[]` if the file is missing or damaged |
| `main()` | Runs the menu and calls the other functions |

## Data format

Each ticket is a dictionary stored in `tickets.json`. Money is stored in
cents, so `4.35` is saved as `435`.

```json
{"number": 1, "bill": 435, "amount": 500, "status": "needs balance"}
```

## Design decisions

- **Whole cents instead of floats:** floats cannot store most decimals
  exactly (`5.00 - 4.35` gives `0.6499999999999995`). Whole numbers are exact.
  Dollars are only shown when printing.
- **Functions with one job:** input, calculation, display, and file handling
  are separate, so each part is easy to test and change.
- **Ticket numbers use `len(tickets) + 1`:** this works while tickets are
  never deleted. Deleting one would create duplicate numbers.

## Known limitations

- No way to void or delete a ticket
- No customer name or date on tickets
- Old tickets saved before numbering was added have no `number` key
- A damaged `tickets.json` is replaced with an empty list on the next save

## Possible next steps

- Daily summary (total paid, total owed, ticket count)
- Customer name and date/time on each ticket
- Void a ticket instead of deleting it
- Automated tests
