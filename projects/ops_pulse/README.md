# OpsPulse

OpsPulse is a beginner-friendly Flask app for student leaders and small teams to track operations tasks, deadlines, budgets, and progress.

## What it does
- Add tasks with title, owner, due date, category, status, budget, and notes
- View all tasks in a dashboard table
- See summary metrics for total tasks, overdue tasks, completion rate, and total budget
- Delete tasks from the table
- Store task data in a CSV file for the MVP

## Setup
1. Open a terminal in `projects/ops_pulse`
2. Install Flask if needed:
   ```bash
   pip install flask
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open the browser at `http://127.0.0.1:5000`

## Files
- `app.py` — Flask routes, CSV persistence, and dashboard logic
- `templates/` — Jinja HTML templates
- `static/style.css` — additional app styling
- `data/tasks.csv` — stored task data

## Notes
- The app uses a simple CSV file in `data/tasks.csv`.
- Overdue tasks automatically update after the due date.
- The dashboard is built with Bootstrap and simple Python code.
