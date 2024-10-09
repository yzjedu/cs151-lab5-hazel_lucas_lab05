# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Set balance to 1000
2. Set choice as an empty string
3. While choice does not equal "e":
   1. While choice does not equal "e", "w", "v", or "d":
        1. Prompt user to enter choice "Invalid Input. Please enter D, W, V, or E.":
        2. Case correct choice to all lowercase 
   2. Check if choice equals "d":
        1. Prompt user to enter deposit value.
        2. Add deposit value to balance.
   3. Otherwise, check if choice equals "w":
        1. Prompt user to enter withdrawal amount
        2. Subtract withdrawal amount from balance
    4. Otherwise, 
       1. Output balance to user.
    5. Check if balance < 0:
        1. Output to user "Your net balance is negative. You will be charged a 5% interest fee."
    6. Prompt user to enter D (Deposit), W(Withdraw), V(View Balance), E(Exit) for choice 
    7. Case Correct choice to lowercase
