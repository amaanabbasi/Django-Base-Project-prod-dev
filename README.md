# Gimmko

- [x] Users: Candidate, Recruiter, Superuser
- [x] Superuser can add a recruiter
- [x] Signup and login for Recruiter
- [x] Candidate Profile view
- [x] Email verification (Need Simple email service to create the backend)
- [x] Document singnature, email notification (Need Simple email service to create the backend)


## Frontend Dev

Dashboard, accounts, home, these are three apps each of them contains their own templates folder and a static folder.
The mysite directory also has a templates and static folder which is a global to all the the other apps mentioned before.

## Setup and Installation

### Pre-requisites
- Python3
- clone the project

Mac/Linux users
- cd Gimmko
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage-dev.py runserver 8000
- http://localhost:8000
