

### Create a virtualenv to isolate our package dependencies locally
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

### Install Django and Django REST framework into the virtualenv
pip install django
pip install djangorestframework
pip install UnixDateTimeField
pip install jsonfield



python manage.py migrate
python manage.py makemigrations django_app
python manage.py migrate antipoaching


# RUN

python manage.py createsuperuser
python ./manage.py runserver


# TESTS

python manage.py test antipoaching
