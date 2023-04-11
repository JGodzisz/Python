#Jeffrey Godzisz
#CSC 121-01SY
#Sales Tax Calculator
price = float(input('please enter the total price of your item: \n'))
stateTax = price * 0.05
countyTax = price * 0.025
print(f'Purchase price: ${price:.2f}')
print(f'State Tax: ${stateTax:.2f}')
print(f'County Tax: ${countyTax:.2f}')
print(f'Total Tax: ${countyTax + stateTax:.2f}')
print(f'Total Price: ${price + stateTax + countyTax:.2f}')
