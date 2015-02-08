from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

class Person(TimeStampedModel):
    user = models.OneToOneField(User)

    tag_uuid = models.CharField(max_length=15)
    is_home = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.user.last_name + ", " + self.user.first_name + " ("+self.user.username+")"

    def __unicode__(self):
        return self.user.last_name + ", " + self.user.first_name + " ("+self.user.username+")"
