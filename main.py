from analysis import load_data, get_summary, print_report
from visualization import create_all_charts


def main():
    print("Personal Finance & Expense Analytics")
    print("Loading transactions...")
    transactions = load_data()
    summary = get_summary(transactions)
    print_report(transactions, summary)
    create_all_charts(summary)


if __name__ == "__main__":
    main()
