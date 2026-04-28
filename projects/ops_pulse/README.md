# OpsPulse – Operations Tracker for Student Leaders

OpsPulse is a simple, beginner-friendly Flask web application that helps student leaders and small teams organize and track their operations work in one centralized place. Whether you're managing club events, project deadlines, team budgets, or leadership responsibilities, OpsPulse keeps everything organized.

## 📋 What OpsPulse Does

OpsPulse provides a clean, centralized dashboard where you can:

- **Add tasks** with detailed information: task title, owner name, due date, category, status, budget, and notes
- **View all tasks** in a searchable, easy-to-read table on the dashboard
- **Track task status** with four options: Not Started, In Progress, Completed, or Overdue
- **Monitor key metrics** at a glance: total task count, number of overdue items, completion rate (%), and total budget spent
- **Organize by category** including Operations, Budget, Logistics, Communications, Events, and more
- **Delete tasks** when they're no longer needed
- **Persist all data** automatically in a simple CSV file (no database required)
- **Automatically detect overdue tasks** based on the due date you entered

### Why OpsPulse?

If you're juggling multiple projects, events, or leadership roles, you know how easy it is to lose track of deadlines and responsibilities. OpsPulse solves this by giving you one place to log everything – no more scattered notes, emails, or spreadsheets.

## 🚀 Getting Started

### Prerequisites

Before you start, make sure you have:

- **Python 3.7 or later** installed on your computer
- **Git** (to clone the repository, optional)
- A text editor or IDE like VS Code

To check if Python is installed, open a terminal and run:
```bash
python --version
```

### Installation & Setup

1. **Clone or download the repository:**
   ```bash
   git clone <repository-url>
   cd oim3640/projects/ops_pulse
   ```
   OR just download the `ops_pulse` folder.

2. **Install Flask** (the web framework OpsPulse uses):
   ```bash
   pip install flask
   ```
   
   If you get a "command not found" error, try:
   ```bash
   python -m pip install flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   
   You should see output like:
   ```
   * Running on http://127.0.0.1:5000
   ```

4. **Open your web browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

   The OpsPulse dashboard will load in your browser!

### Stopping the App

To stop the Flask development server, press **Ctrl+C** in your terminal.

## 📖 How to Use

### Adding a Task

1. On the dashboard, scroll to the **"Add a task"** form on the right side
2. Fill in the fields:
   - **Task title** (required) – what needs to be done
   - **Owner** – who is responsible (optional)
   - **Due date** – when it needs to be done (click the calendar icon)
   - **Category** – pick from Operations, Budget, Logistics, Communications, Events, or Other
   - **Status** – choose Not Started, In Progress, Completed, or Overdue
   - **Budget ($)** – how much money is allocated (optional, default is $0.00)
   - **Short notes** – any additional details or context
3. Click **"Save task"** – your task will appear in the table immediately

### Viewing Your Tasks

- The **dashboard table** shows all your tasks with columns for title, owner, due date, category, status, budget, and notes
- **Metric boxes** at the top show:
  - Total tasks added
  - Number of overdue tasks
  - Completion rate (completed ÷ total × 100%)
  - Total budget allocated

### Deleting a Task

- In the task table, find the row with the task you want to remove
- Click the red **"Delete"** button at the end of that row
- The task will be removed immediately

### Understanding Task Status Colors

- **Red highlighting** = Overdue task (due date has passed and status is not Completed)
- **Green highlighting** = Completed task
- **No highlighting** = Not Started or In Progress

## 📁 File Structure

```
ops_pulse/
├── app.py                  # Main Flask application with routes and logic
├── templates/
│   ├── base.html          # Base HTML template (header, footer, navigation)
│   └── dashboard.html     # Dashboard page with task table and form
├── static/
│   └── style.css          # Custom styling for the app
├── data/
│   └── tasks.csv          # CSV file where task data is stored
└── README.md              # This file
```

## 🔍 Understanding the Code

### app.py
- Contains Flask routes (`/` for dashboard, `/add` for adding tasks, `/delete` for removing tasks)
- Handles reading and writing to the CSV file
- Calculates metrics like completion rate and total budget
- Marks tasks as overdue automatically

### templates/base.html
- Provides the overall page layout (header, footer, navigation)
- Other pages extend this template for consistency

### templates/dashboard.html
- Main page users interact with
- Shows the task table, metrics, and the "Add a task" form
- Uses Bootstrap for styling and responsive design

### static/style.css
- Custom styling to make the app look clean and professional
- Overrides Bootstrap defaults where needed

### data/tasks.csv
- Stores all task data in a simple comma-separated format
- Automatically created when you first run the app
- Can be opened in Excel or any text editor

## 🛠️ Troubleshooting

### "Flask is not installed" or "ModuleNotFoundError: No module named 'flask'"

**Solution:** Install Flask using pip:
```bash
pip install flask
```

### "Address already in use" or "Port 5000 is already in use"

**Solution:** Another app is using port 5000. Either:
- Stop the other app first, OR
- Modify `app.py` line 146 to use a different port:
  ```python
  app.run(debug=True, port=5001)
  ```

### Tasks don't appear after I add them

**Solution:** Check that the `data/` folder exists in the `ops_pulse` directory. The app should create it automatically, but if not:
1. Create a folder named `data` in the `ops_pulse` directory
2. Restart the Flask app by pressing Ctrl+C and running `python app.py` again

### The page looks broken or CSS isn't loading

**Solution:** 
1. Hard refresh your browser: press **Ctrl+Shift+R** (or **Cmd+Shift+R** on Mac)
2. Make sure both `templates/` and `static/` folders exist in the `ops_pulse` directory

### Tasks don't show as overdue even though the due date has passed

**Solution:** Overdue status is calculated when you view the dashboard. It compares the due date to today's date. Make sure your computer's date and time are set correctly.

## 📚 Technologies Used

- **Python 3** – programming language
- **Flask** – lightweight web framework
- **Jinja2** – templating engine (built into Flask)
- **Bootstrap 5** – responsive UI framework
- **CSV** – simple file-based data storage

## 🎯 Future Enhancements

Ideas for extending OpsPulse:

- Edit existing tasks (not just delete)
- Search or filter tasks by keyword or category
- Export tasks to PDF or Excel
- User accounts and authentication
- Data visualization (charts showing budget spend, completion trends)
- Email reminders for approaching deadlines
- Sorting by due date, budget, or owner
- Dark mode theme

## 📝 Notes

- Data is saved locally in `data/tasks.csv` – no internet connection required
- This is a development version (debug mode is enabled) – for production, set `debug=False` in `app.py`
- All task data is stored on your computer; it's not sent anywhere
- The app is designed to be simple and beginner-friendly – no complex features or external dependencies

## 🤝 Questions or Issues?

If you encounter any problems:
1. Check the Troubleshooting section above
2. Make sure Flask is installed: `pip install flask`
3. Verify all folders (`templates/`, `static/`, `data/`) exist
4. Check that you're running the latest version of the code

---

**Happy tracking! 📊**
