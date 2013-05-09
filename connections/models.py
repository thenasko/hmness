from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings

from annoying.functions import get_object_or_None
from hmness.shortcuts import diff, intersection

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

class ConnectionEnd(models.Model):
    connections_in = generic.GenericRelation(Connection,
                                             content_type_field='in_content_type',
                                             object_id_field='in_object_id',
                                             related_name='connections_in',
                                             verbose_name='incomming connections')

    connections_out = generic.GenericRelation(Connection,
                                              content_type_field='out_content_type',
                                              object_id_field='out_object_id',
                                              related_name='connections_out',
                                              verbose_name='outgoing connections')

    @property
    def connections_all(self):
        return self.connections_in.all() | self.connections_out.all()

    @property
    def connections_in_objects(self):
        return [c.out_content_object for c in self.connections_in.iterator()]

    @property
    def connections_out_objects(self):
        return [c.in_content_object for c in self.connections_out.iterator()]

    @property
    def connections_in_only(self):
        return diff(self.connections_in_objects, self.connections_out_objects)

    @property
    def connections_out_only(self):
        return diff(self.connections_out_objects, self.connections_in_objects)

    @property
    def connections_in_out(self):
        return intersection(self.connection_in_objects, self.connections_out_objects)

    @property
    def connections_pack(self):
        c_in = self.connections_in_objects
        c_out = self.connections_out_objects
        return (diff(c_in, c_out),
                diff(c_out, c_in),
                intersection(c_in, c_out))

    def get_following_connection(self, object):
        return get_object_or_None(
            self.connections_out,
            in_content_type = ContentType.objects.get_for_model(object),
            in_object_id = object.id)
    
    def is_following(self, object):
        return not(self.get_following_connection(object) is None)

    def follow(self, object):
        if not self.is_following(object):
            c = Connection.objects.create(
                out_content_object=self,
                in_content_object=object)
            c.save()

    def unfollow(self, object):
        c = self.get_following_connection(object)
        if not(c is None):
            c.delete()

    class Meta:
        abstract = True
