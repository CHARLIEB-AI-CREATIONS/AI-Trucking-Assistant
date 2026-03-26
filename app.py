print("AI Trucking Assistant")

# Inputs
load_weight = float(input("Enter load weight in pounds: "))
loaded_miles = float(input("Enter loaded trip miles: "))
deadhead_miles = float(input("Enter deadhead miles to pickup: "))
rate = float(input("Enter rate offered ($): "))
tolls = float(input("Enter toll cost ($): "))
cost_per_mile = float(input("Enter your truck cost per mile ($): "))

# Calculations
total_miles = loaded_miles + deadhead_miles
operating_cost = total_miles * cost_per_mile
total_expense = operating_cost + tolls
profit = rate - total_expense
profit_per_mile = profit / total_miles if total_miles != 0 else 0
loaded_rpm = rate / loaded_miles if loaded_miles != 0 else 0
all_in_rpm = rate / total_miles if total_miles != 0 else 0

# Targets (your standards)
min_profit_target = 500
min_all_in_rpm = 2.50
 profit < 0:
print("🚨 LOSING MONEY — DO NOT TAKE THIS LOAD")
# Decision Logic
if profit >= min_profit_target and all_in_rpm >= min_all_in_rpm:
 decision = "✅ TAKE THE LOAD"
 reason = "Profit and all-in RPM both meet your target."
elif profit >= 200 and all_in_rpm >= 2.00:
 decision = "⚠️ MAYBE TAKE IT"
 reason = "It makes money, but it is below your strong-load standard."
else:
 decision = "❌ DECLINE THE LOAD"
 reason = "Profit and/or all-in RPM are too weak."
# Output
print("\n--- Load Summary ---")
print(f"Load Weight: {load_weight} lbs")
print(f"Loaded Miles: {loaded_miles}")
print(f"Deadhead Miles: {deadhead_miles}")
print(f"Total Miles: {total_miles}")
print(f"Rate Offered: ${rate:.2f}")
print(f"Tolls: ${tolls:.2f}")
print(f"Cost Per Mile: ${cost_per_mile:.2f}")
print(f"Operating Cost: ${operating_cost:.2f}")
print(f"Total Expense: ${total_expense:.2f}")
print(f"Estimated Profit: ${profit:.2f}")
print(f"Profit Per Mile: ${profit_per_mile:.2f}")print(f"Loaded Rate Per Mile: ${loaded_rpm:.2f}")
print (f"All-In Rate Per Mile: ${all_in_rpm:.2f}")
print("\n--- Decision ---")
print(decision)
print(reason)
