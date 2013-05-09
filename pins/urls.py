from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^login$', 'users.views.login', name='login'),
    # url(r'^signup$', 'users.views.signup', name='signup'),
    # url(r'^logout$', 'users.views.logout', name='logout'),
    # url(r'^register$', 'users.views.register', name='register'),
    # url(r'^auth$', 'users.views.auth', name='auth'),

    url(r'^profile/(?P<pin_id>\d+)', 'pins.views.pin', name='pin'),

    url(r'^follow/(?P<pin_id>\d+)$', 'pins.views.follow', name='follow'),
    url(r'^unfollow/(?P<pin_id>\d+)$', 'pins.views.unfollow', name='unfollow'),
)
