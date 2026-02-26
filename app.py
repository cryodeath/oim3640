import streamlit as st
import json
import os
from collections import defaultdict
from datetime import datetime

# ----------------------------------
# sample data to show on first load
SAMPLE_EXPENSES = {
    "2026-03-15": [
        {"category": "Food", "amount": 120, "desc": "Dinner"},
        {"category": "Transport", "amount": 167, "desc": "Airport taxi"}
    ]
}

# -----------------------
# utility functions

def load_trip(trip_name: str) -> dict:
    """Load a trip JSON from disk. If the file does not exist
    return a fresh structure including sample data for the first
    visit. The returned dictionary always contains keys "name"
    and "expenses".
    """
    filename = f"{trip_name}.json"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    # new trip, give sample expenses so UI isn't empty
    return {"name": trip_name, "expenses": SAMPLE_EXPENSES.copy()}


def save_trip(trip: dict, trip_name: str) -> None:
    """Persist a trip dictionary to `{trip_name}.json`. Overwrites
    existing file.  """
    filename = f"{trip_name}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(trip, f, indent=2)


def add_expense(trip: dict, date: str, cat: str, amt: float, desc: str) -> None:
    """Append a single expense record to the trip and auto‑save."""
    if date not in trip["expenses"]:
        trip["expenses"][date] = []
    trip["expenses"][date].append({"category": cat, "amount": amt, "desc": desc})
    # save immediately
    save_trip(trip, trip["name"])


def daily_total(trip: dict, date: str) -> float:
    """Return total amount spent on a given date."""
    return sum(e["amount"] for e in trip["expenses"].get(date, []))


def category_totals(trip: dict) -> dict:
    """Return a mapping of category -> total amount across all days."""
    totals = defaultdict(float)
    for lst in trip["expenses"].values():
        for e in lst:
            totals[e["category"]] += e["amount"]
    return totals

# -----------------------
# Streamlit application logic

st.set_page_config(page_title="Travel Cost Tracker", layout="wide")
st.title("🧾 Travel Cost Tracker")
# initial guidance for the user
st.markdown("""
Enter or create a trip name in the box below.\
An existing file will be loaded automatically; a new trip starts with sample data.\
Use the form on the left to add expenses, then see summaries in the center and right columns.
"""
)

# use session state to remember loaded trip
if "trip" not in st.session_state:
    st.session_state.trip = None

# --- trip selection / load ---
col0 = st.columns(1)[0]
with col0:
    # explain what this box does
    trip_name = st.text_input(
        "Trip Name:",
        value="Paris 2026",
        help="Type a name for your trip; data is saved to `<name>.json`."
    ).strip()
    if trip_name:
        if st.session_state.trip is None or st.session_state.trip.get("name") != trip_name:
            st.session_state.trip = load_trip(trip_name)
    if trip_name and st.session_state.trip:
        st.info(f"Loaded trip '{trip_name}' with {len(st.session_state.trip['expenses'])} day(s) of data.")

trip = st.session_state.trip
if trip is None:
    st.warning("Enter a trip name above and press Enter to load or start a new trip.")
    st.stop()

# three column layout
col1, col2, col3 = st.columns(3)

# --- left: add expense form ---
with col1:
    st.subheader("➕ Add Expense")
    st.info("Fill in each field below and hit **Add Expense**; the trip file will auto-save.")
    date_val = st.date_input("Date:", value=datetime.today(), help="Select the date for this expense.")
    cat_val = st.text_input("Category:", placeholder="e.g. Food, Transport", help="Expense category (required)")
    amt_val = st.number_input("Amount ($):", min_value=0.0, format="%.2f", help="How much was spent")
    desc_val = st.text_input("Desc:", placeholder="Short description of purchase")
    if st.button("Add Expense"):
        if not cat_val:
            st.warning("Please provide a category before adding.")
        else:
            iso_date = date_val.isoformat()
            add_expense(trip, iso_date, cat_val, amt_val, desc_val)
            st.experimental_rerun()

# --- center: daily breakdown ---
with col2:
    st.subheader("📅 Daily Breakdown")
    for date in sorted(trip["expenses"].keys()):
        total = daily_total(trip, date)
        entries = trip["expenses"][date]
        header = f"{datetime.fromisoformat(date).strftime('%b %d, %Y')}: ${total:.2f} ({len(entries)} expenses)"
        st.markdown(f"**{header}**")
        for e in entries:
            st.write(f"- {e['category']}: ${e['amount']:.2f} - {e['desc']}")
        st.write("---")

# --- right: category summary ---
with col3:
    st.subheader("📊 Category Summary")
    totals = category_totals(trip)
    grand = sum(totals.values())
    days = len(trip["expenses"])
    avg = grand / days if days else 0
    st.metric("Total", f"${grand:.2f}")
    st.metric("Avg Daily", f"${avg:.2f}")
    # sort by amount descending
    for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):
        pct = (amt / grand * 100) if grand else 0
        icon = {
            "Food": "🥐",
            "Transport": "🚕",
            "Hotel": "🏨",
            "Activities": "🎨"
        }.get(cat, "")
        st.write(f"{cat}: ${amt:.2f} ({pct:.0f}%) {icon}")

# done

