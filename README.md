QUOKKA: README
==============

Quokka is a social app for answering thought-provoking questions and reading others' responses. Answers can be voted up or down to bring the most interesting or valuable ones to the top.

Usage
-----

Assuming Python 2.7 and Django 1.7 installed:

* `git clone git@github.com:cassiebrooks/itech.git`
* `cd itech/tango_with_django_project/`
* `pip install django-registration-redux`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python populate_quokka.py` for one prepopulated set of answers, 3 sets, and 3 users
* `python manage.py createsuperuser` for access to the admin panel at /admin
* Run using `python manage.py runserver`
