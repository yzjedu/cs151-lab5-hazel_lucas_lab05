# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Set balance to 1000
2. Output to user ("Welcome to the ATM. Enter "d" to deposit, "w" to withdraw, "v" to view balance, or "e" to exit)
3. Set choice as an empty string
4. While choice does not equal "e", "w", "v", or "d":
     1. Prompt user to enter choice "You have not entered "e" "v" "w" or "v". Please enter one of the valid options.":
     2. Case correct choice to all lowercase 
   3. While choice does not equal "e":
      1. Check if choice equals "d":
         1. Prompt user to enter deposit amount.
         2. Add amount to balance.
      2. Otherwise, check if choice equals "w":
           1. Prompt user to enter withdrawal amount
           2. Subtract amount from balance
      3. Otherwise, check if choice equals "v"
         1. Output balance to user.
      4. Check if balance < 0:
          1. Output to user "Your net balance is negative. You will be charged a 5% interest fee."
      5. Prompt user to enter for choice 
      6. Case Correct choice to lowercase
5. Output to user "Thanks for using the ATM!"
