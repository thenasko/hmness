from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)

    # Additional user profile fields
    #

    def __unicode__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, insrance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)