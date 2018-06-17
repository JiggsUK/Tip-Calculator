"""Calculator to determine the appropriate tip amount"""

bill_amount = float(input("How much is the bill?"))
tip_percentage = float(input("What percentage would you like to tip today?"))

tip_amount = bill_amount * (float(tip_percentage) / 100)
total_cost = bill_amount + tip_amount

print("Bill Amount: £" + str(bill_amount))
print("Tip Amount: £" + str(tip_amount))
print("Total Payable: £" + str(total_cost))
