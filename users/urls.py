from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login$', 'users.views.login', name='login'),
    url(r'^logout$', 'users.views.logout', name='logout'),
    url(r'^auth$', 'users.views.auth', name='auth'),

    url(r'^u/(?P<username>\w+)', 'users.views.user', name='user')
)
