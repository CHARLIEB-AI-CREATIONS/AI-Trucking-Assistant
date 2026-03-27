import streamlit as st

st.set_page_config(page_title="AI Trucking Assistant", page_icon="🚛", layout="wide")

# Header
st.title("🚛 AI Trucking Assistant")
st.caption("Load profitability, rate negotiation, and decision support for trucking operations.")

# Sidebar
st.sidebar.header("Decision Standards")
st.sidebar.write("These rules drive the load recommendation:")
st.sidebar.write("- Minimum target profit: $500")
st.sidebar.write("- Minimum all-in RPM: $2.50")
st.sidebar.write("- Negative profit = automatic decline")
st.sidebar.write("- Strong profit + strong RPM = take load")
st.sidebar.write("- Mid profit = negotiate")
st.sidebar.write("- Weak profit/RPM = decline")

# Targets
min_profit_target = 500.0
min_all_in_rpm = 2.50

# Input layout
col1, col2 = st.columns(2)

with col1:
    load_weight = st.number_input("Load weight (lbs)", min_value=0.0, value=50000.0, step=1000.0)
    loaded_miles = st.number_input("Loaded miles", min_value=0.0, value=800.0, step=10.0)
    deadhead_miles = st.number_input("Deadhead miles", min_value=0.0, value=200.0, step=10.0)

with col2:
    rate = st.number_input("Rate offered ($)", min_value=0.0, value=2500.0, step=50.0)
    tolls = st.number_input("Tolls ($)", min_value=0.0, value=100.0, step=10.0)
    cost_per_mile = st.number_input("Truck cost per mile ($)", min_value=0.0, value=1.50, step=0.05)

if st.button("Analyze Load", use_container_width=True):

    # Core calculations
    total_miles = loaded_miles + deadhead_miles
    operating_cost = total_miles * cost_per_mile
    total_expense = operating_cost + tolls
    profit = rate - total_expense

    profit_per_mile = profit / total_miles if total_miles != 0 else 0
    loaded_rpm = rate / loaded_miles if loaded_miles != 0 else 0
    all_in_rpm = rate / total_miles if total_miles != 0 else 0

    break_even_rate = total_expense
    target_rate = total_expense + min_profit_target
    rate_gap = target_rate - rate

    # Load rating
    if profit < 0:
        load_rating = "❌ TRASH LOAD"
    elif rate_gap <= -300:
        load_rating = "🔥 HIGH VALUE LOAD"
    elif profit >= 800:
        load_rating = "🔥 STRONG PROFIT LOAD"
    elif profit >= 300 and all_in_rpm >= 2.00:
        load_rating = "⚠️ DECENT — NEGOTIATE"
    else:
        load_rating = "⚠️ MARGINAL LOAD"

    # Decision logic
    if profit < 0:
        decision = "❌ DO NOT TAKE THIS LOAD"
        reason = "This load loses money after mileage and toll costs."
    elif profit >= min_profit_target and all_in_rpm >= min_all_in_rpm:
        decision = "✅ TAKE THE LOAD"
        reason = "Profit and all-in RPM both meet your target."
    elif profit >= 200 and all_in_rpm >= 2.00:
        decision = "⚠️ NEGOTIATE FOR MORE"
        reason = "The load makes money, but it is below your preferred standard."
    else:
        decision = "❌ DECLINE THE LOAD"
        reason = "Profit and/or all-in RPM are too weak."

    # Top metric cards
    st.subheader("Key Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Estimated Profit", f"${profit:,.2f}")
    m2.metric("All-In RPM", f"${all_in_rpm:,.2f}")
    m3.metric("Break-Even Rate", f"${break_even_rate:,.2f}")
    m4.metric("Target Rate", f"${target_rate:,.2f}")

    # Main detail section
    left, right = st.columns(2)

    with left:
        st.subheader("Load Summary")
        st.write(f"**Load Weight:** {load_weight:,.0f} lbs")
        st.write(f"**Loaded Miles:** {loaded_miles:,.1f}")
        st.write(f"**Deadhead Miles:** {deadhead_miles:,.1f}")
        st.write(f"**Total Miles:** {total_miles:,.1f}")
        st.write(f"**Rate Offered:** ${rate:,.2f}")
        st.write(f"**Tolls:** ${tolls:,.2f}")
        st.write(f"**Cost Per Mile:** ${cost_per_mile:,.2f}")
        st.write(f"**Operating Cost:** ${operating_cost:,.2f}")
        st.write(f"**Total Expense:** ${total_expense:,.2f}")

    with right:
        st.subheader("Profitability Analysis")
        st.write(f"**Profit Per Mile:** ${profit_per_mile:,.2f}")
        st.write(f"**Loaded RPM:** ${loaded_rpm:,.2f}")
        st.write(f"**All-In RPM:** ${all_in_rpm:,.2f}")
        st.write(f"**Load Rating:** {load_rating}")
        st.write(f"**Suggested Rate (for ${min_profit_target:,.0f} target profit):** ${target_rate:,.2f}")

        if rate_gap > 0:
            st.warning(f"Ask for: +${rate_gap:,.2f}")
        else:
            st.success(f"You are OVER target by ${abs(rate_gap):,.2f}")

    # Final decision box
    st.subheader("Decision")
    st.write(decision)
    st.write(reason)

    if profit < 0:
        st.error("Bad load. You are paying to move this freight.")
    elif decision == "⚠️ NEGOTIATE FOR MORE":
        st.warning("This is not a dead load, but you should push for a better rate.")
    else:
        st.success("This load clears your standards.")
