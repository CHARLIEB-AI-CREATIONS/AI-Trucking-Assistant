import streamlit as st

st.set_page_config(page_title="AI Trucking Assistant", page_icon="🚛")

st.title("🚛 AI Trucking Assistant")
st.write("Evaluate trucking loads instantly.")

load_weight = st.number_input("Load weight (lbs)", value=50000.0)
loaded_miles = st.number_input("Loaded miles", value=800.0)
deadhead_miles = st.number_input("Deadhead miles", value=200.0)
rate = st.number_input("Rate ($)", value=2500.0)
tolls = st.number_input("Tolls ($)", value=100.0)
cost_per_mile = st.number_input("Cost per mile ($)", value=1.5)

if st.button("Analyze"):

    total_miles = loaded_miles + deadhead_miles
    operating_cost = total_miles * cost_per_mile
    total_expense = operating_cost + tolls
    profit = rate - total_expense

    all_in_rpm = rate / total_miles if total_miles != 0 else 0

    st.subheader("Results")
    st.write(f"Total Miles: {total_miles}")
    st.write(f"Total Expense: ${total_expense}")
    st.write(f"Profit: ${profit}")
    st.write(f"All-In RPM: ${all_in_rpm:.2f}")

    if profit < 0:
        st.error("❌ DO NOT TAKE THIS LOAD")
    elif profit >= 500 and all_in_rpm >= 2.5:
        st.success("✅ TAKE THE LOAD")
    else:
        st.warning("⚠️ NEGOTIATE")
