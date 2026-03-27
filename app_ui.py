import streamlit as st

st.set_page_config(page_title="AI Trucking Profit Analyzer", page_icon="🚛", layout="centered")

st.title("🚛 AI Trucking Profit Analyzer")
st.caption("Make smarter load decisions. Maximize profit. Eliminate bad freight.")

# Inputs
load_weight = st.number_input("Load weight (lbs)", min_value=0.0, value=50000.0, step=1000.0)
loaded_miles = st.number_input("Loaded miles", min_value=0.0, value=800.0, step=10.0)
deadhead_miles = st.number_input("Deadhead miles", min_value=0.0, value=200.0, step=10.0)
rate = st.number_input("Rate ($)", min_value=0.0, value=2500.0, step=50.0)
tolls = st.number_input("Tolls ($)", min_value=0.0, value=100.0, step=10.0)
cost_per_mile = st.number_input("Cost per mile ($)", min_value=0.0, value=1.50, step=0.05)

if st.button("Analyze"):

    # Core calculations
    total_miles = loaded_miles + deadhead_miles
    operating_cost = total_miles * cost_per_mile
    total_expense = operating_cost + tolls
    profit = rate - total_expense
    all_in_rpm = rate / total_miles if total_miles != 0 else 0
    profit_per_mile = profit / total_miles if total_miles != 0 else 0

    # Rating logic
    if profit < 0:
        rating = "❌ LOSS"
        color = "red"
    elif all_in_rpm >= 2.75 and profit >= 800:
        rating = "🔥 ELITE LOAD"
        color = "green"
    elif all_in_rpm >= 2.50 and profit >= 500:
        rating = "✅ STRONG LOAD"
        color = "green"
    elif all_in_rpm >= 2.00:
        rating = "⚠️ DECENT — NEGOTIATE"
        color = "orange"
    else:
        rating = "🚫 WEAK LOAD"
        color = "red"

    # Decision logic
    if profit < 0:
        decision = "❌ DO NOT TAKE THIS LOAD"
        reason = "This load loses money after expenses."
    elif all_in_rpm >= 2.50 and profit >= 500:
        decision = "✅ TAKE THE LOAD"
        reason = "This load meets your target profit and RPM standards."
    elif all_in_rpm >= 2.00 and profit > 0:
        decision = "⚠️ NEGOTIATE"
        reason = "This load makes money, but it is below your preferred target."
    else:
        decision = "❌ DECLINE"
        reason = "This load is too weak on profit and/or RPM."

    # Negotiation logic
    target_rate = total_expense + 500
    rate_gap = target_rate - rate

    # Results
    st.subheader("Results")
    st.write(f"**Total Miles:** {total_miles:.1f}")
    st.write(f"**Operating Cost:** ${operating_cost:.2f}")
    st.write(f"**Total Expense:** ${total_expense:.2f}")
    st.write(f"**Profit:** ${profit:.2f}")
    st.write(f"**Profit Per Mile:** ${profit_per_mile:.2f}")
    st.write(f"**All-In RPM:** ${all_in_rpm:.2f}")

    st.subheader("Load Rating")
    st.markdown(f"<h3 style='color:{color};'>{rating}</h3>", unsafe_allow_html=True)

    st.subheader("Decision")
    st.write(decision)
    st.write(reason)

    st.subheader("Negotiation")
    st.write(f"**Target Rate:** ${target_rate:.2f}")

    if rate_gap > 0:
        st.error(f"Ask for: +${rate_gap:.2f}")
    else:
        st.success(f"You're over target by ${abs(rate_gap):.2f}")

    # Money advice
    st.subheader("Money Advice")
    if rate < total_expense + 500:
        st.warning("💡 Ask for more money — this load is below your profit goal.")
    elif rate > total_expense + 800:
        st.success("💰 You're well above target — strong load.")
    else:
        st.info("ℹ️ This load is workable, but not a major winner.")
