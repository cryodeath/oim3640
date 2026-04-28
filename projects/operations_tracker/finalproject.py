from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = Path(__file__).resolve().parent / "data" / "tasks.json"
STATUS_OPTIONS = ["Not Started", "In Progress", "Completed", "Overdue"]
CATEGORY_OPTIONS = ["Operations", "Budget", "Logistics", "Communications", "Other"]


def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        save_tasks([])


def load_tasks():
    ensure_data_file()
    with DATA_FILE.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    for task in tasks:
        if task.get("status") != "Completed":
            task["status"] = mark_overdue(task)
    return tasks


def save_tasks(tasks):
    ensure_data_file()
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def parse_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def mark_overdue(task):
    due_date = parse_date(task.get("due_date"))
    if due_date and due_date < datetime.today().date():
        return "Overdue"
    return task.get("status", "Not Started")


def format_budget(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def compute_metrics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task.get("status") == "Completed")
    overdue = sum(1 for task in tasks if task.get("status") == "Overdue")
    total_budget = sum(format_budget(task.get("budget")) for task in tasks)
    completion_rate = round((completed / total * 100), 1) if total else 0.0
    return {
        "total": total,
        "completed": completed,
        "overdue": overdue,
        "completion_rate": completion_rate,
        "total_budget": total_budget,
    }


def filter_tasks(tasks, status_filter, category_filter):
    filtered = tasks
    if status_filter and status_filter != "All":
        filtered = [task for task in filtered if task.get("status") == status_filter]
    if category_filter and category_filter != "All":
        filtered = [task for task in filtered if task.get("category") == category_filter]
    return filtered


@app.route("/", methods=["GET"])
def index():
    status_filter = request.args.get("status", "All")
    category_filter = request.args.get("category", "All")
    tasks = load_tasks()
    filtered_tasks = filter_tasks(tasks, status_filter, category_filter)
    metrics = compute_metrics(tasks)
    categories = ["All"] + CATEGORY_OPTIONS
    statuses = ["All"] + STATUS_OPTIONS
    return render_template(
        "index.html",
        tasks=filtered_tasks,
        metrics=metrics,
        statuses=statuses,
        categories=categories,
        selected_status=status_filter,
        selected_category=category_filter,
    )


@app.route("/add", methods=["POST"])
def add_task():
    tasks = load_tasks()
    title = request.form.get("title", "").strip()
    owner = request.form.get("owner", "").strip()
    due_date = request.form.get("due_date", "")
    category = request.form.get("category", "Other")
    status = request.form.get("status", "Not Started")
    budget = request.form.get("budget", "0")
    notes = request.form.get("notes", "").strip()

    if not title:
        return redirect(url_for("index"))

    new_task = {
        "title": title,
        "owner": owner,
        "due_date": due_date,
        "category": category if category in CATEGORY_OPTIONS else "Other",
        "status": status if status in STATUS_OPTIONS else "Not Started",
        "budget": round(format_budget(budget), 2),
        "notes": notes,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
