from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.contenttypes import generic

from connections.models import Connection

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)

    # connections_in = generic.GenericRelation(Connection,
    #                                          content_type_field='in_content_type',
    #                                          object_id_field='in_object_id',
    #                                          related_name='connections_in',
    #                                          verbose_name='incomming connections')

    # connections_out = generic.GenericRelation(Connection,
    #                                           content_type_field='out_content_type',
    #                                           object_id_field='out_object_id',
    #                                           related_name='connections_out',
    #                                           verbose_name='outgoing connections')

    def get_connections_in(self):
        pass

    def get_connections_out(self):
        pass

    # Additional user profile fields:
    # * Location(s)
    # * Website
    # * Image/avatar
    # * 

    def __unicode__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
