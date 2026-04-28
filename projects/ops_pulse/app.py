from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
import csv
from datetime import datetime

app = Flask(__name__)

DATA_FILE = Path(__file__).resolve().parent / "data" / "tasks.csv"
FIELDNAMES = ["title", "owner", "due_date", "category", "status", "budget", "notes", "created_at"]
STATUS_OPTIONS = ["Not Started", "In Progress", "Completed", "Overdue"]
CATEGORY_OPTIONS = ["Operations", "Budget", "Logistics", "Communications", "Events", "Other"]


def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_tasks():
    ensure_data_file()
    tasks = []
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["budget"] = format_budget(row.get("budget"))
            row["status"] = mark_overdue(row)
            tasks.append(row)
    return tasks


def save_tasks(tasks):
    ensure_data_file()
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for task in tasks:
            row = {**task, "budget": f"{format_budget(task.get('budget')):.2f}"}
            writer.writerow(row)


def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def format_budget(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def mark_overdue(task):
    due_date = parse_date(task.get("due_date"))
    if due_date and due_date < datetime.today().date() and task.get("status") != "Completed":
        return "Overdue"
    return task.get("status", "Not Started")


def compute_metrics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task.get("status") == "Completed")
    overdue = sum(1 for task in tasks if task.get("status") == "Overdue")
    total_budget = sum(task.get("budget", 0) for task in tasks)
    completion_rate = round((completed / total * 100), 1) if total else 0.0
    return {
        "total": total,
        "completed": completed,
        "overdue": overdue,
        "completion_rate": completion_rate,
        "total_budget": total_budget,
    }


@app.route("/")
def dashboard():
    tasks = load_tasks()
    metrics = compute_metrics(tasks)
    return render_template(
        "dashboard.html",
        tasks=tasks,
        metrics=metrics,
        statuses=STATUS_OPTIONS,
        categories=CATEGORY_OPTIONS,
    )


@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    title = request.form.get("title", "").strip()
    owner = request.form.get("owner", "").strip()
    due_date = request.form.get("due_date", "")
    category = request.form.get("category", "Other")
    status = request.form.get("status", "Not Started")
    budget = request.form.get("budget", "0.00")
    notes = request.form.get("notes", "").strip()

    if title:
        tasks.append({
            "title": title,
            "owner": owner,
            "due_date": due_date,
            "category": category if category in CATEGORY_OPTIONS else "Other",
            "status": status if status in STATUS_OPTIONS else "Not Started",
            "budget": format_budget(budget),
            "notes": notes,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        save_tasks(tasks)

    return redirect(url_for("dashboard"))


@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
