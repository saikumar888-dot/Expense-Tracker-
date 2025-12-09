# Expense Tracker

A simple and interactive expense tracker application built with Streamlit.

## Features
- ➕ Add income and expense transactions
- 📊 View total income, expenses, and balance
- 📅 Track transactions by date
- 📥 Download transactions as CSV
- 🗑️ Clear all transactions

## Local Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/saikumar888-dot/Expense-Tracker-.git
cd Expense-Tracker-
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment on Streamlit Cloud

1. Push your code to GitHub (already done ✓)

2. Go to [Streamlit Cloud](https://share.streamlit.io/)

3. Click "New app"

4. Connect your GitHub account and select:
   - Repository: `saikumar888-dot/Expense-Tracker-`
   - Branch: `main`
   - Main file path: `app.py`

5. Click "Deploy"

Your app will be live at a URL like: `https://expense-tracker-<random>.streamlit.app/`

## Alternative: Deploy on Heroku (Paid)

1. Create a `Procfile`:
```
web: streamlit run app.py --logger.level=error
```

2. Push to GitHub and connect Heroku to your repository

3. Set buildpacks to Python

4. Deploy!

## Usage

1. Enter the date, amount, and transaction type (Income/Expense)
2. Click the "+" button to add the transaction
3. View your balance and transaction history
4. Download transactions as CSV if needed
5. Clear all transactions with the "Clear All" button

---
Built with ❤️ using Streamlit
