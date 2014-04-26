from django.db import models

# Create your models here.


class Alumni(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    year = models.IntegerField()
    track = models.CharField(max_length=30)
    lfw = models.BooleanField(default=False)
    lat = models.BigIntegerField()
    long = models.BigIntegerField()

    def __unicode__(self):
        return "{} - {} - {} - {} - Track: {} Looking For Work: {}".format(self.name,
                                                                           self.email,
                                                                           self.year,
                                                                           self.track,
                                                                           self.lfw)
