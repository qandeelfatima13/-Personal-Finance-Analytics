# Personal Finance & Expense Analytics

A Python data-analysis project that explores a sample personal-finance dataset and summarizes income, expenses, net savings, monthly trends, and expense categories. It creates four visualizations using Pandas and Matplotlib.


## Features
- Loads and cleans transaction data from CSV
- Calculates total income, total expenses, net savings, and savings rate
- Summarizes expense totals by category
- Compares monthly income and expenses
- Generates charts for monthly totals, category totals, category shares, and net savings

## Technology Stack
- Python
- Pandas
- Matplotlib

## Folder Structure
```text
Personal_Finance_Analytics/
├── data/
│   └── transactions.csv
├── images/
│   └── charts/          # Generated charts are saved here
├── analysis.py
├── visualization.py
├── main.py
├── requirements.txt
└── README.md
```

## Run the Project
1. Install Python 3.
2. Open this project folder in VS Code or a terminal.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python main.py
   ```
The report prints in the terminal and charts are generated in `images/charts/`.

## Dataset
`data/transactions.csv` contains fictional sample transactions for 2025. The dataset is for demonstration and learning, not financial advice or real personal records.
