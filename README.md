# 💰 Personal Finance Tracker

A command-line Python application to track your personal finances — income, expenses by category, and monthly budgets.

Built collaboratively as part of the **Jedha Bootcamp** Full Stack program.

---

## 📋 Features

- **Income tracking** — record and accumulate monthly income
- **Expense tracking** — log expenses by category (Food, Rent, Transport, etc.)
- **Budget planner** — set monthly budgets per category
- **Budget status** — compare spending vs. budget with overspend alerts
- **Persistent storage** — data saved locally in `data.json`

---

## 🗂️ Project Structure

```
personal-finance_tracker/
├── finance_tracker.py          # Main CLI entry point (income + menu)
├── finance_tracker_depenses.py # Expense tracker module (OOP)
├── budget.py                   # Budget management (set & display)
├── data.json                   # Local data store (auto-generated)
└── .gitignore
```

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/vinceslater-dotcom/personal-finance_tracker.git
cd personal-finance_tracker

# Run the app
python finance_tracker.py
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

- Python 3.x — standard library only (no external dependencies)
- JSON for local data persistence

---

## 👥 Contributors

Collaborative project — contributions from multiple Jedha Bootcamp students.
