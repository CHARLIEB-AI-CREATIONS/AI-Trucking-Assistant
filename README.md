# 🚛 AI Trucking Profit Analyzer  
**Built by Charles Barnes**

A Python-based tool that evaluates trucking loads in real time and determines whether a load is profitable, negotiable, or should be rejected.

---

## 🚀 Features

- Calculates total miles (loaded + deadhead)
- Computes operating cost and total expenses
- Calculates profit and profit per mile
- Displays loaded RPM and all-in RPM
- Provides clear TAKE / NEGOTIATE / REJECT decisions
- Suggests better rates for negotiation
- Identifies high-value and low-value loads instantly

---

## 📊 Financial Insights

Breakdown includes:

- Total miles
- Operating cost
- Total expense
- Profit
- Profit per mile
- All-in RPM

---

## 💡 Profit Optimization Logic

- Flags bad loads instantly ❌  
- Suggests negotiation opportunities ⚠️  
- Highlights strong and elite loads 🔥  
- Uses real trucking metrics (RPM, cost per mile, deadhead impact)

---

## 🧠 Decision System

The tool classifies loads into:

- 🔥 **HIGH VALUE LOAD** → Strong profit + high RPM  
- ⚠️ **DECENT – NEGOTIATE** → Close to target, needs better rate  
- ❌ **DO NOT TAKE THIS LOAD** → Not profitable  

---

## 🖥️ UI Version (Streamlit App)

This project includes a web-based interface for easier use.

### Run locally:

```bash
pip install streamlit
python3 -m streamlit run app_ui.py
