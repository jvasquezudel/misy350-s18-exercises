# Asking for the bill amount and converting it to an int
billamount = float(raw_input("Enter the bill amount: "))

#Asking for the tip amount
tip = float(raw_input("Enter tip percentage (as a decimal): "))

#Calculating total bill
billamount = round(billamount + (billamount * tip), 2)

print "You should pay $%s" % (billamount)
