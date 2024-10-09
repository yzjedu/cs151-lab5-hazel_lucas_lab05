# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Set balance to 1000
2. Output to user ("Welcome to the ATM. Enter "d" to deposit, "w" to withdraw, "d" to view balance, or "e" to exit)
3. Set choice as an empty string
1. While choice does not equal "e", "w", "v", or "d":
     1. Prompt user to enter choice "You have not entered "e" "v" "w" or "v". Please enter one of the valid options.":
     2. Case correct choice to all lowercase 
   3. While choice does not equal "e":
      2. Check if choice equals "d":
         1. Prompt user to enter deposit amount.
         2. Add amount to balance.
      3. Otherwise, check if choice equals "w":
           1. Prompt user to enter withdrawal amount
           2. Subtract amount from balance
      4. Otherwise, check if choice equals "v"
         1. Output balance to user.
      5. Check if balance < 0:
          1. Output to user "Your net balance is negative. You will be charged a 5% interest fee."
      6. Prompt user to enter D (Deposit), W(Withdraw), V(View Balance), E(Exit) for choice 
      7. Case Correct choice to lowercase
8. Output to user "Thanks for using the ATM!"
