from django.conf.urls import patterns, include, url

# Enabling the admin interface
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hmness.views.home', name='home'),

    url(r'^contact$', 'hmness.views.contact', name='contact'),
    url(r'^about$', 'hmness.views.about', name='about'),

    url(r'^u/', include('users.urls', namespace='users')),

    url(r'^p/', include('pins.urls', namespace='pins')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
