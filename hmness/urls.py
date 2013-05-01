from django.conf.urls import patterns, include, url

# Enabling the admin interface
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hmness.views.home', name='home'),

    url(r'^login$', 'users.views.login', name='login'),
    url(r'^logout$', 'users.views.logout', name='logout'),
    url(r'^auth$', 'users.views.auth', name='auth'),

    url(r'^contact$', 'hmness.views.contact', name='contact'),
    url(r'^about$', 'hmness.views.about', name='about'),

    # Examples:
    # url(r'^hmness/', include('hmness.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
