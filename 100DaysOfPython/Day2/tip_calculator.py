print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = percent /100
tip = total * tip_as_percentage
total_with_tip = total + tip
bill_per_person = round((total_with_tip / people), 2)
print(f"Each person should pay: ${bill_per_person}")
