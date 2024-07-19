print("Welcome to the tip calculator!")
billamount = input("What was the total bill?\n$")
tipamount = input("What tip percentage would you like to give?\n")
people = input("How many people are you going to split the bill with?\n")

billtip = float(billamount) * (float(tipamount) / 100)

billperperson = "%.2f" % round((float(billamount) + int(billtip)) / int(people) ,2)

print(f"Each person should pay: ${billperperson}")