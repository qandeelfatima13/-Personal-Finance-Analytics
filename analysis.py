import pandas as pd

from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "transactions.csv"


def load_data():
    """Load, validate, and clean the transactions dataset."""
    df = pd.read_csv(DATA_FILE)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Date", "Type", "Category", "Amount"])
    df = df[df["Amount"] > 0].copy()
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    df["MonthName"] = df["Date"].dt.strftime("%b")
    return df



def get_summary(df):
    income = df.loc[df["Type"] == "Income", "Amount"].sum()
    expenses = df.loc[df["Type"] == "Expense", "Amount"].sum()
    savings = income - expenses
    savings_rate = (savings / income * 100) if income else 0
    expense_df = df[df["Type"] == "Expense"]
    category_totals = expense_df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    monthly = df.pivot_table(index="Month", columns="Type", values="Amount", aggfunc="sum", fill_value=0)
    monthly = monthly.sort_index()
    return {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "savings_rate": savings_rate,
        "category_totals": category_totals,
        "monthly": monthly,
        "expense_count": len(expense_df),
        "transaction_count": len(df),
    }


def print_report(df, summary):
    print("\n" + "=" * 58)
    print("       PERSONAL FINANCE & EXPENSE ANALYTICS REPORT")
    print("=" * 58)
    print(f"Total Income       : PKR {summary['income']:,.0f}")
    print(f"Total Expenses     : PKR {summary['expenses']:,.0f}")
    print(f"Net Savings       : PKR {summary['savings']:,.0f}")
    print(f"Savings Rate      : {summary['savings_rate']:.1f}%")
    print(f"Transactions      : {summary['transaction_count']}")
    print("\nTop Expense Categories:")
    print(summary["category_totals"].head(5).to_string())
    print("\nMonthly Totals:")
    print(summary["monthly"].to_string())
    if not summary["category_totals"].empty:
        top_category = summary["category_totals"].idxmax()
        top_amount = summary["category_totals"].max()
        print(f"\nHighest spending category: {top_category} (PKR {top_amount:,.0f})")
    print("\nReport completed. Charts are saved in images/charts/.\n")
