from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse

#from connections.models import Connection, ConnectionEnd

from hmness.shortcuts import diff, intersection

from actstream.models import following as actstream_following
from actstream.models import followers as actstream_followers

class FollowEnd(models.Model):
    @property
    def follow_object(self):
        raise NotImplementedError("FollowEnd.follow_object is an abstract property.")

    @property
    def following(self):
        return actstream_following(self.follow_object)

    @property
    def followers(self):
        return actstream_followers(self.follow_object)

    @property
    def following_only(self):
        return diff(self.following, self.followers)

    @property
    def followers_only(self):
        return diff(self.followers, self.following)

    @property
    def follow_profile(self):
        self_following = self.following
        self_followers = self.followers
        return (diff(self_following, self_followers),
                diff(self_followers, self_following),
                intersection(self_following, self_followers))

    @property
    def following_count(self):
        return len(self.following)

    @property
    def followers_count(self):
        return len(self.followers)

    # TODO: is_following, follow, unfollow
    # TODO: name, __str__, __unicode__

    class Meta:
        abstract = True
    

class UserProfile(FollowEnd):
    user = models.OneToOneField(User, unique=True)

    @property
    def name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse('users:user', kwargs={'username': self.user.username})

    @property
    def follow_object(self):
        return self.user

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


