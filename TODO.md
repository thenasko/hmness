TODO
====

* Write a basic database structure, add a few examples via the admin interface
* Extend the django user profile (see this [article](http://gistflow.com/posts/725-how-to-extend-the-behaviour-of-the-user-class-in-django-1-5))
* Create a fogot password form/mechanism
* Login view should redirect to the place it came from
* Allow users to log in via Google, Facebook
* Add [FontAwesome](http://fortawesome.github.io/Font-Awesome/) integration in order to access a wider set of icons in various sizes
* Create a simple 404/other code error page
* Implement "remember me" in login forms
* Implement the sign up form
* Add a sign up button in the navbar
* The authorization page should focus correctly
* The authorization page should pertain some data

Lower priority tasks
====================

* Login form(s) should not post unless text is present in both fields
* Should the navbar login form should use Django forms?

Issues
======

* Migrating users to south gave some errors; investigate this

Longterm tasks
==============

* Allow users to log in with an email (this involves ensuring email uniqueness, and using a custon authentication backend)
* Theme bootstrap (see [Cerulean](http://bootswatch.com/cerulean/) and [Spruce](http://bootswatch.com/spruce/))
* Convert user profile to Django 1.5 once packages are released for Debian/Ububuntu
* Template ```{% url %}``` syntax changed from Django 1.4 to 1.5; we need to add quotations around view names when upgrading

Deployment tasks
================

* Change SECRET_KEY in ```settings.py```
