#Jeffrey Godzisz
#MidTerm Program
#3/8/2022 CSC-121-01SY

#variables used from problem presented
goal = 500
caseCost = 8
barCost = 1.00
sgaDonation = .1
caseHolds = 12

#requesting input
sold = int(input("How many bars have been sold?\n"))
#input validation loop
while sold < 0:
    sold = int(input("Please enter a positve number for bars sold:\n"))

#calculations
casesSold = sold / caseHolds

casesCosts = casesSold * 8

subTotalEarned = sold - casesCosts

sgaEarned = subTotalEarned * sgaDonation

earned = subTotalEarned - sgaEarned

#information to be printed regardless of goal being met
print(f'Bars Sold: ${sold: ,.2f}')
print(f'Subtotal Profit: ${subTotalEarned: ,.2f}')
print(f'SGA Proceeds: ${sgaEarned: ,.2f}')
print(f'Cheer Teams Proceeds: ${earned: ,.2f}')

#decision structure for goal being met or not
if earned >= goal:
    print("Congratulations! You have raised $500 or more!")
else:
    print("Sorry! You did not meet your goal!")
