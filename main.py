balance = 1000
choice = ''
print("Welcome to the ATM. Enter D to deposit, W to withdraw, V to view balance, or E to exit.")
while choice not in ['e','d','w','v']:
    choice = input("You have not entered D, W, V, or E.\nPlease enter D, W, V, or E: ").lower()
    while choice != 'e':
        if choice == 'd':
            amount = float(input("Enter your deposit amount: "))
            balance += amount
        elif choice =='w':
            amount = float(input("Enter your withdrawal amount: "))
            balance -= amount
        else:
            print(f'Your current balance is ${balance:.2f}')

        if balance < 0:
            print("Your net balance is negative. You will be charged a 5% interest fee.")

        choice = input("Enter D, W, V, or E: ").lower()
print("Thanks for using the ATM. Have a good day!")