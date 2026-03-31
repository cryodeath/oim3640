"""
Travel Spending Tracker
=======================
A simple terminal app to log and analyze your travel expenses.
Tracks spending by date and category, saves trips to JSON.
"""

import json
import os
from datetime import datetime


# ─── Data Structure ──────────────────────────────────────────────────────────
# Each trip is a dictionary:
# {
#     "trip_name": "Colombia March 2026",
#     "expenses": [
#         {"date": "2026-03-14", "category": "Food", "amount": 12.50, "description": "Street arepa"},
#         ...
#     ]
# }

CATEGORIES = ["Food", "Hotel", "Transport", "Activities", "Other"]
DATA_DIR = "trips"


# ─── File I/O ────────────────────────────────────────────────────────────────

def ensure_data_dir():
    """Create the trips folder if it doesn't exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def save_trip(trip):
    """Save a trip dictionary to a JSON file."""
    ensure_data_dir()
    filename = os.path.join(DATA_DIR, trip["trip_name"].replace(" ", "_") + ".json")
    with open(filename, "w") as f:
        json.dump(trip, f, indent=2)
    print(f"\n  Saved to {filename}")


def load_trip(filepath):
    """Load a trip dictionary from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)


def list_saved_trips():
    """Return a list of saved trip file paths."""
    ensure_data_dir()
    files = [
        os.path.join(DATA_DIR, f)
        for f in os.listdir(DATA_DIR)
        if f.endswith(".json")
    ]
    return sorted(files)


# ─── Input Helpers ───────────────────────────────────────────────────────────

def get_positive_float(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value <= 0:
                print("  Please enter a positive number.")
                continue
            return round(value, 2)
        except ValueError:
            print("  That's not a valid number. Try again.")


def get_date(prompt):
    """Keep asking until the user enters a valid date in YYYY-MM-DD format."""
    while True:
        raw = input(prompt).strip()
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        except ValueError:
            print("  Invalid date. Use YYYY-MM-DD format (e.g., 2026-03-14).")


def get_category():
    """Display category menu and return a valid choice."""
    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")
    while True:
        raw = input("  Pick a category (1-5): ").strip()
        try:
            choice = int(raw)
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            else:
                print(f"  Enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("  Enter a number.")


# ─── Core Features ───────────────────────────────────────────────────────────

def add_expense(trip):
    """Prompt the user for expense details and add it to the trip."""
    print("\n--- Add Expense ---")
    date = get_date("  Date (YYYY-MM-DD): ")
    category = get_category()
    amount = get_positive_float("  Amount ($): ")
    description = input("  Description: ").strip()
    if not description:
        description = "(no description)"

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }
    trip["expenses"].append(expense)
    print(f"\n  Added: {date} | {category} | ${amount:.2f} | {description}")


def view_daily_summary(trip):
    """Show expenses grouped by date with daily totals."""
    expenses = trip["expenses"]
    if not expenses:
        print("\n  No expenses recorded yet.")
        return

    # Group by date
    daily = {}
    for exp in expenses:
        day = exp["date"]
        if day not in daily:
            daily[day] = []
        daily[day].append(exp)

    print("\n--- Daily Summary ---")
    for day in sorted(daily.keys()):
        items = daily[day]
        total = sum(e["amount"] for e in items)
        print(f"\n  {day}  —  ${total:.2f}  ({len(items)} expense{'s' if len(items) != 1 else ''})")
        for e in items:
            print(f"    ${e['amount']:>8.2f}  {e['category']:<12} {e['description']}")


def view_category_summary(trip):
    """Show spending broken down by category with percentages."""
    expenses = trip["expenses"]
    if not expenses:
        print("\n  No expenses recorded yet.")
        return

    # Sum by category
    cat_totals = {}
    for exp in expenses:
        cat = exp["category"]
        cat_totals[cat] = cat_totals.get(cat, 0) + exp["amount"]

    grand_total = sum(cat_totals.values())

    print("\n--- Category Summary ---")
    print(f"  {'Category':<14} {'Amount':>10} {'Percent':>8}")
    print(f"  {'-'*34}")
    for cat in CATEGORIES:
        if cat in cat_totals:
            amt = cat_totals[cat]
            pct = (amt / grand_total) * 100
            bar = "█" * int(pct / 5)  # simple visual bar
            print(f"  {cat:<14} ${amt:>9.2f} {pct:>6.1f}%  {bar}")
    print(f"  {'-'*34}")
    print(f"  {'TOTAL':<14} ${grand_total:>9.2f}")


def view_trip_overview(trip):
    """Show high-level trip stats."""
    expenses = trip["expenses"]
    if not expenses:
        print("\n  No expenses recorded yet.")
        return

    total = sum(e["amount"] for e in expenses)
    dates = sorted(set(e["date"] for e in expenses))
    num_days = len(dates)
    avg_daily = total / num_days if num_days > 0 else 0
    biggest = max(expenses, key=lambda e: e["amount"])

    print("\n--- Trip Overview ---")
    print(f"  Trip name:        {trip['trip_name']}")
    print(f"  Total expenses:   {len(expenses)}")
    print(f"  Total spent:      ${total:.2f}")
    print(f"  Days tracked:     {num_days}")
    print(f"  Avg per day:      ${avg_daily:.2f}")
    print(f"  Biggest expense:  ${biggest['amount']:.2f} — {biggest['description']} ({biggest['date']})")


def delete_expense(trip):
    """Let the user remove an expense by number."""
    expenses = trip["expenses"]
    if not expenses:
        print("\n  No expenses to delete.")
        return

    print("\n--- Delete Expense ---")
    for i, e in enumerate(expenses, 1):
        print(f"  {i}. {e['date']} | {e['category']:<12} | ${e['amount']:>8.2f} | {e['description']}")

    while True:
        raw = input("\n  Enter expense number to delete (or 'c' to cancel): ").strip()
        if raw.lower() == "c":
            print("  Cancelled.")
            return
        try:
            idx = int(raw) - 1
            if 0 <= idx < len(expenses):
                removed = expenses.pop(idx)
                print(f"  Deleted: {removed['date']} | ${removed['amount']:.2f} | {removed['description']}")
                return
            else:
                print(f"  Enter a number between 1 and {len(expenses)}.")
        except ValueError:
            print("  Enter a number.")


# ─── Menu ────────────────────────────────────────────────────────────────────

def print_menu():
    """Display the main menu."""
    print("\n╔══════════════════════════════════╗")
    print("║   TRAVEL SPENDING TRACKER        ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Add expense                  ║")
    print("║  2. Daily summary                ║")
    print("║  3. Category summary             ║")
    print("║  4. Trip overview                ║")
    print("║  5. Delete an expense            ║")
    print("║  6. Save trip                    ║")
    print("║  7. Quit                         ║")
    print("╚══════════════════════════════════╝")


def start_or_load_trip():
    """Ask the user to start a new trip or load an existing one."""
    saved = list_saved_trips()

    print("\n" + "=" * 40)
    print("  TRAVEL SPENDING TRACKER")
    print("=" * 40)

    if saved:
        print("\n  Saved trips found:")
        for i, path in enumerate(saved, 1):
            name = os.path.basename(path).replace(".json", "").replace("_", " ")
            print(f"    {i}. {name}")
        print(f"    {len(saved) + 1}. Start a new trip")

        while True:
            raw = input("\n  Choose an option: ").strip()
            try:
                choice = int(raw)
                if 1 <= choice <= len(saved):
                    trip = load_trip(saved[choice - 1])
                    print(f"\n  Loaded: {trip['trip_name']}")
                    return trip
                elif choice == len(saved) + 1:
                    break  # fall through to new trip
                else:
                    print(f"  Enter a number between 1 and {len(saved) + 1}.")
            except ValueError:
                print("  Enter a number.")

    # New trip
    name = input("\n  Enter trip name (e.g., Colombia March 2026): ").strip()
    if not name:
        name = "My Trip"
    trip = {"trip_name": name, "expenses": []}
    print(f"\n  Created new trip: {name}")
    return trip


def main():
    """Main program loop."""
    trip = start_or_load_trip()

    while True:
        print_menu()
        choice = input("\n  Enter choice (1-7): ").strip()

        if choice == "1":
            add_expense(trip)
        elif choice == "2":
            view_daily_summary(trip)
        elif choice == "3":
            view_category_summary(trip)
        elif choice == "4":
            view_trip_overview(trip)
        elif choice == "5":
            delete_expense(trip)
        elif choice == "6":
            save_trip(trip)
        elif choice == "7":
            # Auto-save before quitting
            if trip["expenses"]:
                save = input("\n  Save before quitting? (y/n): ").strip().lower()
                if save == "y":
                    save_trip(trip)
            print("\n  Happy travels! 👋\n")
            break
        else:
            print("  Invalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()