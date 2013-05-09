from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse

from connections.models import Connection, ConnectionEnd

class UserProfile(ConnectionEnd):
    user = models.OneToOneField(User, unique=True)

    @property
    def name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse('users:user', kwargs={'username': self.user.username})

    def get_follow_url(self):
        return reverse('users:follow', kwargs={'username': self.user.username})

    def get_unfollow_url(self):
        return reverse('users:unfollow', kwargs={'username': self.user.username})

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
