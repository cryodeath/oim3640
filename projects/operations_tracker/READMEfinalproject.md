# Operations Tracker

A Flask-based app for student leaders and small teams to log tasks, deadlines, budgets, and project progress in one place.

## What it does
- Add tasks with title, owner, due date, category, status, budget, and notes
- View a task dashboard with metrics for total tasks, overdue items, completion rate, and total budget
- Filter tasks by status and category
- Delete tasks and keep data in a JSON file

## Install and run
1. Open a terminal in `projects/operations_tracker`
2. Install Flask if needed:
   ```bash
   pip install flask
   ```
3. Run the app:
   ```bash
   python finalproject.py
   ```
4. Open `http://127.0.0.1:5000` in your browser

## Files
- `finalproject.py` — Flask app logic and task persistence
- `templates/` — HTML templates for the dashboard and form
- `static/style.css` — styling for the app
- `data/tasks.json` — stored task data
- `AI_USAGE.md` — documentation of AI usage

## Notes
- Tasks persist in `data/tasks.json`
- Due dates should be entered in the browser date picker format
- Overdue tasks are automatically highlighted after the due date passes
