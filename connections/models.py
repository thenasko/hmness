from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings

class Connection(models.Model):
    in_content_type = models.ForeignKey(ContentType,
                                        limit_choices_to=settings.CONNECTIONS_MODELS_LIMIT,
                                        related_name='in_set')
    in_object_id = models.PositiveIntegerField()
    in_content_object = generic.GenericForeignKey('in_content_type', 'in_object_id')

    out_content_type = models.ForeignKey(ContentType,
                                         limit_choices_to=settings.CONNECTIONS_MODELS_LIMIT,
                                         related_name='out_set')
    out_object_id = models.PositiveIntegerField()
    out_content_object = generic.GenericForeignKey('out_content_type', 'out_object_id')

    def __unicode__(self):
        return "Connection from %s to %s" % (self.out_content_object, self.in_content_object)
