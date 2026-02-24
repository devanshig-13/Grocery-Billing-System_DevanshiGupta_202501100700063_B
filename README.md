"Problem Statement"

Write a Python program that calculates the total cost of five items based on their individual prices and quantities.

If the total amount exceeds 100, apply a 10% discount and display the final payable amount along with the discount applied.

The program should:

Take the price of 5 items as input (float values)

Take the quantity of each item as input (integer values)

Calculate the total cost

Apply a 10% discount if the total cost is greater than 100

Display the total amount, discount, and final amount



"Approach"

Take input for the prices of five items using float(input()).

Take input for the quantities of each item using int(input()).

Calculate the total cost using the formula:

total = (price × quantity) for all items

Check if the total amount is greater than 100.

If the condition is true:

Calculate 10% discount: discount = total * 0.1

Compute final amount: final_amount = total - discount

Print the total amount, discount, and final payable amount.



"sample output" 

Enter price of item 1: 50

Enter price of item 2: 20

Enter price of item 3: 30

Enter price of item 4: 10

Enter price of item 5: 5

2

1

1

1

1

Enter amount = 165.0

Discount = 16.5

Final amount = 148.5

