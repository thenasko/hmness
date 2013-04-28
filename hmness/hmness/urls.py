from django.conf.urls import patterns, include, url

# Enabling the admin interface
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hmness.views.home', name='home'),
    url(r'^contact$', 'hmness.views.contact', name='contact'),
    # url(r'^hmness/', include('hmness.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
