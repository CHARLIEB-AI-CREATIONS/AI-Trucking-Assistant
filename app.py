print("AI Trucking Assistant")

while True:
 print("\n--- New Load ---")

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
    
    profit_per_mile = profit / total_miles if total_miles != 0 else 0
    loaded_rpm = rate / loaded_miles if loaded_miles != 0 else 0
    all_in_rpm = rate / total_miles if total_miles != 0 else 0
    
    min_profit_target = 500
    min_all_in_rpm = 2.50
    
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
    
        print("\n--- Load Summary ---")
        print(f"Total Miles: {total_miles}")
        print(f"Estimated Profit: ${profit:.2f}")
        print(f"All-In RPM: ${all_in_rpm:.2f}")
        
        print("\n--- Decision ---")
        print(decision)
        print(reason)
        again = input("\nRun another load? (y/n): ")
        if again.lower() != 'y':
            break
