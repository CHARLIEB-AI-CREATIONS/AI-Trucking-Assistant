# 🚛 AI Trucking Profit Analyzer  
**Built by Charles Barnes**

A Python-based AI decision tool that evaluates trucking load profitability and provides clear **take / negotiate / decline** recommendations based on real operating costs.

---

## 📌 Overview

This application helps owner-operators, dispatchers, and logistics professionals make smarter load decisions by analyzing:

- Total miles (loaded + deadhead)
- Operating costs
- Profit margins
- Revenue per mile (RPM)

Instead of guessing, this tool delivers **data-driven decisions**.

---

## ⚙️ Features

- Calculates total miles and expenses  
- Computes profit and profit per mile  
- Displays All-In RPM (Revenue Per Mile)  
- Provides clear decision outcomes  
- Includes negotiation guidance  
- Built with an interactive UI using Streamlit  

---

## 🚀 Advanced Features (AI Decision Engine)

### 🔥 Intelligent Load Rating System

Each load is automatically classified:

- ❌ **LOSS** — Negative profit  
- 🚫 **WEAK LOAD** — Low efficiency  
- ⚠️ **DECENT — NEGOTIATE** — Profitable but below target  
- ✅ **STRONG LOAD** — Meets solid standards  
- 🔥 **ELITE LOAD** — High-profit opportunity  

---

### 🧠 Smart Decision Logic

Simulates real-world dispatcher thinking using:

- Profitability  
- Expense analysis  
- All-in RPM  

Outputs:
- ✅ TAKE THE LOAD  
- ⚠️ NEGOTIATE  
- ❌ DECLINE  

---

### 💰 Negotiation Engine

- Calculates target rate needed to hit profit goals  
- Shows how much to ask brokers for  
- Identifies over-target loads  

---

### 📊 Financial Insights

Breakdown includes:

- Total miles  
- Operating cost  
- Total expense  
- Profit  
- Profit per mile  
- All-in RPM  

---

### 💡 Profit Optimization

- Flags bad loads instantly  
- Suggests negotiation opportunities  
- Highlights strong and elite loads  

---

## 🖥️ How to Run

```bash
pip install streamlit
streamlit run app_ui.py
