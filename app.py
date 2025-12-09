import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Expense Tracker", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS
st.markdown("""
    <style>
        .header {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 2rem;
            color: #333;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 1.5rem;
            border-radius: 0.5rem;
            text-align: center;
        }
        .income {
            color: #28a745;
        }
        .expense {
            color: #dc3545;
        }
        .balance {
            color: #007bff;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# Header
st.markdown('<div class="header">💰 Expense Tracker</div>', unsafe_allow_html=True)

# Input form
st.subheader("Add Transaction")
col1, col2, col3, col4 = st.columns(4)

with col1:
    transaction_date = st.date_input("Date", value=datetime.now())

with col2:
    amount = st.number_input("Amount", min_value=0.0, step=0.01)

with col3:
    transaction_type = st.selectbox("Transaction Type", ["Income", "Expense"])

with col4:
    st.write("")
    st.write("")
    if st.button("+ Add", use_container_width=True):
        if amount > 0:
            st.session_state.transactions.append({
                "Date": transaction_date,
                "Amount": amount,
                "Type": transaction_type
            })
            st.success(f"{transaction_type} of ${amount:.2f} added!")
        else:
            st.error("Please enter a valid amount")

# Calculate totals
total_income = sum(t["Amount"] for t in st.session_state.transactions if t["Type"] == "Income")
total_expense = sum(t["Amount"] for t in st.session_state.transactions if t["Type"] == "Expense")
balance = total_income - total_expense

# Display metrics
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <p style="font-size: 0.9rem; color: #666;">Total Income</p>
            <p class="income" style="font-size: 2rem; margin: 0;">💵 ${total_income:.2f}</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <p style="font-size: 0.9rem; color: #666;">Total Expense</p>
            <p class="expense" style="font-size: 2rem; margin: 0;">💸 ${total_expense:.2f}</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <p style="font-size: 0.9rem; color: #666;">Balance</p>
            <p class="balance" style="font-size: 2rem; margin: 0;">💰 ${balance:.2f}</p>
        </div>
    """, unsafe_allow_html=True)

# Display transactions table
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Transactions")

if st.session_state.transactions:
    df = pd.DataFrame(st.session_state.transactions)
    df = df.sort_values('Date', ascending=False)
    
    # Display table
    st.dataframe(
        df[['Date', 'Amount', 'Type']].rename(
            columns={'Date': 'Transaction Date', 'Amount': 'Amount ($)', 'Type': 'Transaction Type'}
        ),
        use_container_width=True,
        hide_index=True
    )
    
    # Delete transaction
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🗑️ Clear All", use_container_width=True):
            st.session_state.transactions = []
            st.rerun()
else:
    st.info("No transactions yet. Add one to get started!")

# Download option
if st.session_state.transactions:
    st.markdown("<br>", unsafe_allow_html=True)
    df_download = pd.DataFrame(st.session_state.transactions)
    csv = df_download.to_csv(index=False)
    st.download_button(
        label="📥 Download Transactions (CSV)",
        data=csv,
        file_name="transactions.csv",
        mime="text/csv"
    )
