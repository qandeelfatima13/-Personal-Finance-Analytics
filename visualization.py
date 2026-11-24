from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

CHART_DIR = Path(__file__).parent / "images" / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

NAVY = "#14243A"
GOLD = "#D8B24C"
GREEN = "#45B37A"
CORAL = "#E77B6B"
PALETTE = ["#D8B24C", "#45B37A", "#E77B6B", "#6CA6CD", "#9675B8", "#D58E58", "#65B7B2", "#A6B56B"]


def style_axes(ax, title):
    ax.set_title(title, fontsize=14, fontweight="bold", color=NAVY, pad=14)
    ax.set_facecolor("#FFFFFF")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#D9E1E8")
    ax.spines["bottom"].set_color("#D9E1E8")
    ax.tick_params(colors="#586779")
    ax.grid(axis="y", linestyle="--", alpha=0.25)
    ax.set_axisbelow(True)


def save_monthly_chart(summary):
    monthly = summary["monthly"]
    fig, ax = plt.subplots(figsize=(10, 5.5))
    months = monthly.index
    income = monthly.get("Income", [0] * len(months))
    expenses = monthly.get("Expense", [0] * len(months))
    ax.plot(months, income, marker="o", linewidth=2.8, color=GREEN, label="Income")
    ax.plot(months, expenses, marker="o", linewidth=2.8, color=CORAL, label="Expenses")
    style_axes(ax, "Monthly Income vs Expenses")
    ax.set_ylabel("Amount (PKR)")
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax.legend(frameon=False)
    plt.xticks(rotation=35, ha="right")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "monthly_income_expenses.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_category_chart(summary):
    categories = summary["category_totals"]
    fig, ax = plt.subplots(figsize=(9, 6))
    if not categories.empty:
        ax.bar(categories.index, categories.values, color=PALETTE[:len(categories)], width=0.72)
    style_axes(ax, "Expenses by Category")
    ax.set_ylabel("Amount (PKR)")
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "expenses_by_category.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_category_pie(summary):
    categories = summary["category_totals"]
    fig, ax = plt.subplots(figsize=(8, 7))
    if not categories.empty:
        ax.pie(categories.values, labels=categories.index, autopct="%1.1f%%", startangle=90,
               colors=PALETTE[:len(categories)], wedgeprops={"linewidth": 1, "edgecolor": "white"})
    ax.set_title("Expense Share by Category", fontsize=14, fontweight="bold", color=NAVY, pad=14)
    ax.axis("equal")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "expense_category_share.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def save_savings_chart(summary):
    monthly = summary["monthly"].copy()
    if "Income" not in monthly:
        monthly["Income"] = 0
    if "Expense" not in monthly:
        monthly["Expense"] = 0
    monthly["Net"] = monthly["Income"] - monthly["Expense"]
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.bar(monthly.index, monthly["Net"], color=GREEN, width=0.7)
    style_axes(ax, "Monthly Net Savings")
    ax.set_ylabel("Amount (PKR)")
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    plt.xticks(rotation=35, ha="right")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "monthly_net_savings.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def create_all_charts(summary):
    save_monthly_chart(summary)
    save_category_chart(summary)
    save_category_pie(summary)
    save_savings_chart(summary)
    print(f"Charts saved to: {CHART_DIR}")
