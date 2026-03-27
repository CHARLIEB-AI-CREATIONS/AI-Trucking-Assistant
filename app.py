print("AI Trucking Assistant")

while True:
    print("\n--- New Load ---")

    # Inputs
    load_weight = float(input("Enter load weight in pounds: "))
    loaded_miles = float(input("Enter loaded trip miles: "))
    deadhead_miles = float(input("Enter deadhead miles to pickup: "))
    rate = float(input("Enter rate offered ($): "))
    tolls = float(input("Enter toll cost ($): "))
    cost_per_mile = float(input("Enter your truck cost per mile ($): "))

    # Targets
    min_profit_target = 500
    min_all_in_rpm = 2.50

    # Calculations
    total_miles = loaded_miles + deadhead_miles
    operating_cost = total_miles * cost_per_mile
    total_expense = operating_cost + tolls
    profit = rate - total_expense
# Load Rating
if profit >= 800 and all_in_rpm >= 2.75:
    load_rating = "🔥 HIGH VALUE LOAD"
elif profit >= 300:
    load_rating = "⚠️ DECENT — NEGOTIATE"
else:
    load_rating = "❌ LOW VALUE LOAD"
    target_rate = total_expense + min_profit_target
    rate_gap = target_rate - rate

    profit_per_mile = profit / total_miles if total_miles != 0 else 0
    loaded_rpm = rate / loaded_miles if loaded_miles != 0 else 0
    all_in_rpm = rate / total_miles if total_miles != 0 else 0

    # Decision Logic
    if profit < 0:
        decision = "❌ LOSING MONEY — DO NOT TAKE THIS LOAD"
        reason = "You are paying to move this load."
    elif profit >= min_profit_target and all_in_rpm >= min_all_in_rpm:
        decision = "✅ TAKE THE LOAD"
        reason = "Profit and all-in RPM both meet your target."
    elif profit >= 200 and all_in_rpm >= 2.00:
        decision = "⚠️ MAYBE TAKE IT"
        reason = "It makes money, but below your strong standard."
    else:
        decision = "❌ DECLINE THE LOAD"
        reason = "Profit and/or RPM too weak."

    # Output
    print("\n--- Load Summary ---")
    print(f"Total Miles: {total_miles}")
    print(f"Operating Cost: ${operating_cost:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Estimated Profit: ${profit:.2f}")
    print(f"Profit Per Mile: ${profit_per_mile:.2f}")
    print(f"All-In RPM: ${all_in_rpm:.2f}")
    print(f"Suggested Rate (Target Profit): ${target_rate:.2f}")

    if rate_gap > 0:
        print(f"Ask for: +${rate_gap:.2f}")
    else:
        print("Current rate already meets your target")

    print("\n--- Decision ---")
    print(decision)
    print(reason)

    # Loop control
    again = input("\nRun another load? (y/n): ")
    if again.lower() != 'y':
        break
