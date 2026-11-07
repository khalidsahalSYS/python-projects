# Python Projects

This repository has been converted into a Django-based website page checker project.

## Features
- Check whether a public website URL loads successfully
- Display the HTTP status code
- Measure response time
- Extract the page title, main heading, and meta description
- Simple and clean UI for testing pages

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Django server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Open the app in the browser:
   ```text
   http://127.0.0.1:8000/
   ```

## Example URL to test
- https://example.com
- https://www.python.org

## Project structure
- `manage.py` - Django entry point
- `pagechecker_project/` - project configuration
- `pagechecker_app/` - URL checking logic and views
- `templates/pagechecker/home.html` - UI template
