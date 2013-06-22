TODO
====

* Create a forgot password form/mechanism
* Allow users to log in via Google, Facebook
* Create a simple 404/other code error page
* Implement "remember me" in login forms
* The authorization page should focus correctly
* Is there a way to merge /auth and /register?
* Add location data to user/pin
* Think about pin edit rights, follow/unfollow on behalf of pin
* Add a creation date to connections (is there an abstract model which does that?)
* Add url access to pin tabs
* On tab move change url without reloading
* In user/pin profile, clicking on follow stats should open the connections tab
* Replace the "Log out" button in the navbar with a profile menu
* Remove url tabs persistence code for user.html/pin.html
* Pin/user tabs should use AJAX
* Make navbar thinner, change the size of user-image-small
* Navbar dropdown should appear on hover
* Decrease ```@navbarHeight``` and recompile bootstrap-cosmo
* Redo the connections tab with actions stream app
* Update the follow/unfollow button in the pins page

Lower priority tasks
====================

* Login form(s) should not post unless text is present in both fields
* Should the navbar login form should use Django forms?
* When the browser window is narrow, there is some white space above the navbar
* When the browser window is narrow, the auth page behaves strangely
* Insert check for active user when logging in
* What characters are allowed in a username/does this conform with the url standard
* Enforce email uniqueness for users
* Convert url tag to Django 1.5 standard (see [this](http://nomulous.com/blog/easily-adopt-djangos-new-url-template-syntax/))
* Figure out a way to deal with UserProfiles in admin interface (Connection's GenericRelations do not work well with inlines)
* Add a connection block mechanism
* Follow/unfollow button position in user pane
* Get login/logout/signin/signout wording consistent
* Use abstract methods in ConnectionEnd
* Add @autostrip to registration form
* Customize follow/unfollow messages, check for correctness before adding a message
* Add caching, use ```django-cache-utils```
* Add Dajax support
* Change color of logout text to be darker

Issues
======

* Migrating users to south gave some errors; investigate this

Longterm tasks
==============

* Allow users to log in with an email (this involves ensuring email uniqueness, and using a custon authentication backend)
* Theme bootstrap (see [Cerulean](http://bootswatch.com/cerulean/) and [Spruce](http://bootswatch.com/spruce/)); the current theme looks similar to Facebook
* Convert user profile to Django 1.5 once packages are released for Debian/Ububuntu
* Template ```{% url %}``` syntax changed from Django 1.4 to 1.5; we need to add quotations around view names when upgrading
* Implement user profile privacy settings (public, private, etc.)
* Decide on responsive vs fixed interface

Deployment tasks
================

* Change SECRET_KEY in ```settings.py```
* Compile/minify bootstrap
