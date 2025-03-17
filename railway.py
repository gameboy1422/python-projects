# Railway Reservation System

# Dictionary to store train details
trains = {
    "12345": {"name": "Express 101", "seats": 50, "source": "City A", "destination": "City B"},
    "67890": {"name": "Superfast 202", "seats": 30, "source": "City C", "destination": "City D"}
}

# Dictionary to store booked tickets
booked_tickets = {}

def display_trains():
    print("\nAvailable Trains:")
    print("Train Number | Train Name       | Available Seats | Source    | Destination")
    print("-" * 65)
    for train_number, details in trains.items():
        print(f"{train_number.ljust(12)} | {details['name'].ljust(16)} | {str(details['seats']).ljust(15)} | {details['source'].ljust(9)} | {details['destination']}")

def book_ticket():
    train_number = input("Enter Train Number: ")
    if train_number in trains:
        if trains[train_number]["seats"] > 0:
            passenger_name = input("Enter Passenger Name: ")
            ticket_id = f"TKT{len(booked_tickets) + 1}"
            booked_tickets[ticket_id] = {
                "train_number": train_number,
                "passenger_name": passenger_name,
                "status": "Confirmed"
            }
            trains[train_number]["seats"] -= 1
            print(f"Ticket booked successfully! Your Ticket ID is: {ticket_id}")
        else:
            print("Sorry, no seats available on this train.")
    else:
        print("Invalid Train Number.")

def check_ticket_status():
    ticket_id = input("Enter Ticket ID: ")
    if ticket_id in booked_tickets:
        ticket = booked_tickets[ticket_id]
        print(f"\nTicket ID: {ticket_id}")
        print(f"Passenger Name: {ticket['passenger_name']}")
        print(f"Train Number: {ticket['train_number']}")
        print(f"Status: {ticket['status']}")
    else:
        print("Invalid Ticket ID.")

def cancel_ticket():
    ticket_id = input("Enter Ticket ID: ")
    if ticket_id in booked_tickets:
        train_number = booked_tickets[ticket_id]["train_number"]
        trains[train_number]["seats"] += 1
        del booked_tickets[ticket_id]
        print("Ticket canceled successfully!")
    else:
        print("Invalid Ticket ID.")

def main_menu():
    while True:
        print("\nRailway Reservation System")
        print("1. Display Available Trains")
        print("2. Book a Ticket")
        print("3. Check Ticket Status")
        print("4. Cancel Ticket")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_trains()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            check_ticket_status()
        elif choice == "4":
            cancel_ticket()
        elif choice == "5":
            print("Thank you for using the Railway Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()