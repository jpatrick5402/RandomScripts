

wanted_savings = "A"
while type(wanted_savings) != int:
    try:
        wanted_savings = int(input("How much would you like to save each month: "))
    except:
        print("Please enter a number")
        wanted_savings = "A"

current_monthly_income = "B"
while type(current_monthly_income) != int:
    try:
        current_monthly_income = int(input("How much do you earn each month: "))
    except:
        print("Please enter a number")
        current_monthly_income = "B"

expences=[]
ans = "C"
while ans:
    try:
        ans = input("Type 'DONE' when finished.\nEnter the cost of each montly expence and press enter: ")
        if ans == "DONE": break
        expences.append(int(ans))
    except:
        print("Please enter a number")
    
total_expences = 0
for i in expences:
    total_expences = total_expences + i
print(f"Total expenses {total_expences}")