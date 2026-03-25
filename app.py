print("AI Trucking Assistant")

load_weight = float(input("Enter load weight in pounds: "))
loaded_miles = float(input("Enter loaded trip miles: "))
deadhead_miles = float(input("Enter deadhead miles to pickup: "))
rate = float(input("Enter rate offered ($): "))
tolls = float(input("Enter toll cost ($): "))
cost_per_mile = float(input("Enter your truck cost per mile ($): "))

total_miles = loaded_miles + deadhead_miles
operating_cost = total_miles * cost_per_mile
total_expense = operating_cost + tolls
profit = rate - total_expense
rpm = rate / loaded_miles if loaded_miles != 0 else 0
all_mile_rpm = rate / total_miles if total_miles != 0 else 0

if profit < 0:
 print("⚠️ This load is NOT profitable")
else:
 print("✅ This load is profitable")

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
print(f"Loaded Rate Per Mile: ${rpm:.2f}")
print(f"All-In Rate Per Mile: ${all_mile_rpm:.2f}")
