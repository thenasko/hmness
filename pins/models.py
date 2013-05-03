from django.db import models

class PIN(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Joined date
    # Last activity date
    # Image
    # Location
    # Description/wiki
    # Followers
