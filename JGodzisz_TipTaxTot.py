#Jeffrey Godzisz
#CSC 121-01SY
#Tip, Tax, and Total Program
import turtle

#display a dialog box for numeric input
price_of_meal = turtle.numinput('Input needed', 'What was the price of your meal:', default=0.00)
#preform calculations
tip = price_of_meal * 0.18
tax = price_of_meal * 0.07
total = price_of_meal + tax + tip

print(f'Price of meal: ${price_of_meal:.2f}')
print(f'18% tip: ${tip:.2f}')
print(f'Tax: ${tax:.2f}')
print(f'Total Bill: ${total:.2f}')
