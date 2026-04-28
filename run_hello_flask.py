import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FLASK_APP_DIR = ROOT / "hello flask"

# Ensure the Flask app folder is imported before the root app.py
sys.path.insert(0, str(FLASK_APP_DIR))

try:
    from app import app
except Exception as exc:
    raise RuntimeError(
        "Unable to import the Flask app from 'hello flask/app.py'. "
        "Run this script from the repository root and ensure the folder exists."
    ) from exc

if __name__ == "__main__":
    app.run(debug=True)
