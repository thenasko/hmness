from django.db import models
from django.core.urlresolvers import reverse

from connections.models import ConnectionEnd


class PIN(ConnectionEnd):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Joined date
    # Last activity date
    # Image
    # Location
    # Description/wiki
    # Followers

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('pins:pin', kwargs={'pin_id': self.id})

    def get_follow_url(self):
        return reverse('pins:follow', kwargs={'pin_id': self.id})

    def get_unfollow_url(self):
        return reverse('pins:unfollow', kwargs={'pin_id': self.id})

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
