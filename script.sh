#!/bin/bash
apt-get install pip
pip install -r requirement.txt
python manage.py makemigrations accounts
python manage.py sqlmigrate accounts 0001
python manage.py migrate
python -mwebbrowser http://127.0.0.1:8000