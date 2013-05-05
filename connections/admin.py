from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from connections.models import Connection

class ConnectionInInline(GenericTabularInline):
    model = Connection
    ct_field = 'in_content_type'
    ct_fk_field = 'in_object_id'

class ConnectionOutInline(GenericTabularInline):
    model = Connection
    ct_field = 'out_content_type'
    ct_fk_field = 'out_object_id'

admin.site.register(Connection)
