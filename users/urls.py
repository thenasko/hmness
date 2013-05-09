from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^login$', 'users.views.login', name='login'),
    url(r'^signup$', 'users.views.signup', name='signup'),
    url(r'^logout$', 'users.views.logout', name='logout'),
    url(r'^register$', 'users.views.register', name='register'),
    url(r'^auth$', 'users.views.auth', name='auth'),
    
    url(r'^profile/(?P<username>\w+)$', 'users.views.user', name='user'),
    url(r'^profile/(?P<username>\w+)/activity$', 'users.views.user', {'active_tab': 'activity'}, name='user-activity'),
    url(r'^profile/(?P<username>\w+)/connections$', 'users.views.user', {'active_tab': 'connections'}, name='user-connections'),
    url(r'^profile/(?P<username>\w+)/edit$', 'users.views.user', {'active_tab': 'edit'}, name='user-edit'),

    url(r'^follow/(?P<username>\w+)$', 'users.views.follow', name='follow'),
    url(r'^unfollow/(?P<username>\w+)$', 'users.views.unfollow', name='unfollow'),
)
