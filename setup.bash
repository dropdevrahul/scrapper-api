#!/bin/bash
echo "Installing Virtualenv"

pip install virtualenv


echo "Making a new Virtual environment in venv folder"
virtualenv venv

. env/bin/source

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

echo "Creating default User"
python manage.py createsuperuser


python manage.py runserver
