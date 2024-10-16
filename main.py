# Programmers: Lucas Podowski, Hazel
# Course:  CS151, Zelalem Yalew
# Due Date: 10/16/2024
# Lab Assignment: 5
# Problem Statement: Build a simulation of an ATM (Automatic Teller Machine)
# Data In: choice
# Data Out: Balance
balance = 1000

# Variable to store users choice
choice = ''

# Displays a welcome message and instructions
print("Welcome to the ATM. Enter D to deposit, W to withdraw, V to view balance, or E to exit.")

# Outer loop to ensure the user inputs a valid option at the start
while choice not in ['e', 'd', 'w', 'v']:
    # Prompt user to enter a valid choice (D, W, V, or E)
    choice = input("You have not entered D, W, V, or E.\nPlease enter D, W, V, or E: ").lower()

    # Continue interacting with the user until they choose to exit ('e')
    while choice != 'e':
        # If the user chooses to deposit ('d')
        if choice == 'd':
            amount = float(input("Enter your deposit amount: "))  # Get the deposit amount from user
            balance += amount  # Add the deposit amount to the balance
        # If the user chooses to withdraw ('w')
        elif choice == 'w':
            amount = float(input("Enter your withdrawal amount: "))  # Get the withdrawal amount from user
            balance -= amount  # Subtract the withdrawal amount from the balance
        # If the user chooses to view their balance ('v')
        else:
            print(f'Your current balance is ${balance:.2f}')  # Display the current balance to the user

        # Ask the user again for their choice to continue or exit

        if balance < 0:
            print("Your net balance is negative. You will be charged a 5% interest fee.")

        choice = input("Enter D, W, V, or E: ").lower()

# Display a goodbye message once the user chooses to exit ('e')
print("Thanks for using the ATM. Have a good day!")