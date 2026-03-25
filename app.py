print("AI Trucking Assistant")

load_weight = float(input("Enter load weight in pounds: "))
miles = float(input("Enter trip miles: "))
rate = float(input("Enter rate offered ($): "))
fuel_cost = float(input("Enter estimated fuel cost ($): "))

profit = rate - fuel_cost

if profit < 0:
  print("⚠️ This load is NOT profitable")
else:
  print("✅ This load is profitable")

rpm = rate/ miles if miles != 0 else 0

print("\n--- Load Summary ---")
print(f"Load Weight: {load_weight} lbs")
print(f"Trip Miles: {miles}")
print(f"Rate Offered: ${rate:.2f}")
print(f"Estimated Fuel Cost: ${fuel_cost:.2f}")
print(f"Estimated Profit: ${profit:.2f}")
print(f"Rate Per Mile: ${rpm:.2f}")
