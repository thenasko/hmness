hmness
======

The Homeness Project

Introduction
------------

(TODO: Add a description of the goals and ideas behind this project.)

Technical setup
---------------

The current prerequisites of the project are
* git
* python-sqlite (or other database engine)
* python-pip
* python-django
* python-django-south
* python-django-dajaxice, python-django-dajax
* django-bootstrap-toolkit (to install use ```pip install django-bootstrap-toolkit```)
* django-annoying (to install use ```pip install django-annoying```)
* django-jsonfield (to install use ```pip install django-jsonfield```)
* django-activity-stream (to install use ```pip install django-activity-stream```)

Use the following command to check out the repository.

```
git clone https://github.com/thenasko/hmness.git hmness-project
```

To start the application change to `hmness-project/hmness` and run
```
python manage.py runserver
```
You can then direct your browser to `localhost:8000`. If you are using a remote machine, add `0.0.0.0:8000` at the end of the command above to allow external access.

This repository includes a sample database. To access the administrator features use username ```admin``` and password ```test```.

(TODO: Write a brief note on setting up a testing/development environment.)

See [our TODO list](TODO.md) for tasks we would like to accomplish.
