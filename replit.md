# Doctor Scheduler

## Project Overview
This is a Django-based web application for scheduling doctors across different sections and blocks. The application helps manage doctor rosters, blocks (sections), and scheduling with features for handling vacation preferences and visit requirements.

## Purpose
The Doctor Scheduler application allows users to:
- Manage a roster of doctors with their year, specialty (IM status), and vacation preferences
- Create and manage blocks/sections with vacation types and visit limits
- Schedule doctors to different blocks based on their preferences and requirements
- Track job slots with year and specialty requirements

## Current State
- **Status**: Successfully imported and configured for Replit
- **Running**: Django development server on port 5000
- **Database**: SQLite3 with existing migrations applied
- **Frontend**: Bootstrap-based UI with HTMX for dynamic interactions

## Project Architecture

### Technology Stack
- **Backend**: Django 5.2.8 (Python web framework)
- **Database**: SQLite3 (file-based database)
- **Frontend**: Bootstrap CSS + HTMX for dynamic UI
- **Deployment**: Configured with Gunicorn for production

### Project Structure
```
Doctor_Scheduler/          # Django project configuration
├── settings.py           # Project settings (configured for Replit)
├── urls.py              # URL routing
├── wsgi.py              # WSGI application
└── asgi.py              # ASGI application

Main/                      # Main application
├── models.py            # Data models (Doctor, Section, JobSlot, etc.)
├── views.py             # View functions
├── forms.py             # Django forms
├── urls.py              # App URL routing
├── templates/           # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── home.html       # Homepage
│   ├── roster.html     # Doctor roster page
│   ├── block.html      # Blocks management page
│   ├── schedule.html   # Scheduling page
│   └── create_edit_block.html  # Block creation/editing
└── static/             # Static files
    ├── css/            # Bootstrap CSS
    └── js/             # Bootstrap & HTMX JavaScript

manage.py                  # Django management script
requirements.txt          # Python dependencies
db.sqlite3               # SQLite database
```

### Data Models
1. **Doctor**: Stores doctor information (name, year, IM status, wards left, vacation preferences)
2. **Section**: Blocks/sections with vacation types and visit limits
3. **DoctorBlockPreference**: Links doctors to their preferred sections
4. **JobSlot**: Defines available positions with year and specialty requirements

### Key Features
- Doctor roster management
- Block/section configuration with vacation types (Zero, 2+2, 5+2)
- Doctor preferences for block assignments
- Job slot requirements (year range, IM-only flag)

## Replit Configuration

### Development
- **Workflow**: Django Server runs on 0.0.0.0:5000
- **Settings**: ALLOWED_HOSTS set to '*' for Replit proxy
- **CSRF**: Trusted origins configured for *.replit.dev and *.repl.co

### Deployment
- **Type**: Autoscale deployment
- **Server**: Gunicorn WSGI server
- **Command**: `gunicorn --bind=0.0.0.0:5000 --reuse-port Doctor_Scheduler.wsgi:application`

## Recent Changes
- **2025-12-01**: Initial import from GitHub
  - Installed Python 3.11 and Django 5.2.8
  - Created requirements.txt with Django and Gunicorn
  - Updated settings.py for Replit environment (ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS)
  - Configured Django Server workflow on port 5000
  - Set up deployment configuration with Gunicorn
  - Created .gitignore for Python/Django projects
  - Verified application runs successfully

## Running the Application

### Development
The Django development server runs automatically via the "Django Server" workflow. Access the application through the Replit webview.

### Production Deployment
When you publish this Repl, it will use Gunicorn to serve the application in production mode.

## Database
The application uses SQLite3 with an existing database file (db.sqlite3). Migrations are already applied. The database contains the following tables:
- Doctors
- Sections (blocks)
- Doctor Block Preferences
- Job Slots
- Django admin tables

## Admin Access
To create a Django admin superuser, run:
```bash
python manage.py createsuperuser
```

Then access the admin panel at `/admin` to manage data through Django's built-in admin interface.
