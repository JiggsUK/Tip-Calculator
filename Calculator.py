"""Calculator to determine the appropriate tip amount"""

bill_amount = float(input("How much is the bill?"))


def tip_suggestions(bill):
    ten_percent = bill * 0.1
    fifteen_percent = bill * 0.15
    twenty_percent = bill * 0.2
    thirty_percent = bill * 0.3

    print("10% tip: £" + ("{0:.2f}".format(ten_percent)))
    print("15% tip: £" + ("{0:.2f}".format(fifteen_percent)))
    print("20% tip: £" + ("{0:.2f}".format(twenty_percent)))
    print("30% tip: £" + ("{0:.2f}".format(thirty_percent)) + "  WOW! Feeling generous, aren't we?")


tip_suggestions(bill_amount)
tip_percentage = float(input("\nWhat percentage would you like to tip today?"))

tip_amount = bill_amount * (float(tip_percentage) / 100)
total_cost = bill_amount + tip_amount

print("Bill Amount:   £" + ("{0:.2f}".format(bill_amount)))
print("Tip Amount:    £" + ("{0:.2f}".format(tip_amount)))
print("Total Payable: £" + ("{0:.2f}".format(total_cost)))
