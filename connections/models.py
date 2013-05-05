from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Connection(models.Model):
    in_content_type = models.ForeignKey(ContentType, related_name='in_set')
    in_object_id = models.PositiveIntegerField()
    in_content_object = generic.GenericForeignKey('in_content_type', 'in_object_id')

    out_content_type = models.ForeignKey(ContentType, related_name='out_set')
    out_object_id = models.PositiveIntegerField()
    out_content_object = generic.GenericForeignKey('out_content_type', 'out_object_id')
