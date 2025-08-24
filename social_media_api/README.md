# Social Media API (Starter)


This is the initial scaffolding for a Social Media API using Django and Django REST Framework with Token Authentication.


## Requirements
- Python 3.10+
- Django 5
- Django REST Framework
- Pillow (for image uploads)


## Setup


```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# macOS/Linux
# source venv/bin/activate


pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver